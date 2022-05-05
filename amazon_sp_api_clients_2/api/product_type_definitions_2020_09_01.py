"""
Selling Partner API for Product Type Definitions
=============================================================================================

The Selling Partner API for Product Type Definitions provides programmatic access to attribute and data requirements for product types in the Amazon catalog. Use this API to return the JSON Schema for a product type that you can then use with other Selling Partner APIs, such as the Selling Partner API for Listings Items, the Selling Partner API for Catalog Items, and the Selling Partner API for Feeds (for JSON-based listing feeds).

For more information, see the [Product Type Definitions API Use Case Guide](doc:product-type-api-use-case-guide).
API Version: 2020-09-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'items': Reference(ref='#/components/schemas/Error'), 'type': 'array'}

    pass


@attrs.define
class ProductType:

    marketplace_ids: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'string'}

    pass


@attrs.define
class ProductTypeDefinition:

    locale: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'string'}
    marketplace_ids: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    product_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'string'}
    property_groups: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'additionalProperties': Reference(ref='#/components/schemas/PropertyGroup'), 'type': 'object'}
    requirements: Union[Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'enum': ['LISTING', 'LISTING_PRODUCT_ONLY', 'LISTING_OFFER_ONLY'], 'type': 'string'}
    requirements_enforced: Union[Literal["ENFORCED"], Literal["NOT_ENFORCED"]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'enum': ['ENFORCED', 'NOT_ENFORCED'], 'type': 'string'}

    meta_schema: dict[str, Any]
    # {'ref': '#/components/schemas/SchemaLink', 'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>}
    product_type_version: dict[str, Any]
    # {'ref': '#/components/schemas/ProductTypeVersion', 'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>}
    schema: dict[str, Any]
    # {'ref': '#/components/schemas/SchemaLink', 'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>}
    pass


@attrs.define
class ProductTypeList:

    product_types: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'items': Reference(ref='#/components/schemas/ProductType'), 'type': 'array'}

    pass


@attrs.define
class ProductTypeVersion:

    latest: bool
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'boolean'}
    release_candidate: bool
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'boolean'}
    version: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'string'}

    pass


@attrs.define
class PropertyGroup:

    description: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'string'}
    property_names: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    title: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'string'}

    pass


@attrs.define
class SchemaLink:

    checksum: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'type': 'string'}
    link: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C7E53F0>, 'properties': {'resource': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='URI resource for the link.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'verb': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=['GET'], type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='HTTP method for the link operation.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}, 'type': 'object', 'required': ['resource', 'verb']}

    pass


class ProductTypeDefinitions20200901Client(BaseClient):
    def get_definitions_product_type(
        self,
        product_type: str,
        marketplace_ids: list[str],
        seller_id: str = None,
        product_type_version: str = None,
        requirements: Union[Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]] = None,
        requirements_enforced: Union[Literal["ENFORCED"], Literal["NOT_ENFORCED"]] = None,
        locale: Union[
            Literal["DEFAULT"],
            Literal["ar"],
            Literal["ar_AE"],
            Literal["de"],
            Literal["de_DE"],
            Literal["en"],
            Literal["en_AE"],
            Literal["en_AU"],
            Literal["en_CA"],
            Literal["en_GB"],
            Literal["en_IN"],
            Literal["en_SG"],
            Literal["en_US"],
            Literal["es"],
            Literal["es_ES"],
            Literal["es_MX"],
            Literal["es_US"],
            Literal["fr"],
            Literal["fr_CA"],
            Literal["fr_FR"],
            Literal["it"],
            Literal["it_IT"],
            Literal["ja"],
            Literal["ja_JP"],
            Literal["nl"],
            Literal["nl_NL"],
            Literal["pl"],
            Literal["pl_PL"],
            Literal["pt"],
            Literal["pt_BR"],
            Literal["pt_PT"],
            Literal["sv"],
            Literal["sv_SE"],
            Literal["tr"],
            Literal["tr_TR"],
            Literal["zh"],
            Literal["zh_CN"],
            Literal["zh_TW"],
        ] = None,
    ):
        """
        Retrieve an Amazon product type definition.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            product_type: The Amazon product type name.
            seller_id: A selling partner identifier. When provided, seller-specific requirements and values are populated within the product type definition schema, such as brand names associated with the selling partner.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
                Note: This parameter is limited to one marketplaceId at this time.
            product_type_version: The version of the Amazon product type to retrieve. Defaults to "LATEST",. Prerelease versions of product type definitions may be retrieved with "RELEASE_CANDIDATE". If no prerelease version is currently available, the "LATEST" live version will be provided.
            requirements: The name of the requirements set to retrieve requirements for.
            requirements_enforced: Identifies if the required attributes for a requirements set are enforced by the product type definition schema. Non-enforced requirements enable structural validation of individual attributes without all the required attributes being present (such as for partial updates).
            locale: Locale for retrieving display labels and other presentation details. Defaults to the default language of the first marketplace in the request.
        """
        url = "/definitions/2020-09-01/productTypes/{productType}"
        values = (
            product_type,
            seller_id,
            marketplace_ids,
            product_type_version,
            requirements,
            requirements_enforced,
            locale,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_definitions_product_type_params)
        return response

    _get_definitions_product_type_params = (  # name, param in
        ("productType", "path"),
        ("sellerId", "query"),
        ("marketplaceIds", "query"),
        ("productTypeVersion", "query"),
        ("requirements", "query"),
        ("requirementsEnforced", "query"),
        ("locale", "query"),
    )

    def search_definitions_product_types(
        self,
        marketplace_ids: list[str],
        keywords: list[str] = None,
    ):
        """
        Search for and return a list of Amazon product types that have definitions available.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            keywords: A comma-delimited list of keywords to search product types by.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
        """
        url = "/definitions/2020-09-01/productTypes"
        values = (
            keywords,
            marketplace_ids,
        )
        response = self._parse_args_and_request(url, "GET", values, self._search_definitions_product_types_params)
        return response

    _search_definitions_product_types_params = (  # name, param in
        ("keywords", "query"),
        ("marketplaceIds", "query"),
    )
