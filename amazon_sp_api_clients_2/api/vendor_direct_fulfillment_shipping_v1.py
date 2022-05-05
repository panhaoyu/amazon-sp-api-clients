"""
Selling Partner API for Direct Fulfillment Shipping
=============================================================================================

The Selling Partner API for Direct Fulfillment Shipping provides programmatic access to a direct fulfillment vendor's shipping data.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Address:

    address_line1: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    postal_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    pass


@attrs.define
class Container:

    carrier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    container_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    container_sequence_number: int
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'integer'}
    container_type: Union[Literal["carton"], Literal["pallet"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'enum': ['carton', 'pallet'], 'type': 'string'}
    manifest_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    manifest_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    packed_items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/PackedItem'), 'type': 'array'}
    scac_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    ship_method: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    tracking_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    dimensions: dict[str, Any]
    # {'ref': '#/components/schemas/Dimensions', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class CustomerInvoice:

    content: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    purchase_order_number: str
    # {'pattern': '^[a-zA-Z0-9]+$', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    pass


@attrs.define
class CustomerInvoiceList:

    customer_invoices: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/CustomerInvoice'), 'type': 'array'}

    pagination: dict[str, Any]
    # {'ref': '#/components/schemas/Pagination', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Dimensions:

    unit_of_measure: Union[Literal["IN"], Literal["CM"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'enum': ['IN', 'CM'], 'type': 'string'}

    height: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    length: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    width: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetCustomerInvoiceResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/CustomerInvoice', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class GetCustomerInvoicesResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/CustomerInvoiceList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class GetPackingSlipListResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/PackingSlipList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class GetPackingSlipResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/PackingSlip', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class GetShippingLabelListResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingLabelList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class GetShippingLabelResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingLabel', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class Item:

    buyer_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    item_sequence_number: int
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'integer'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    shipped_quantity: dict[str, Any]
    # {'ref': '#/components/schemas/ItemQuantity', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class ItemQuantity:

    amount: int
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'integer'}
    unit_of_measure: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    pass


@attrs.define
class LabelData:

    content: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    package_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    ship_method: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    ship_method_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    tracking_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    pass


@attrs.define
class PackedItem:

    buyer_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    item_sequence_number: int
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'integer'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    packed_quantity: dict[str, Any]
    # {'ref': '#/components/schemas/ItemQuantity', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class PackingSlip:

    content: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    content_type: Union[Literal["application/pdf"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'enum': ['application/pdf'], 'type': 'string'}
    purchase_order_number: str
    # {'pattern': '^[a-zA-Z0-9]+$', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    pass


@attrs.define
class PackingSlipList:

    packing_slips: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/PackingSlip'), 'type': 'array'}

    pagination: dict[str, Any]
    # {'ref': '#/components/schemas/Pagination', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class Pagination:

    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    tax_registration_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/TaxRegistrationDetails'), 'type': 'array'}

    address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class ShipmentConfirmation:

    containers: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/Container'), 'type': 'array'}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/Item'), 'type': 'array'}
    purchase_order_number: str
    # {'pattern': '^[a-zA-Z0-9]+$', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    selling_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    ship_from_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    shipment_details: dict[str, Any]
    # {'ref': '#/components/schemas/ShipmentDetails', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class ShipmentDetails:

    estimated_delivery_date: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    is_priority_shipment: bool
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'boolean'}
    shipment_status: Union[Literal["SHIPPED"], Literal["FLOOR_DENIAL"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'enum': ['SHIPPED', 'FLOOR_DENIAL'], 'type': 'string'}
    shipped_date: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    vendor_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    pass


@attrs.define
class ShipmentStatusUpdate:

    purchase_order_number: str
    # {'pattern': '^[a-zA-Z0-9]+$', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    selling_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    ship_from_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    status_update_details: dict[str, Any]
    # {'ref': '#/components/schemas/StatusUpdateDetails', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class ShippingLabel:

    label_data: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/LabelData'), 'type': 'array'}
    label_format: Union[Literal["PNG"], Literal["ZPL"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'enum': ['PNG', 'ZPL'], 'type': 'string'}
    purchase_order_number: str
    # {'pattern': '^[a-zA-Z0-9]+$', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    selling_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    ship_from_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class ShippingLabelList:

    shipping_labels: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/ShippingLabel'), 'type': 'array'}

    pagination: dict[str, Any]
    # {'ref': '#/components/schemas/Pagination', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class ShippingLabelRequest:

    containers: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/Container'), 'type': 'array'}
    purchase_order_number: str
    # {'pattern': '^[a-zA-Z0-9]+$', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    selling_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    ship_from_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class StatusUpdateDetails:

    reason_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    shipment_schedule: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'properties': {'estimatedDeliveryDateTime': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='Date on which the shipment is expected to reach the customer delivery location. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.', schema_format='date-time', default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'apptWindowStartDateTime': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='This field indicates the date and time at the start of the appointment window scheduled to deliver the shipment. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.', schema_format='date-time', default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'apptWindowEndDateTime': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='This field indicates the date and time at the end of the appointment window scheduled to deliver the shipment. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.', schema_format='date-time', default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}, 'type': 'object'}
    status_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    status_date_time: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    tracking_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    status_location_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class SubmitShipmentConfirmationsRequest:

    shipment_confirmations: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/ShipmentConfirmation'), 'type': 'array'}

    pass


@attrs.define
class SubmitShipmentConfirmationsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/TransactionReference', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class SubmitShipmentStatusUpdatesRequest:

    shipment_status_updates: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/ShipmentStatusUpdate'), 'minItems': 1, 'type': 'array'}

    pass


@attrs.define
class SubmitShipmentStatusUpdatesResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/TransactionReference', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class SubmitShippingLabelsRequest:

    shipping_label_requests: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'items': Reference(ref='#/components/schemas/ShippingLabelRequest'), 'type': 'array'}

    pass


@attrs.define
class SubmitShippingLabelsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/TransactionReference', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_messages: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    tax_registration_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'enum': ['VAT', 'GST'], 'type': 'string'}

    tax_registration_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


@attrs.define
class TransactionReference:

    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'type': 'string'}

    pass


@attrs.define
class Weight:

    unit_of_measure: Union[Literal["KG"], Literal["LB"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>, 'enum': ['KG', 'LB'], 'type': 'string'}

    value: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB700>}
    pass


class VendorDirectFulfillmentShippingV1Client(BaseClient):
    def get_customer_invoice(
        self,
        purchase_order_number: str,
    ):
        """
        Returns a customer invoice based on the purchaseOrderNumber that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchase_order_number: Purchase order number of the shipment for which to return the invoice.
        """
        url = "/vendor/directFulfillment/shipping/v1/customerInvoices/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(url, "GET", values, self._get_customer_invoice_params)
        return response

    _get_customer_invoice_params = (("purchaseOrderNumber", "path"),)  # name, param in

    def get_customer_invoices(
        self,
        created_after: str,
        created_before: str,
        ship_from_party_id: str = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
    ):
        """
        Returns a list of customer invoices created during a time frame that you specify. You define the  time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must be no more than 7 days.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            ship_from_party_id: The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            limit: The limit to the number of records returned
            created_after: Orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort ASC or DESC by order creation date.
            next_token: Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call.
        """
        url = "/vendor/directFulfillment/shipping/v1/customerInvoices"
        values = (
            ship_from_party_id,
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_customer_invoices_params)
        return response

    _get_customer_invoices_params = (  # name, param in
        ("shipFromPartyId", "query"),
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
    )

    def get_packing_slip(
        self,
        purchase_order_number: str,
    ):
        """
        Returns a packing slip based on the purchaseOrderNumber that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchase_order_number: The purchaseOrderNumber for the packing slip you want.
        """
        url = "/vendor/directFulfillment/shipping/v1/packingSlips/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(url, "GET", values, self._get_packing_slip_params)
        return response

    _get_packing_slip_params = (("purchaseOrderNumber", "path"),)  # name, param in

    def get_packing_slips(
        self,
        created_after: str,
        created_before: str,
        ship_from_party_id: str = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
    ):
        """
        Returns a list of packing slips for the purchase orders that match the criteria specified. Date range to search must not be more than 7 days.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            ship_from_party_id: The vendor warehouseId for order fulfillment. If not specified the result will contain orders for all warehouses.
            limit: The limit to the number of records returned
            created_after: Packing slips that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Packing slips that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort ASC or DESC by packing slip creation date.
            next_token: Used for pagination when there are more packing slips than the specified result size limit. The token value is returned in the previous API call.
        """
        url = "/vendor/directFulfillment/shipping/v1/packingSlips"
        values = (
            ship_from_party_id,
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_packing_slips_params)
        return response

    _get_packing_slips_params = (  # name, param in
        ("shipFromPartyId", "query"),
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
    )

    def get_shipping_label(
        self,
        purchase_order_number: str,
    ):
        """
        Returns a shipping label for the purchaseOrderNumber that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchase_order_number: The purchase order number for which you want to return the shipping label. It should be the same purchaseOrderNumber as received in the order.
        """
        url = "/vendor/directFulfillment/shipping/v1/shippingLabels/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(url, "GET", values, self._get_shipping_label_params)
        return response

    _get_shipping_label_params = (("purchaseOrderNumber", "path"),)  # name, param in

    def get_shipping_labels(
        self,
        created_after: str,
        created_before: str,
        ship_from_party_id: str = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
    ):
        """
        Returns a list of shipping labels created during the time frame that you specify. You define that time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must not be more than 7 days.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            ship_from_party_id: The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            limit: The limit to the number of records returned.
            created_after: Shipping labels that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Shipping labels that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort ASC or DESC by order creation date.
            next_token: Used for pagination when there are more ship labels than the specified result size limit. The token value is returned in the previous API call.
        """
        url = "/vendor/directFulfillment/shipping/v1/shippingLabels"
        values = (
            ship_from_party_id,
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_shipping_labels_params)
        return response

    _get_shipping_labels_params = (  # name, param in
        ("shipFromPartyId", "query"),
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
    )

    def submit_shipment_confirmations(
        self,
    ):
        """
        Submits one or more shipment confirmations for vendor orders.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/vendor/directFulfillment/shipping/v1/shipmentConfirmations"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_shipment_confirmations_params)
        return response

    _submit_shipment_confirmations_params = ()  # name, param in

    def submit_shipment_status_updates(
        self,
    ):
        """
        This API call is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API will submit a shipment status update for the package that a vendor has shipped. It will provide the Amazon customer visibility on their order, when the package is outside of Amazon Network visibility.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/vendor/directFulfillment/shipping/v1/shipmentStatusUpdates"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_shipment_status_updates_params)
        return response

    _submit_shipment_status_updates_params = ()  # name, param in

    def submit_shipping_label_request(
        self,
    ):
        """
        Creates a shipping label for a purchase order and returns a transactionId for reference.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/vendor/directFulfillment/shipping/v1/shippingLabels"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_shipping_label_request_params)
        return response

    _submit_shipping_label_request_params = ()  # name, param in
