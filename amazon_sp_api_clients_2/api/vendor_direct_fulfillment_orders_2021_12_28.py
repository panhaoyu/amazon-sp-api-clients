"""
Selling Partner API for Direct Fulfillment Orders
=============================================================================================

The Selling Partner API for Direct Fulfillment Orders provides programmatic access to a direct fulfillment vendor's order data.
API Version: 2021-12-28
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AcknowledgementStatus:
    """
    Status of acknowledgement.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _acknowledgement_status_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AcknowledgementStatus(**data)

    code: Optional[str] = attrs.field()
    """
    Acknowledgement code is a unique two digit value which indicates the status of the acknowledgement. For a list of acknowledgement codes that Amazon supports, see the Vendor Direct Fulfillment APIs Use Case Guide.
    """

    description: Optional[str] = attrs.field()
    """
    Reason for the acknowledgement code.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    Address of the party.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Address(**data)

    address_line1: str = attrs.field()
    """
    First line of the address.
    """

    address_line2: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional address information, if required.
    """

    address_line3: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional address information, if required.
    """

    attention: Optional[str] = attrs.field(
        default=None,
    )
    """
    The attention name of the person at that address.
    """

    city: Optional[str] = attrs.field(
        default=None,
    )
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field()
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.
    """

    county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The county where person, business or institution is located.
    """

    district: Optional[str] = attrs.field(
        default=None,
    )
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field()
    """
    The name of the person, business or institution at that address.
    """

    phone: Optional[str] = attrs.field(
        default=None,
    )
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The postal code of that address. It conatins a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: str = attrs.field()
    """
    The state or region where person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _decimal_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Decimal(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Error(**data)

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_list_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ErrorList(**data)

    errors: List["Error"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GiftDetails:
    """
    Gift details for the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _gift_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GiftDetails(**data)

    gift_message: Optional[str] = attrs.field()
    """
    Gift message to be printed in shipment.
    """

    gift_wrap_id: Optional[str] = attrs.field()
    """
    Gift wrap identifier for the gift wrapping, if any.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    Details of quantity ordered.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_quantity_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ItemQuantity(**data)

    amount: Optional[int] = attrs.field()
    """
    Acknowledged quantity. This value should not be zero.
    """

    unit_of_measure: Optional[Union[Literal["Each"]]] = attrs.field()
    """
    Unit of measure for the acknowledged quantity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _money_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Money(**data)

    amount: Optional["Decimal"] = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
    """

    currency_code: Optional[str] = attrs.field()
    """
    Three digit currency code in ISO 4217 format. String of length 3.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Order:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Order(**data)

    order_details: Optional["OrderDetails"] = attrs.field(
        default=None,
    )
    """
    Details of an order.
    """

    purchase_order_number: str = attrs.field()
    """
    The purchase order number for this order. Formatting Notes: alpha-numeric code.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderAcknowledgementItem:
    """
    Details of an individual order being acknowledged.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_acknowledgement_item_name_convert
        data = {name_convert[k]: v for k, v in data}
        return OrderAcknowledgementItem(**data)

    acknowledgement_date: datetime = attrs.field()
    """
    The date and time when the order is acknowledged, in ISO-8601 date/time format. For example: 2018-07-16T23:00:00Z / 2018-07-16T23:00:00-05:00 / 2018-07-16T23:00:00-08:00.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    acknowledgement_status: "AcknowledgementStatus" = attrs.field()
    """
    Status of acknowledgement.
    """

    item_acknowledgements: List["OrderItemAcknowledgement"] = attrs.field()
    """
    Item details including acknowledged quantity.
    """

    purchase_order_number: str = attrs.field()
    """
    The purchase order number for this order. Formatting Notes: alpha-numeric code.
    """

    selling_party: "PartyIdentification" = attrs.field()

    ship_from_party: "PartyIdentification" = attrs.field()

    vendor_order_number: str = attrs.field()
    """
    The vendor's order number for this order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderDetails:
    """
    Details of an order.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return OrderDetails(**data)

    bill_to_party: "PartyIdentification" = attrs.field()

    customer_order_number: str = attrs.field()
    """
    The customer order number.
    """

    items: List["OrderItem"] = attrs.field()
    """
    A list of items in this purchase order.
    """

    order_date: datetime = attrs.field()
    """
    The date the order was placed. This  field is expected to be in ISO-8601 date/time format, for example:2018-07-16T23:00:00Z/ 2018-07-16T23:00:00-05:00 /2018-07-16T23:00:00-08:00. If no time zone is specified, UTC should be assumed.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    order_status: Optional[
        Union[Literal["NEW"], Literal["SHIPPED"], Literal["ACCEPTED"], Literal["CANCELLED"]]
    ] = attrs.field(
        default=None,
    )
    """
    Current status of the order.
    """

    selling_party: "PartyIdentification" = attrs.field()

    ship_from_party: "PartyIdentification" = attrs.field()

    ship_to_party: "Address" = attrs.field()
    """
    Address of the party.
    """

    shipment_details: "ShipmentDetails" = attrs.field()
    """
    Shipment details required for the shipment.
    """

    tax_total: Optional["TaxItemDetails"] = attrs.field(
        default=None,
    )
    """
    Total tax details for the line item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItem:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_item_name_convert
        data = {name_convert[k]: v for k, v in data}
        return OrderItem(**data)

    buyer_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Buyer's standard identification number (ASIN) of an item.
    """

    gift_details: Optional["GiftDetails"] = attrs.field(
        default=None,
    )
    """
    Gift details for the item.
    """

    item_sequence_number: str = attrs.field()
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    net_price: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    ordered_quantity: "ItemQuantity" = attrs.field()
    """
    Details of quantity ordered.
    """

    scheduled_delivery_shipment: Optional["ScheduledDeliveryShipment"] = attrs.field(
        default=None,
    )
    """
    Dates for the scheduled delivery shipments.
    """

    tax_details: Optional["TaxItemDetails"] = attrs.field(
        default=None,
    )
    """
    Total tax details for the line item.
    """

    title: Optional[str] = attrs.field(
        default=None,
    )
    """
    Title for the item.
    """

    total_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    vendor_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor selected product identification of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemAcknowledgement:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_item_acknowledgement_name_convert
        data = {name_convert[k]: v for k, v in data}
        return OrderItemAcknowledgement(**data)

    acknowledged_quantity: "ItemQuantity" = attrs.field()
    """
    Details of quantity ordered.
    """

    buyer_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Buyer's standard identification number (ASIN) of an item.
    """

    item_sequence_number: str = attrs.field()
    """
    Line item sequence number for the item.
    """

    vendor_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor selected product identification of the item. Should be the same as was provided in the purchase order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderList:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_list_name_convert
        data = {name_convert[k]: v for k, v in data}
        return OrderList(**data)

    orders: Optional[List["Order"]] = attrs.field()

    pagination: Optional["Pagination"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pagination:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _pagination_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Pagination(**data)

    next_token: Optional[str] = attrs.field()
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _party_identification_name_convert
        data = {name_convert[k]: v for k, v in data}
        return PartyIdentification(**data)

    address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    Address of the party.
    """

    party_id: str = attrs.field()
    """
    Assigned identification for the party. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    tax_info: Optional["TaxRegistrationDetails"] = attrs.field(
        default=None,
    )
    """
    Tax registration details of the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ScheduledDeliveryShipment:
    """
    Dates for the scheduled delivery shipments.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _scheduled_delivery_shipment_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ScheduledDeliveryShipment(**data)

    earliest_nominated_delivery_date: Optional[datetime] = attrs.field()
    """
    Earliest nominated delivery date for the scheduled delivery.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    latest_nominated_delivery_date: Optional[datetime] = attrs.field()
    """
    Latest nominated delivery date for the scheduled delivery.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    scheduled_delivery_service_type: Optional[str] = attrs.field()
    """
    Scheduled delivery service type.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentDates:
    """
    Shipment dates.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_dates_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ShipmentDates(**data)

    promised_delivery_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    Delivery date promised to the Amazon customer.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    required_ship_date: datetime = attrs.field()
    """
    Time by which the vendor is required to ship the order.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentDetails:
    """
    Shipment details required for the shipment.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ShipmentDetails(**data)

    is_gift: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the order contain a gift. Include the gift message and gift wrap information.
    """

    is_priority_shipment: bool = attrs.field()
    """
    When true, this is a priority shipment.
    """

    is_pslip_required: bool = attrs.field()
    """
    When true, a packing slip is required to be sent to the customer.
    """

    is_scheduled_delivery_shipment: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, this order is part of a scheduled delivery program.
    """

    message_to_customer: str = attrs.field()
    """
    Message to customer for order status.
    """

    ship_method: str = attrs.field()
    """
    Ship method to be used for shipping the order. Amazon defines ship method codes indicating the shipping carrier and shipment service level. To see the full list of ship methods in use, including both the code and the friendly name, search the 'Help' section on Vendor Central for 'ship methods'.
    """

    shipment_dates: "ShipmentDates" = attrs.field()
    """
    Shipment dates.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitAcknowledgementRequest:
    """
    The request schema for the submitAcknowledgement operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_acknowledgement_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SubmitAcknowledgementRequest(**data)

    order_acknowledgements: Optional[List["OrderAcknowledgementItem"]] = attrs.field()
    """
    A list of one or more purchase orders.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitAcknowledgementResponse:
    """
    The response schema for the submitAcknowledgement operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_acknowledgement_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SubmitAcknowledgementResponse(**data)

    errors: Optional["ErrorList"] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxDetails:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _tax_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TaxDetails(**data)

    tax_amount: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    tax_rate: Optional["Decimal"] = attrs.field(
        default=None,
    )
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
    """

    taxable_amount: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    type: Optional[
        Union[
            Literal["CONSUMPTION"],
            Literal["GST"],
            Literal["MwSt."],
            Literal["PST"],
            Literal["TOTAL"],
            Literal["TVA"],
            Literal["VAT"],
        ]
    ] = attrs.field(
        default=None,
    )
    """
    Tax type.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxItemDetails:
    """
    Total tax details for the line item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _tax_item_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TaxItemDetails(**data)

    tax_line_item: Optional[List["TaxDetails"]] = attrs.field()
    """
    A list of tax line items.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _tax_registration_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TaxRegistrationDetails(**data)

    tax_registration_address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    Address of the party.
    """

    tax_registration_messages: Optional[str] = attrs.field(
        default=None,
    )
    """
    Tax registration message that can be used for additional tax related details.
    """

    tax_registration_number: str = attrs.field()
    """
    Tax registration number for the party. For example, VAT ID.
    """

    tax_registration_type: Optional[Union[Literal["VAT"], Literal["GST"]]] = attrs.field(
        default=None,
    )
    """
    Tax registration type for the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionId:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transaction_id_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TransactionId(**data)

    transaction_id: Optional[str] = attrs.field()
    """
    GUID assigned by Amazon to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


_acknowledgement_status_name_convert = {
    "code": "code",
    "description": "description",
}

_address_name_convert = {
    "addressLine1": "address_line1",
    "addressLine2": "address_line2",
    "addressLine3": "address_line3",
    "attention": "attention",
    "city": "city",
    "countryCode": "country_code",
    "county": "county",
    "district": "district",
    "name": "name",
    "phone": "phone",
    "postalCode": "postal_code",
    "stateOrRegion": "state_or_region",
}

_decimal_name_convert = {}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_error_list_name_convert = {
    "errors": "errors",
}

_gift_details_name_convert = {
    "giftMessage": "gift_message",
    "giftWrapId": "gift_wrap_id",
}

_item_quantity_name_convert = {
    "amount": "amount",
    "unitOfMeasure": "unit_of_measure",
}

_money_name_convert = {
    "amount": "amount",
    "currencyCode": "currency_code",
}

_order_name_convert = {
    "orderDetails": "order_details",
    "purchaseOrderNumber": "purchase_order_number",
}

_order_acknowledgement_item_name_convert = {
    "acknowledgementDate": "acknowledgement_date",
    "acknowledgementStatus": "acknowledgement_status",
    "itemAcknowledgements": "item_acknowledgements",
    "purchaseOrderNumber": "purchase_order_number",
    "sellingParty": "selling_party",
    "shipFromParty": "ship_from_party",
    "vendorOrderNumber": "vendor_order_number",
}

_order_details_name_convert = {
    "billToParty": "bill_to_party",
    "customerOrderNumber": "customer_order_number",
    "items": "items",
    "orderDate": "order_date",
    "orderStatus": "order_status",
    "sellingParty": "selling_party",
    "shipFromParty": "ship_from_party",
    "shipToParty": "ship_to_party",
    "shipmentDetails": "shipment_details",
    "taxTotal": "tax_total",
}

_order_item_name_convert = {
    "buyerProductIdentifier": "buyer_product_identifier",
    "giftDetails": "gift_details",
    "itemSequenceNumber": "item_sequence_number",
    "netPrice": "net_price",
    "orderedQuantity": "ordered_quantity",
    "scheduledDeliveryShipment": "scheduled_delivery_shipment",
    "taxDetails": "tax_details",
    "title": "title",
    "totalPrice": "total_price",
    "vendorProductIdentifier": "vendor_product_identifier",
}

_order_item_acknowledgement_name_convert = {
    "acknowledgedQuantity": "acknowledged_quantity",
    "buyerProductIdentifier": "buyer_product_identifier",
    "itemSequenceNumber": "item_sequence_number",
    "vendorProductIdentifier": "vendor_product_identifier",
}

_order_list_name_convert = {
    "orders": "orders",
    "pagination": "pagination",
}

_pagination_name_convert = {
    "nextToken": "next_token",
}

_party_identification_name_convert = {
    "address": "address",
    "partyId": "party_id",
    "taxInfo": "tax_info",
}

_scheduled_delivery_shipment_name_convert = {
    "earliestNominatedDeliveryDate": "earliest_nominated_delivery_date",
    "latestNominatedDeliveryDate": "latest_nominated_delivery_date",
    "scheduledDeliveryServiceType": "scheduled_delivery_service_type",
}

_shipment_dates_name_convert = {
    "promisedDeliveryDate": "promised_delivery_date",
    "requiredShipDate": "required_ship_date",
}

_shipment_details_name_convert = {
    "isGift": "is_gift",
    "isPriorityShipment": "is_priority_shipment",
    "isPslipRequired": "is_pslip_required",
    "isScheduledDeliveryShipment": "is_scheduled_delivery_shipment",
    "messageToCustomer": "message_to_customer",
    "shipMethod": "ship_method",
    "shipmentDates": "shipment_dates",
}

_submit_acknowledgement_request_name_convert = {
    "orderAcknowledgements": "order_acknowledgements",
}

_submit_acknowledgement_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_tax_details_name_convert = {
    "taxAmount": "tax_amount",
    "taxRate": "tax_rate",
    "taxableAmount": "taxable_amount",
    "type": "type",
}

_tax_item_details_name_convert = {
    "taxLineItem": "tax_line_item",
}

_tax_registration_details_name_convert = {
    "taxRegistrationAddress": "tax_registration_address",
    "taxRegistrationMessages": "tax_registration_messages",
    "taxRegistrationNumber": "tax_registration_number",
    "taxRegistrationType": "tax_registration_type",
}

_transaction_id_name_convert = {
    "transactionId": "transaction_id",
}


class VendorDirectFulfillmentOrders20211228Client(BaseClient):
    def get_order(
        self,
        purchase_order_number: str,
    ) -> Union[ErrorList, Order]:
        """
        Returns purchase order information for the purchaseOrderNumber that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            purchase_order_number: The order identifier for the purchase order that you want. Formatting Notes: alpha-numeric code.
        """
        url = "/vendor/directFulfillment/orders/2021-12-28/purchaseOrders/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_order_params,
            self._get_order_responses,
        )
        return response

    _get_order_params = (("purchaseOrderNumber", "path"),)  # name, param in

    _get_order_responses = {
        200: Order,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_orders(
        self,
        created_after: datetime,
        created_before: datetime,
        ship_from_party_id: str = None,
        status: Union[Literal["NEW"], Literal["SHIPPED"], Literal["ACCEPTED"], Literal["CANCELLED"]] = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
        include_details: bool = None,
    ) -> Union[ErrorList, OrderList]:
        """
        Returns a list of purchase orders created during the time frame that you specify. You define the time frame using the createdAfter and createdBefore parameters. You must use both parameters. You can choose to get only the purchase order numbers by setting the includeDetails parameter to false. In that case, the operation returns a list of purchase order numbers. You can then call the getOrder operation to return the details of a specific order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            ship_from_party_id: The vendor warehouse identifier for the fulfillment warehouse. If not specified, the result will contain orders for all warehouses.
            status: Returns only the purchase orders that match the specified status. If not specified, the result will contain orders that match any status.
            limit: The limit to the number of purchase orders returned.
            created_after: Purchase orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Purchase orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort the list in ascending or descending order by order creation date.
            next_token: Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call.
            include_details: When true, returns the complete purchase order details. Otherwise, only purchase order numbers are returned.
        """
        url = "/vendor/directFulfillment/orders/2021-12-28/purchaseOrders"
        values = (
            ship_from_party_id,
            status,
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
            include_details,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_orders_params,
            self._get_orders_responses,
        )
        return response

    _get_orders_params = (  # name, param in
        ("shipFromPartyId", "query"),
        ("status", "query"),
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
        ("includeDetails", "query"),
    )

    _get_orders_responses = {
        200: OrderList,
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def submit_acknowledgement(
        self,
        order_acknowledgements: List["OrderAcknowledgementItem"] = None,
    ) -> Union[ErrorList, TransactionId]:
        """
        Submits acknowledgements for one or more purchase orders.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            order_acknowledgements: A list of one or more purchase orders.
        """
        url = "/vendor/directFulfillment/orders/2021-12-28/acknowledgements"
        values = (order_acknowledgements,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_acknowledgement_params,
            self._submit_acknowledgement_responses,
        )
        return response

    _submit_acknowledgement_params = (("orderAcknowledgements", "body"),)  # name, param in

    _submit_acknowledgement_responses = {
        202: TransactionId,
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }
