import html
import re
import textwrap
from builtins import isinstance
from itertools import chain

import black


class Utils:
    @staticmethod
    def wrap_description(text: str, initial_indent: int = 0, subsequent_indent: int = 4, width=0) -> str:
        """Wrap description with indent and width.

        Args:
            text: the description.
            initial_indent: whitespaces before line 1
            subsequent_indent: whitespaces before line 2 and more
            width: line width

        Returns:
            for indent=4 and left=8:
            --------xxxxxxxxxxxxxxxxxxxx
            ------------xxxxxxxxxxxxxxxx
            ------------xxxxxxxxxxxxxxxx
        """
        lines = text.splitlines()
        result = chain.from_iterable(textwrap.wrap(line, width=width, initial_indent=' ' * initial_indent,
                                                   subsequent_indent=' ' * subsequent_indent) for line in lines)
        return '\n'.join(result)

    @staticmethod
    def get_type_hint(schema):
        from .generator import Schema, ParsedSchema, Reference
        assert isinstance(schema, Schema)
        type_convert = {
            ('integer', None): 'int',
            ('string', None): 'str',
            ('boolean', None): 'bool',
            ('object', None): "Dict[str, {child}]",
            ('array', None): "List[{child}]",
            ('number', None): 'float',
            ('string', 'date-time'): 'datetime',
            ('string', 'date'): 'date',
            ('string', 'boolean'): 'bool',
            ('string', 'uri'): 'str',
            ('string', '[A-Z]{2}'): 'str',
            ('string', 'byte'): 'bytes',
            ('integer', 'int32'): 'int',
            ('integer', 'int64'): 'int',
            ('number', 'double'): 'float',
        }
        if schema is None:
            return 'Any'

        assert schema.type is not None
        probable_fields = {'generator', 'type', 'description', 'name', 'enum', 'maximum', 'minimum', 'items',
                           'minItems', 'maxItems', 'pattern', 'default', 'required', 'minLength', 'maxLength',
                           'uniqueItems', 'example',
                           'schema_format', 'properties', 'additionalProperties',
                           'ref_name', 'is_property', 'parsed_properties'}
        fields = {f for f in schema.__fields_set__ if getattr(schema, f) is not None}
        assert fields.issubset(probable_fields), fields - probable_fields

        child = 'Any'
        if schema.type == 'array':
            child_item = schema.items
            if isinstance(child_item, Reference):
                child = schema.items.ref.split('/')[-1]
                child = f"'{child}'"
            elif isinstance(child_item, Schema):
                child = type_convert[(child_item.type, child_item.schema_format)].format(child='Any')
            else:
                raise TypeError(type(child_item))
        elif isinstance(schema, ParsedSchema) and schema.type == 'object' and schema.ref_name:
            return f"'{schema.ref_name}'"
        type_hint = type_convert[(schema.type, schema.schema_format)].format(child=child)
        assert schema.enum is None or type_hint == 'str'
        choices = ', '.join(f'Literal["{v}"]' for v in schema.enum) if schema.enum is not None else None
        type_hint = f'Union[{choices}]' if type_hint == 'str' and choices is not None else type_hint
        return type_hint

    @staticmethod
    def camel_to_underline(name: str):
        return re.sub('(?<=[a-z])[A-Z]+', lambda m: f'_{m.group(0).lower()}', name).lower()

    @staticmethod
    def camel_to_class_name(name: str):
        return re.sub(r'^_?([a-z])', lambda s: s.group(1).upper(), name)

    @staticmethod
    def underline_to_class_name(name: str):
        return ''.join(word.capitalize() for word in name.split('_'))

    @staticmethod
    def format_python_file(content: str):
        content = html.unescape(content)
        try:
            content = black.format_str(content, mode=black.Mode(line_length=120))
        except black.parsing.InvalidInput:
            content_with_line_number = '\n'.join(
                [f'{index + 1:>3} {line}' for index, line in enumerate(content.splitlines())])
            print(content_with_line_number)
            raise
        return content

    @staticmethod
    def find_new_schema(schema):
        """Find inline schemas, which are not able to convert in python.

        Python type hint for dict do not support inline type hint.
        This method will find the inline schemas and convert to reference, which will be created as classes.

        Args:
            schema: the inline schema

        Returns:
            Like the input arguments, but as a list.
            The first of the tuple is the path of the inline schema, including parent path,
            like ``offer.price.unit``.

        """
        from .generator import ParsedSchema
        from openapi_schema_pydantic.v3.v3_0_3 import Reference

        assert isinstance(schema, ParsedSchema), type(schema)
        new_schemas: list[ParsedSchema] = []

        fields = schema.__fields_set__
        fields = {f for f in fields if getattr(schema, f) is not None}
        fields -= {'type', 'description', 'required', 'properties', 'minLength', 'maxLength', 'enum', 'items',
                   'allOf', 'additionalProperties', 'schema_format', 'maxItems', 'minItems', 'minimum', 'maximum',
                   'example', 'pattern', 'name'}
        assert not fields

        # additional properties only contains simple types, do not need to convert
        if (additional := schema.additionalProperties) is not None:
            assert isinstance(additional, ParsedSchema)
            assert additional.__fields_set__.issubset({'type'})

        if schema.properties:
            for sub_name, sub_schema in schema.properties.items():
                if isinstance(sub_schema, Reference):
                    continue
                assert isinstance(sub_schema, ParsedSchema)
                assert sub_schema.type in ('string', 'integer', 'boolean', 'number', 'array')
                if sub_schema.type == 'array':
                    capitalized_sub_name = Utils.camel_to_class_name(sub_name)

                    if sub_schema.type == 'array':
                        item = sub_schema.items
                        if isinstance(item, Reference):
                            continue
                        assert isinstance(item, ParsedSchema)
                        if item.type in ('string', 'integer', 'boolean', 'number'):
                            continue
                        assert item.type == 'object', item.type
                        item.name = f'{schema.name}{capitalized_sub_name}Item'
                        sub_schema.items = Reference(ref=f"#/components/schemas/{item.name}")
                        new_schemas.append(item)
                        new_schemas.extend(Utils.find_new_schema(item))

        if item := schema.items:
            assert isinstance(item, (Reference, ParsedSchema))
            if isinstance(item, ParsedSchema):
                known = {'type', 'maxLength', 'enum', 'description', 'properties'}
                assert not (v := item.__fields_set__ - known), v
                assert item.type in ('string', 'object')
                if item.type == 'object':
                    assert item.properties is not None
                    item.name = f'{schema.name}Item'
                    schema.items = Reference(ref=f"#/components/schemas/{item.name}")
                    new_schemas.append(item)
                    new_schemas.extend(Utils.find_new_schema(item))
        return new_schemas
