"""
Selling Partner API for Listings Items
=============================================================================================
The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.
For more information, see the [Listing Items API Use Case Guide](doc:listings-items-api-v2020-09-01-use-case-guide).
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2020-09-01
"""
from ..utils.base_client import BaseClient


class ListingsItems20200901Client(BaseClient):
    def put_listings_item(
        self,
        # name='sellerId' param_in='path' description='A selling partner identifier, such as a merchant account or vendor code.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
        # name='sku' param_in='path' description='A selling partner provided identifier for an Amazon listing.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
        # name='marketplaceIds' param_in='query' description='A comma-delimited list of Amazon marketplace identifiers for the request.' required=True deprecated=False allowEmptyValue=False style='form' explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None), contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='array', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example='ATVPDKIKX0DER' examples=None content=None
        # name='issueLocale' param_in='query' description='A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.' required=False deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example='en_US' examples=None content=None
    ):
        url = "/listings/2020-09-01/items/{sellerId}/{sku}"

    def delete_listings_item(
        self,
        # name='sellerId' param_in='path' description='A selling partner identifier, such as a merchant account or vendor code.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
        # name='sku' param_in='path' description='A selling partner provided identifier for an Amazon listing.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
        # name='marketplaceIds' param_in='query' description='A comma-delimited list of Amazon marketplace identifiers for the request.' required=True deprecated=False allowEmptyValue=False style='form' explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None), contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='array', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example='ATVPDKIKX0DER' examples=None content=None
        # name='issueLocale' param_in='query' description='A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.' required=False deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example='en_US' examples=None content=None
    ):
        url = "/listings/2020-09-01/items/{sellerId}/{sku}"

    def patch_listings_item(
        self,
        # name='sellerId' param_in='path' description='A selling partner identifier, such as a merchant account or vendor code.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
        # name='sku' param_in='path' description='A selling partner provided identifier for an Amazon listing.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
        # name='marketplaceIds' param_in='query' description='A comma-delimited list of Amazon marketplace identifiers for the request.' required=True deprecated=False allowEmptyValue=False style='form' explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None), contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='array', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example='ATVPDKIKX0DER' examples=None content=None
        # name='issueLocale' param_in='query' description='A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.' required=False deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example='en_US' examples=None content=None
    ):
        url = "/listings/2020-09-01/items/{sellerId}/{sku}"
