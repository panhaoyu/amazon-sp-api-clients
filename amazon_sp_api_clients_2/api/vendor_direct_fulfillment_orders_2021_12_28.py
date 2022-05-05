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
from typing import Any, List, Dict, Union, Literal


@attrs.define
class AcknowledgementStatus:

    code: str = attrs.field()
    description: str = attrs.field()

    pass


@attrs.define
class Address:

    address_line1: str = attrs.field()
    address_line2: str = attrs.field()
    address_line3: str = attrs.field()
    attention: str = attrs.field()
    city: str = attrs.field()
    country_code: str = attrs.field()
    county: str = attrs.field()
    district: str = attrs.field()
    name: str = attrs.field()
    phone: str = attrs.field()
    postal_code: str = attrs.field()
    state_or_region: str = attrs.field()

    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Error:

    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:

    errors: list["Error"] = attrs.field()

    pass


@attrs.define
class GiftDetails:

    gift_message: str = attrs.field()
    gift_wrap_id: str = attrs.field()

    pass


@attrs.define
class ItemQuantity:

    amount: int = attrs.field()
    unit_of_measure: Union[Literal["Each"]] = attrs.field()

    pass


@attrs.define
class Money:

    currency_code: str = attrs.field()

    amount: "Decimal" = attrs.field()
    pass


@attrs.define
class Order:

    purchase_order_number: str = attrs.field()

    order_details: "OrderDetails" = attrs.field()
    pass


@attrs.define
class OrderAcknowledgementItem:

    acknowledgement_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    item_acknowledgements: list["OrderItemAcknowledgement"] = attrs.field()
    purchase_order_number: str = attrs.field()
    vendor_order_number: str = attrs.field()

    acknowledgement_status: "AcknowledgementStatus" = attrs.field()
    selling_party: "PartyIdentification" = attrs.field()
    ship_from_party: "PartyIdentification" = attrs.field()
    pass


@attrs.define
class OrderDetails:

    customer_order_number: str = attrs.field()
    items: list["OrderItem"] = attrs.field()
    order_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    order_status: Union[Literal["NEW"], Literal["SHIPPED"], Literal["ACCEPTED"], Literal["CANCELLED"]] = attrs.field()

    bill_to_party: "PartyIdentification" = attrs.field()
    selling_party: "PartyIdentification" = attrs.field()
    ship_from_party: "PartyIdentification" = attrs.field()
    ship_to_party: "Address" = attrs.field()
    shipment_details: "ShipmentDetails" = attrs.field()
    tax_total: "TaxItemDetails" = attrs.field()
    pass


@attrs.define
class OrderItem:

    buyer_product_identifier: str = attrs.field()
    item_sequence_number: str = attrs.field()
    title: str = attrs.field()
    vendor_product_identifier: str = attrs.field()

    gift_details: "GiftDetails" = attrs.field()
    net_price: "Money" = attrs.field()
    ordered_quantity: "ItemQuantity" = attrs.field()
    scheduled_delivery_shipment: "ScheduledDeliveryShipment" = attrs.field()
    tax_details: "TaxItemDetails" = attrs.field()
    total_price: "Money" = attrs.field()
    pass


@attrs.define
class OrderItemAcknowledgement:

    buyer_product_identifier: str = attrs.field()
    item_sequence_number: str = attrs.field()
    vendor_product_identifier: str = attrs.field()

    acknowledged_quantity: "ItemQuantity" = attrs.field()
    pass


@attrs.define
class OrderList:

    orders: list["Order"] = attrs.field()

    pagination: "Pagination" = attrs.field()
    pass


@attrs.define
class Pagination:

    next_token: str = attrs.field()

    pass


@attrs.define
class PartyIdentification:

    party_id: str = attrs.field()

    address: "Address" = attrs.field()
    tax_info: "TaxRegistrationDetails" = attrs.field()
    pass


@attrs.define
class ScheduledDeliveryShipment:

    earliest_nominated_delivery_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    latest_nominated_delivery_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    scheduled_delivery_service_type: str = attrs.field()

    pass


@attrs.define
class ShipmentDates:

    promised_delivery_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    required_ship_date: str = attrs.field()
    # {'schema_format': 'date-time'}

    pass


@attrs.define
class ShipmentDetails:

    is_gift: bool = attrs.field()
    is_priority_shipment: bool = attrs.field()
    is_pslip_required: bool = attrs.field()
    is_scheduled_delivery_shipment: bool = attrs.field()
    message_to_customer: str = attrs.field()
    ship_method: str = attrs.field()

    shipment_dates: "ShipmentDates" = attrs.field()
    pass


@attrs.define
class SubmitAcknowledgementRequest:

    order_acknowledgements: list["OrderAcknowledgementItem"] = attrs.field()

    pass


@attrs.define
class SubmitAcknowledgementResponse:

    errors: "ErrorList" = attrs.field()
    payload: "TransactionId" = attrs.field()
    pass


@attrs.define
class TaxDetails:

    type: Union[
        Literal["CONSUMPTION"],
        Literal["GST"],
        Literal["MwSt."],
        Literal["PST"],
        Literal["TOTAL"],
        Literal["TVA"],
        Literal["VAT"],
    ] = attrs.field()

    tax_amount: "Money" = attrs.field()
    tax_rate: "Decimal" = attrs.field()
    taxable_amount: "Money" = attrs.field()
    pass


@attrs.define
class TaxItemDetails:

    tax_line_item: "TaxLineItem" = attrs.field()
    pass


@attrs.define
class TaxLineItem:

    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_messages: str = attrs.field()
    tax_registration_number: str = attrs.field()
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field()

    tax_registration_address: "Address" = attrs.field()
    pass


@attrs.define
class TransactionId:

    transaction_id: str = attrs.field()

    pass


class VendorDirectFulfillmentOrders20211228Client(BaseClient):
    def get_order(
        self,
        purchase_order_number: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_order_params)
        return response

    _get_order_params = (("purchaseOrderNumber", "path"),)  # name, param in

    def get_orders(
        self,
        created_after: str,
        created_before: str,
        ship_from_party_id: str = None,
        status: Union[Literal["NEW"], Literal["SHIPPED"], Literal["ACCEPTED"], Literal["CANCELLED"]] = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
        include_details: str = None,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_orders_params)
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

    def submit_acknowledgement(
        self,
    ):
        """
        Submits acknowledgements for one or more purchase orders.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        """
        url = "/vendor/directFulfillment/orders/2021-12-28/acknowledgements"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_acknowledgement_params)
        return response

    _submit_acknowledgement_params = ()  # name, param in
