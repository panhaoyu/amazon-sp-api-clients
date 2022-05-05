import html
import json
import re
from functools import cached_property
from pathlib import Path

import black
import django.template
from django.conf import settings
from django.shortcuts import render
from django.test import RequestFactory
from openapi_schema_pydantic import Operation, Reference
from openapi_schema_pydantic.v3.v3_0_3 import OpenAPI

settings.configure(TEMPLATES=[{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [Path(__file__).parent / 'templates']
}])
django.setup()


class OperationWithName(Operation):
    path: str
    method: str

    @property
    def method_name(self):
        name = re.sub('(?<=[a-z])[A-Z]+', lambda m: f'_{m.group(0).lower()}', self.operationId)
        # print(f'{self.operationId:>40} | {name}')
        return name


class Generator:
    def __init__(self, path: Path):
        """Generate a sdk client from OpenAPI json.

        Args:
            path: OpenAPI json file version 3.
        """
        self.path = path

    @cached_property
    def data(self) -> OpenAPI:
        with open(self.path) as f:
            data = json.load(f)
        data = OpenAPI.parse_obj(data)

        # servers is useless
        # url='https://sellingpartnerapi-na.amazon.com/' description=None variables=None
        assert len(data.servers) == 1

        return data

    @cached_property
    def components(self):
        return self.data.components

    @cached_property
    def operations(self) -> list[OperationWithName]:
        operations = [OperationWithName(**{'path': path, 'method': method, **getattr(path_item, method).dict()})
                      for path, path_item in self.data.paths.items()
                      for method in path_item.__fields_set__]
        for operation in [o for o in operations if o.parameters is not None]:
            if not any(isinstance(p, Reference) for p in operation.parameters):
                continue
            parameters = operation.parameters
            result = []
            for parameter in operation.parameters:
                if not isinstance(parameter, Reference):
                    result.append(parameter)
                    continue
                ref = parameter.ref
                if not (match := re.match('^#/components/parameters/(.*?)$', ref)):
                    raise ValueError(ref)
                name = match.group(1)
                result.append(self.data.components.parameters[name])
            operation.parameters = parameters
        return operations

    @cached_property
    def content(self):
        content = render(RequestFactory(), 'api.html', {'data': self}).content.decode('utf-8')
        for _ in range(5):
            content = html.unescape(re.sub(r'\n+', '\n', content))
            try:
                content = black.format_str(content, mode=black.Mode(line_length=120))
            except black.parsing.InvalidInput:
                content_with_line_number = '\n'.join(
                    [f'{index + 1:>3} {line}' for index, line in enumerate(content.splitlines())])
                print(content_with_line_number)
                raise
        return content

    @cached_property
    def package_name(self):
        return self.path.stem

    @cached_property
    def class_name(self):
        return ''.join(word.capitalize() for word in self.package_name.split('_'))

    @cached_property
    def directory(self):
        return Path(__file__).parent.parent / 'amazon_sp_api_clients_2' / self.package_name

    def generate(self):
        self.directory.mkdir(parents=True, exist_ok=True)
        with open(self.directory / '__init__.py', 'w') as f:
            f.write('')
        with open(self.directory / 'api.py', 'w') as f:
            f.write(self.content)


def main():
    for json_file in (Path(__file__).parent.parent / 'swagger3_apis').glob('*.json'):
        # if 'listing' not in json_file.stem:
        #     continue
        Generator(json_file).generate()


if __name__ == '__main__':
    main()
