"""
Selling Partner API for Orders
=============================================================================================

The Selling Partner API for Orders helps you programmatically retrieve order information. These APIs let you develop fast, flexible, custom applications in areas like order synchronization, order research, and demand-based decision support tools.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from ..utils.base_object import BaseObject
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class UpdateShipmentStatusRequest(BaseObject):
    """
    Request to update the status of shipment of an order.
    """

    marketplace_id: str = attrs.field(
        default=None,
    )
    """
    the unobfuscated marketplace ID
    """

    order_items: Optional[List["OrderItemsItem"]] = attrs.field(
        default=None,
    )
    """
    the list of order items and quantities when the seller wants to partially update the shipment status of the order
    """

    shipment_status: Union[Literal["ReadyForPickup"], Literal["PickedUp"], Literal["RefusedPickup"]] = attrs.field(
        default=None,
    )
    """
    the status of the shipment of the order to be updated
    """

    _attrs_config = {
        "marketplaceId": ["marketplace_id", "string"],
        "orderItems": ["order_items", "array"],
        "shipmentStatus": ["shipment_status", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class UpdateVerificationStatusRequest(BaseObject):
    """
    Request to update the verification status of an order containing regulated products.
    """

    regulated_order_verification_status: "UpdateVerificationStatusRequestBody" = attrs.field(
        default=None,
    )
    """
    The updated values of the VerificationStatus field.
    """

    _attrs_config = {"regulatedOrderVerificationStatus": ["regulated_order_verification_status", "object"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class UpdateVerificationStatusRequestBody(BaseObject):
    """
    The updated values of the VerificationStatus field.
    """

    external_reviewer_id: str = attrs.field(
        default=None,
    )
    """
    The identifier for the order's regulated information reviewer.
    """

    rejection_reason_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The unique identifier for the rejection reason used for rejecting the order's regulated information. Only required
    if the new status is rejected.
    """

    status: Union[Literal["Approved"], Literal["Rejected"]] = attrs.field(
        default=None,
    )
    """
    The new verification status of the order.
    """

    _attrs_config = {
        "externalReviewerId": ["external_reviewer_id", "string"],
        "rejectionReasonId": ["rejection_reason_id", "string"],
        "status": ["status", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemsItem(BaseObject):

    order_item_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    the unique identifier for the order item
    """

    quantity: Optional[int] = attrs.field(
        default=None,
    )
    """
    the quantity of items that needs an update of the shipment status
    """

    _attrs_config = {"orderItemId": ["order_item_id", "string"], "quantity": ["quantity", "integer"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class UpdateShipmentStatusErrorResponse(BaseObject):
    """
    The error response schema for the UpdateShipmentStatus operation.
    """

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    _attrs_config = {"errors": ["errors", "array"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class UpdateVerificationStatusErrorResponse(BaseObject):
    """
    The error response schema for the UpdateVerificationStatus operation.
    """

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    _attrs_config = {"errors": ["errors", "array"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOrdersResponse(BaseObject):
    """
    The response schema for the getOrders operation.
    """

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrdersList"] = attrs.field(
        default=None,
    )
    """
    A list of orders along with additional information to make subsequent API calls.
    """

    _attrs_config = {"errors": ["errors", "array"], "payload": ["payload", "object"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOrderResponse(BaseObject):
    """
    The response schema for the getOrder operation.
    """

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Order"] = attrs.field(
        default=None,
    )
    """
    Order information.
    """

    _attrs_config = {"errors": ["errors", "array"], "payload": ["payload", "object"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOrderBuyerInfoResponse(BaseObject):
    """
    The response schema for the getOrderBuyerInfo operation.
    """

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrderBuyerInfo"] = attrs.field(
        default=None,
    )
    """
    Buyer information for an order.
    """

    _attrs_config = {"errors": ["errors", "array"], "payload": ["payload", "object"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOrderRegulatedInfoResponse(BaseObject):
    """
    The response schema for the getOrderRegulatedInfo operation.
    """

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrderRegulatedInfo"] = attrs.field(
        default=None,
    )
    """
    The order's regulated information along with its verification status.
    """

    _attrs_config = {"errors": ["errors", "array"], "payload": ["payload", "object"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOrderAddressResponse(BaseObject):
    """
    The response schema for the getOrderAddress operation.
    """

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrderAddress"] = attrs.field(
        default=None,
    )
    """
    The shipping address for the order.
    """

    _attrs_config = {"errors": ["errors", "array"], "payload": ["payload", "object"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOrderItemsResponse(BaseObject):
    """
    The response schema for the getOrderItems operation.
    """

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrderItemsList"] = attrs.field(
        default=None,
    )
    """
    The order items list along with the order ID.
    """

    _attrs_config = {"errors": ["errors", "array"], "payload": ["payload", "object"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOrderItemsBuyerInfoResponse(BaseObject):
    """
    The response schema for the getOrderItemsBuyerInfo operation.
    """

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrderItemsBuyerInfoList"] = attrs.field(
        default=None,
    )
    """
    A single order item's buyer information list with the order ID.
    """

    _attrs_config = {"errors": ["errors", "array"], "payload": ["payload", "object"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrdersList(BaseObject):
    """
    A list of orders along with additional information to make subsequent API calls.
    """

    created_before: Optional[str] = attrs.field(
        default=None,
    )
    """
    A date used for selecting orders created before (or at) a specified time. Only orders placed before the specified
    time are returned. The date must be in ISO 8601 format.
    """

    last_updated_before: Optional[str] = attrs.field(
        default=None,
    )
    """
    A date used for selecting orders that were last updated before (or at) a specified time. An update is defined as any
    change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller.
    All dates must be in ISO 8601 format.
    """

    next_token: Optional[str] = attrs.field(
        default=None,
    )
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """

    orders: List["Order"] = attrs.field(
        default=None,
    )
    """
    A list of orders.
    """

    _attrs_config = {
        "CreatedBefore": ["created_before", "string"],
        "LastUpdatedBefore": ["last_updated_before", "string"],
        "NextToken": ["next_token", "string"],
        "Orders": ["orders", "array"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class Order(BaseObject):
    """
    Order information.
    """

    amazon_order_id: str = attrs.field(
        default=None,
    )
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    automated_shipping_settings: Optional["AutomatedShippingSettings"] = attrs.field(
        default=None,
    )
    """
    Contains information regarding the Shipping Settings Automation program, such as whether the order's shipping
    settings were generated automatically, and what those settings are.
    """

    buyer_info: Optional["BuyerInfo"] = attrs.field(
        default=None,
    )
    """
    Buyer information
    """

    buyer_invoice_preference: Optional[Union[Literal["INDIVIDUAL"], Literal["BUSINESS"]]] = attrs.field(
        default=None,
    )
    """
    The buyer's invoicing preference. Available only in the TR marketplace.
    """

    buyer_tax_information: Optional["BuyerTaxInformation"] = attrs.field(
        default=None,
    )
    """
    Contains the business invoice tax information. Available only in the TR marketplace.
    """

    cba_displayable_shipping_label: Optional[str] = attrs.field(
        default=None,
    )
    """
    Custom ship label for Checkout by Amazon (CBA).
    """

    default_ship_from_location_address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    The shipping address for the order.
    """

    earliest_delivery_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The start of the time period within which you have committed to fulfill the order. In ISO 8601 date time format.
    Returned only for seller-fulfilled orders.
    """

    earliest_ship_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The start of the time period within which you have committed to ship the order. In ISO 8601 date time format.
    Returned only for seller-fulfilled orders.
    Note: EarliestShipDate might not be returned for orders placed before February 1, 2013.
    """

    easy_ship_shipment_status: Optional[str] = attrs.field(
        default=None,
    )
    """
    The status of the Amazon Easy Ship order. This property is included only for Amazon Easy Ship orders.
    Possible values: PendingPickUp, LabelCanceled, PickedUp, OutForDelivery, Damaged, Delivered, RejectedByBuyer,
    Undeliverable, ReturnedToSeller, ReturningToSeller.
    """

    fulfillment_channel: Optional[Union[Literal["MFN"], Literal["AFN"]]] = attrs.field(
        default=None,
    )
    """
    Whether the order was fulfilled by Amazon (AFN) or by the seller (MFN).
    """

    fulfillment_instruction: Optional["FulfillmentInstruction"] = attrs.field(
        default=None,
    )
    """
    Contains the instructions about the fulfillment like where should it be fulfilled from.
    """

    has_regulated_items: Optional[bool] = attrs.field(
        default=None,
    )
    """
    Whether the order contains regulated items which may require additional approval steps before being fulfilled.
    """

    is_business_order: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the order is an Amazon Business order. An Amazon Business order is an order where the buyer is a Verified
    Business Buyer.
    """

    is_estimated_ship_date_set: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the estimated ship date is set for the order. Returned only for Sourcing on Demand orders.
    """

    is_global_express_enabled: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the order is a GlobalExpress order.
    """

    is_iba: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the item within this order was bought and re-sold by Amazon Business EU SARL (ABEU). By buying and
    instantly re-selling your items, ABEU becomes the seller of record, making your inventory available for sale to
    customers who would not otherwise purchase from a third-party seller.
    """

    is_ispu: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, this order is marked to be picked up from a store rather than delivered.
    """

    is_premium_order: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the order has a Premium Shipping Service Level Agreement. For more information about Premium Shipping
    orders, see "Premium Shipping Options" in the Seller Central Help for your marketplace.
    """

    is_prime: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the order is a seller-fulfilled Amazon Prime order.
    """

    is_replacement_order: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, this is a replacement order.
    """

    is_sold_by_ab: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the item within this order was bought and re-sold by Amazon Business EU SARL (ABEU). By buying and
    instantly re-selling your items, ABEU becomes the seller of record, making your inventory available for sale to
    customers who would not otherwise purchase from a third-party seller.
    """

    last_update_date: str = attrs.field(
        default=None,
    )
    """
    The date when the order was last updated.
    Note: LastUpdateDate is returned with an incorrect date for orders that were last updated before 2009-04-01.
    """

    latest_delivery_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The end of the time period within which you have committed to fulfill the order. In ISO 8601 date time format.
    Returned only for seller-fulfilled orders that do not have a PendingAvailability, Pending, or Canceled status.
    """

    latest_ship_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The end of the time period within which you have committed to ship the order. In ISO 8601 date time format. Returned
    only for seller-fulfilled orders.
    Note: LatestShipDate might not be returned for orders placed before February 1, 2013.
    """

    marketplace_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The identifier for the marketplace where the order was placed.
    """

    marketplace_tax_info: Optional["MarketplaceTaxInfo"] = attrs.field(
        default=None,
    )
    """
    Tax information about the marketplace.
    """

    number_of_items_shipped: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of items shipped.
    """

    number_of_items_unshipped: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of items unshipped.
    """

    order_channel: Optional[str] = attrs.field(
        default=None,
    )
    """
    The order channel of the first item in the order.
    """

    order_status: Union[
        Literal["Pending"],
        Literal["Unshipped"],
        Literal["PartiallyShipped"],
        Literal["Shipped"],
        Literal["Canceled"],
        Literal["Unfulfillable"],
        Literal["InvoiceUnconfirmed"],
        Literal["PendingAvailability"],
    ] = attrs.field(
        default=None,
    )
    """
    The current order status.
    """

    order_total: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    order_type: Optional[
        Union[
            Literal["StandardOrder"],
            Literal["LongLeadTimeOrder"],
            Literal["Preorder"],
            Literal["BackOrder"],
            Literal["SourcingOnDemandOrder"],
        ]
    ] = attrs.field(
        default=None,
    )
    """
    The type of the order.
    """

    payment_execution_detail: Optional[List["PaymentExecutionDetailItem"]] = attrs.field(
        default=None,
    )
    """
    A list of payment execution detail items.
    """

    payment_method: Optional[Union[Literal["COD"], Literal["CVS"], Literal["Other"]]] = attrs.field(
        default=None,
    )
    """
    The payment method for the order. This property is limited to Cash On Delivery (COD) and Convenience Store (CVS)
    payment methods. Unless you need the specific COD payment information provided by the PaymentExecutionDetailItem
    object, we recommend using the PaymentMethodDetails property to get payment method information.
    """

    payment_method_details: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    A list of payment method detail items.
    """

    promise_response_due_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    Indicates the date by which the seller must respond to the buyer with an estimated ship date. Returned only for
    Sourcing on Demand orders.
    """

    purchase_date: str = attrs.field(
        default=None,
    )
    """
    The date when the order was created.
    """

    replaced_order_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The order ID value for the order that is being replaced. Returned only if IsReplacementOrder = true.
    """

    sales_channel: Optional[str] = attrs.field(
        default=None,
    )
    """
    The sales channel of the first item in the order.
    """

    seller_display_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller’s friendly name registered in the marketplace.
    """

    seller_order_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    A seller-defined order identifier.
    """

    ship_service_level: Optional[str] = attrs.field(
        default=None,
    )
    """
    The shipment service level of the order.
    """

    shipment_service_level_category: Optional[str] = attrs.field(
        default=None,
    )
    """
    The shipment service level category of the order.
    Possible values: Expedited, FreeEconomy, NextDay, SameDay, SecondDay, Scheduled, Standard.
    """

    shipping_address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    The shipping address for the order.
    """

    _attrs_config = {
        "AmazonOrderId": ["amazon_order_id", "string"],
        "AutomatedShippingSettings": ["automated_shipping_settings", "object"],
        "BuyerInfo": ["buyer_info", "object"],
        "BuyerInvoicePreference": ["buyer_invoice_preference", "string"],
        "BuyerTaxInformation": ["buyer_tax_information", "object"],
        "CbaDisplayableShippingLabel": ["cba_displayable_shipping_label", "string"],
        "DefaultShipFromLocationAddress": ["default_ship_from_location_address", "object"],
        "EarliestDeliveryDate": ["earliest_delivery_date", "string"],
        "EarliestShipDate": ["earliest_ship_date", "string"],
        "EasyShipShipmentStatus": ["easy_ship_shipment_status", "string"],
        "FulfillmentChannel": ["fulfillment_channel", "string"],
        "FulfillmentInstruction": ["fulfillment_instruction", "object"],
        "HasRegulatedItems": ["has_regulated_items", "boolean"],
        "IsBusinessOrder": ["is_business_order", "boolean"],
        "IsEstimatedShipDateSet": ["is_estimated_ship_date_set", "boolean"],
        "IsGlobalExpressEnabled": ["is_global_express_enabled", "boolean"],
        "IsIBA": ["is_iba", "boolean"],
        "IsISPU": ["is_ispu", "boolean"],
        "IsPremiumOrder": ["is_premium_order", "boolean"],
        "IsPrime": ["is_prime", "boolean"],
        "IsReplacementOrder": ["is_replacement_order", "boolean"],
        "IsSoldByAB": ["is_sold_by_ab", "boolean"],
        "LastUpdateDate": ["last_update_date", "string"],
        "LatestDeliveryDate": ["latest_delivery_date", "string"],
        "LatestShipDate": ["latest_ship_date", "string"],
        "MarketplaceId": ["marketplace_id", "string"],
        "MarketplaceTaxInfo": ["marketplace_tax_info", "object"],
        "NumberOfItemsShipped": ["number_of_items_shipped", "integer"],
        "NumberOfItemsUnshipped": ["number_of_items_unshipped", "integer"],
        "OrderChannel": ["order_channel", "string"],
        "OrderStatus": ["order_status", "string"],
        "OrderTotal": ["order_total", "object"],
        "OrderType": ["order_type", "string"],
        "PaymentExecutionDetail": ["payment_execution_detail", "array"],
        "PaymentMethod": ["payment_method", "string"],
        "PaymentMethodDetails": ["payment_method_details", "array"],
        "PromiseResponseDueDate": ["promise_response_due_date", "string"],
        "PurchaseDate": ["purchase_date", "string"],
        "ReplacedOrderId": ["replaced_order_id", "string"],
        "SalesChannel": ["sales_channel", "string"],
        "SellerDisplayName": ["seller_display_name", "string"],
        "SellerOrderId": ["seller_order_id", "string"],
        "ShipServiceLevel": ["ship_service_level", "string"],
        "ShipmentServiceLevelCategory": ["shipment_service_level_category", "string"],
        "ShippingAddress": ["shipping_address", "object"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderBuyerInfo(BaseObject):
    """
    Buyer information for an order.
    """

    amazon_order_id: str = attrs.field(
        default=None,
    )
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    buyer_county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The county of the buyer.
    """

    buyer_email: Optional[str] = attrs.field(
        default=None,
    )
    """
    The anonymized email address of the buyer.
    """

    buyer_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The name of the buyer.
    """

    buyer_tax_info: Optional["BuyerTaxInfo"] = attrs.field(
        default=None,
    )
    """
    Tax information about the buyer.
    """

    purchase_order_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The purchase order (PO) number entered by the buyer at checkout. Returned only for orders where the buyer entered a
    PO number at checkout.
    """

    _attrs_config = {
        "AmazonOrderId": ["amazon_order_id", "string"],
        "BuyerCounty": ["buyer_county", "string"],
        "BuyerEmail": ["buyer_email", "string"],
        "BuyerName": ["buyer_name", "string"],
        "BuyerTaxInfo": ["buyer_tax_info", "object"],
        "PurchaseOrderNumber": ["purchase_order_number", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderRegulatedInfo(BaseObject):
    """
    The order's regulated information along with its verification status.
    """

    amazon_order_id: str = attrs.field(
        default=None,
    )
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    regulated_information: "RegulatedInformation" = attrs.field(
        default=None,
    )
    """
    The regulated information collected during purchase and used to verify the order.
    """

    regulated_order_verification_status: "RegulatedOrderVerificationStatus" = attrs.field(
        default=None,
    )
    """
    The verification status of the order along with associated approval or rejection metadata.
    """

    requires_dosage_label: bool = attrs.field(
        default=None,
    )
    """
    Whether the order requires attaching a dosage information label when shipped.
    """

    _attrs_config = {
        "AmazonOrderId": ["amazon_order_id", "string"],
        "RegulatedInformation": ["regulated_information", "object"],
        "RegulatedOrderVerificationStatus": ["regulated_order_verification_status", "object"],
        "RequiresDosageLabel": ["requires_dosage_label", "boolean"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class RegulatedOrderVerificationStatus(BaseObject):
    """
    The verification status of the order along with associated approval or rejection metadata.
    """

    external_reviewer_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The identifier for the order's regulated information reviewer.
    """

    rejection_reason: Optional["RejectionReason"] = attrs.field(
        default=None,
    )
    """
    The reason for rejecting the order's regulated information. Not present if the order isn't rejected.
    """

    requires_merchant_action: bool = attrs.field(
        default=None,
    )
    """
    Whether the regulated information provided in the order requires a review by the merchant.
    """

    review_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The date the order was reviewed. In ISO 8601 date time format.
    """

    status: Union[
        Literal["Pending"], Literal["Approved"], Literal["Rejected"], Literal["Expired"], Literal["Cancelled"]
    ] = attrs.field(
        default=None,
    )
    """
    The verification status of the order.
    """

    valid_rejection_reasons: List["RejectionReason"] = attrs.field(
        default=None,
    )
    """
    A list of valid rejection reasons that may be used to reject the order's regulated information.
    """

    _attrs_config = {
        "ExternalReviewerId": ["external_reviewer_id", "string"],
        "RejectionReason": ["rejection_reason", "object"],
        "RequiresMerchantAction": ["requires_merchant_action", "boolean"],
        "ReviewDate": ["review_date", "string"],
        "Status": ["status", "string"],
        "ValidRejectionReasons": ["valid_rejection_reasons", "array"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class RejectionReason(BaseObject):
    """
    The reason for rejecting the order's regulated information. Not present if the order isn't rejected.
    """

    rejection_reason_description: str = attrs.field(
        default=None,
    )
    """
    The human-readable description of this rejection reason.
    """

    rejection_reason_id: str = attrs.field(
        default=None,
    )
    """
    The unique identifier for the rejection reason.
    """

    _attrs_config = {
        "RejectionReasonDescription": ["rejection_reason_description", "string"],
        "RejectionReasonId": ["rejection_reason_id", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class RegulatedInformation(BaseObject):
    """
    The regulated information collected during purchase and used to verify the order.
    """

    fields: List["RegulatedInformationField"] = attrs.field(
        default=None,
    )
    """
    A list of regulated information fields as collected from the regulatory form.
    """

    _attrs_config = {"Fields": ["fields", "array"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class RegulatedInformationField(BaseObject):
    """
    A field collected from the regulatory form.
    """

    field_id: str = attrs.field(
        default=None,
    )
    """
    The unique identifier for the field.
    """

    field_label: str = attrs.field(
        default=None,
    )
    """
    The human-readable name for the field.
    """

    field_type: Union[Literal["Text"], Literal["FileAttachment"]] = attrs.field(
        default=None,
    )
    """
    The type of field the field.
    """

    field_value: str = attrs.field(
        default=None,
    )
    """
    The content of the field as collected in regulatory form. Note that FileAttachment type fields will contain an URL
    to download the attachment here.
    """

    _attrs_config = {
        "FieldId": ["field_id", "string"],
        "FieldLabel": ["field_label", "string"],
        "FieldType": ["field_type", "string"],
        "FieldValue": ["field_value", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderAddress(BaseObject):
    """
    The shipping address for the order.
    """

    amazon_order_id: str = attrs.field(
        default=None,
    )
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    shipping_address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    The shipping address for the order.
    """

    _attrs_config = {"AmazonOrderId": ["amazon_order_id", "string"], "ShippingAddress": ["shipping_address", "object"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address(BaseObject):
    """
    The shipping address for the order.
    """

    address_line1: Optional[str] = attrs.field(
        default=None,
    )
    """
    The street address.
    """

    address_line2: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional street address information, if required.
    """

    address_line3: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional street address information, if required.
    """

    address_type: Optional[Union[Literal["Residential"], Literal["Commercial"]]] = attrs.field(
        default=None,
    )
    """
    The address type of the shipping address.
    """

    city: Optional[str] = attrs.field(
        default=None,
    )
    """
    The city
    """

    country_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The country code. A two-character country code, in ISO 3166-1 alpha-2 format.
    """

    county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The county.
    """

    district: Optional[str] = attrs.field(
        default=None,
    )
    """
    The district.
    """

    municipality: Optional[str] = attrs.field(
        default=None,
    )
    """
    The municipality.
    """

    name: str = attrs.field(
        default=None,
    )
    """
    The name.
    """

    phone: Optional[str] = attrs.field(
        default=None,
    )
    """
    The phone number. Not returned for Fulfillment by Amazon (FBA) orders.
    """

    postal_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The postal code.
    """

    state_or_region: Optional[str] = attrs.field(
        default=None,
    )
    """
    The state or region.
    """

    _attrs_config = {
        "AddressLine1": ["address_line1", "string"],
        "AddressLine2": ["address_line2", "string"],
        "AddressLine3": ["address_line3", "string"],
        "AddressType": ["address_type", "string"],
        "City": ["city", "string"],
        "CountryCode": ["country_code", "string"],
        "County": ["county", "string"],
        "District": ["district", "string"],
        "Municipality": ["municipality", "string"],
        "Name": ["name", "string"],
        "Phone": ["phone", "string"],
        "PostalCode": ["postal_code", "string"],
        "StateOrRegion": ["state_or_region", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money(BaseObject):
    """
    The monetary value of the order.
    """

    amount: Optional[str] = attrs.field(
        default=None,
    )
    """
    The currency amount.
    """

    currency_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The three-digit currency code. In ISO 4217 format.
    """

    _attrs_config = {"Amount": ["amount", "string"], "CurrencyCode": ["currency_code", "string"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class PaymentExecutionDetailItem(BaseObject):
    """
    Information about a sub-payment method used to pay for a COD order.
    """

    payment: "Money" = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    payment_method: str = attrs.field(
        default=None,
    )
    """
    A sub-payment method for a COD order.
    Possible values:
    * COD - Cash On Delivery.
    * GC - Gift Card.
    * PointsAccount - Amazon Points.
    """

    _attrs_config = {"Payment": ["payment", "object"], "PaymentMethod": ["payment_method", "string"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyerTaxInfo(BaseObject):
    """
    Tax information about the buyer.
    """

    company_legal_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The legal name of the company.
    """

    tax_classifications: Optional[List["TaxClassification"]] = attrs.field(
        default=None,
    )
    """
    A list of tax classifications that apply to the order.
    """

    taxing_region: Optional[str] = attrs.field(
        default=None,
    )
    """
    The country or region imposing the tax.
    """

    _attrs_config = {
        "CompanyLegalName": ["company_legal_name", "string"],
        "TaxClassifications": ["tax_classifications", "array"],
        "TaxingRegion": ["taxing_region", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class MarketplaceTaxInfo(BaseObject):
    """
    Tax information about the marketplace.
    """

    tax_classifications: Optional[List["TaxClassification"]] = attrs.field(
        default=None,
    )
    """
    A list of tax classifications that apply to the order.
    """

    _attrs_config = {"TaxClassifications": ["tax_classifications", "array"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxClassification(BaseObject):
    """
    The tax classification for the order.
    """

    name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The type of tax.
    """

    value: Optional[str] = attrs.field(
        default=None,
    )
    """
    The buyer's tax identifier.
    """

    _attrs_config = {"Name": ["name", "string"], "Value": ["value", "string"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemsList(BaseObject):
    """
    The order items list along with the order ID.
    """

    amazon_order_id: str = attrs.field(
        default=None,
    )
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    next_token: Optional[str] = attrs.field(
        default=None,
    )
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """

    order_items: List["OrderItem"] = attrs.field(
        default=None,
    )
    """
    A list of order items.
    """

    _attrs_config = {
        "AmazonOrderId": ["amazon_order_id", "string"],
        "NextToken": ["next_token", "string"],
        "OrderItems": ["order_items", "array"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItem(BaseObject):
    """
    A single order item.
    """

    asin: str = attrs.field(
        default=None,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    buyer_info: Optional["ItemBuyerInfo"] = attrs.field(
        default=None,
    )
    """
    A single item's buyer information.
    """

    buyer_requested_cancel: Optional["BuyerRequestedCancel"] = attrs.field(
        default=None,
    )
    """
    Information about whether or not a buyer requested cancellation.
    """

    codfee: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    codfee_discount: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    condition_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The condition of the item.
    Possible values: New, Used, Collectible, Refurbished, Preorder, Club.
    """

    condition_note: Optional[str] = attrs.field(
        default=None,
    )
    """
    The condition of the item as described by the seller.
    """

    condition_subtype_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The subcondition of the item.
    Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty,
    Refurbished, Open Box, Any, Other.
    """

    deemed_reseller_category: Optional[Union[Literal["IOSS"], Literal["UOSS"]]] = attrs.field(
        default=None,
    )
    """
    The category of deemed reseller. This applies to selling partners that are not based in the EU and is used to help
    them meet the VAT Deemed Reseller tax laws in the EU and UK.
    """

    ioss_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The IOSS number for the marketplace. Sellers shipping to the European Union (EU) from outside of the EU must provide
    this IOSS number to their carrier when Amazon has collected the VAT on the sale.
    """

    is_gift: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the item is a gift.
    """

    is_transparency: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, transparency codes are required.
    """

    item_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    item_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    order_item_id: str = attrs.field(
        default=None,
    )
    """
    An Amazon-defined order item identifier.
    """

    points_granted: Optional["PointsGrantedDetail"] = attrs.field(
        default=None,
    )
    """
    The number of Amazon Points offered with the purchase of an item, and their monetary value.
    """

    price_designation: Optional[str] = attrs.field(
        default=None,
    )
    """
    Indicates that the selling price is a special price that is available only for Amazon Business orders. For more
    information about the Amazon Business Seller Program, see the [Amazon Business
    website](https://www.amazon.com/b2b/info/amazon-business).
    Possible values: BusinessPrice - A special price that is available only for Amazon Business orders.
    """

    product_info: Optional["ProductInfoDetail"] = attrs.field(
        default=None,
    )
    """
    Product information on the number of items.
    """

    promotion_discount: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    promotion_discount_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    promotion_ids: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    A list of promotion identifiers provided by the seller when the promotions were created.
    """

    quantity_ordered: int = attrs.field(
        default=None,
    )
    """
    The number of items in the order.
    """

    quantity_shipped: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of items shipped.
    """

    scheduled_delivery_end_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The end date of the scheduled delivery window in the time zone of the order destination. In ISO 8601 date time
    format.
    """

    scheduled_delivery_start_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The start date of the scheduled delivery window in the time zone of the order destination. In ISO 8601 date time
    format.
    """

    seller_sku: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """

    serial_number_required: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the product type for this item has a serial number.
    Returned only for Amazon Easy Ship orders.
    """

    shipping_discount: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    shipping_discount_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    shipping_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    shipping_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    store_chain_store_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The store chain store identifier. Linked to a specific store in a store chain.
    """

    tax_collection: Optional["TaxCollection"] = attrs.field(
        default=None,
    )
    """
    Information about withheld taxes.
    """

    title: Optional[str] = attrs.field(
        default=None,
    )
    """
    The name of the item.
    """

    _attrs_config = {
        "ASIN": ["asin", "string"],
        "BuyerInfo": ["buyer_info", "object"],
        "BuyerRequestedCancel": ["buyer_requested_cancel", "object"],
        "CODFee": ["codfee", "object"],
        "CODFeeDiscount": ["codfee_discount", "object"],
        "ConditionId": ["condition_id", "string"],
        "ConditionNote": ["condition_note", "string"],
        "ConditionSubtypeId": ["condition_subtype_id", "string"],
        "DeemedResellerCategory": ["deemed_reseller_category", "string"],
        "IossNumber": ["ioss_number", "string"],
        "IsGift": ["is_gift", "boolean"],
        "IsTransparency": ["is_transparency", "boolean"],
        "ItemPrice": ["item_price", "object"],
        "ItemTax": ["item_tax", "object"],
        "OrderItemId": ["order_item_id", "string"],
        "PointsGranted": ["points_granted", "object"],
        "PriceDesignation": ["price_designation", "string"],
        "ProductInfo": ["product_info", "object"],
        "PromotionDiscount": ["promotion_discount", "object"],
        "PromotionDiscountTax": ["promotion_discount_tax", "object"],
        "PromotionIds": ["promotion_ids", "array"],
        "QuantityOrdered": ["quantity_ordered", "integer"],
        "QuantityShipped": ["quantity_shipped", "integer"],
        "ScheduledDeliveryEndDate": ["scheduled_delivery_end_date", "string"],
        "ScheduledDeliveryStartDate": ["scheduled_delivery_start_date", "string"],
        "SellerSKU": ["seller_sku", "string"],
        "SerialNumberRequired": ["serial_number_required", "boolean"],
        "ShippingDiscount": ["shipping_discount", "object"],
        "ShippingDiscountTax": ["shipping_discount_tax", "object"],
        "ShippingPrice": ["shipping_price", "object"],
        "ShippingTax": ["shipping_tax", "object"],
        "StoreChainStoreId": ["store_chain_store_id", "string"],
        "TaxCollection": ["tax_collection", "object"],
        "Title": ["title", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemsBuyerInfoList(BaseObject):
    """
    A single order item's buyer information list with the order ID.
    """

    amazon_order_id: str = attrs.field(
        default=None,
    )
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    next_token: Optional[str] = attrs.field(
        default=None,
    )
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """

    order_items: List["OrderItemBuyerInfo"] = attrs.field(
        default=None,
    )
    """
    A single order item's buyer information list.
    """

    _attrs_config = {
        "AmazonOrderId": ["amazon_order_id", "string"],
        "NextToken": ["next_token", "string"],
        "OrderItems": ["order_items", "array"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemBuyerInfo(BaseObject):
    """
    A single order item's buyer information.
    """

    buyer_customized_info: Optional["BuyerCustomizedInfoDetail"] = attrs.field(
        default=None,
    )
    """
    Buyer information for custom orders from the Amazon Custom program.
    """

    gift_message_text: Optional[str] = attrs.field(
        default=None,
    )
    """
    A gift message provided by the buyer.
    """

    gift_wrap_level: Optional[str] = attrs.field(
        default=None,
    )
    """
    The gift wrap level specified by the buyer.
    """

    gift_wrap_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    gift_wrap_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    order_item_id: str = attrs.field(
        default=None,
    )
    """
    An Amazon-defined order item identifier.
    """

    _attrs_config = {
        "BuyerCustomizedInfo": ["buyer_customized_info", "object"],
        "GiftMessageText": ["gift_message_text", "string"],
        "GiftWrapLevel": ["gift_wrap_level", "string"],
        "GiftWrapPrice": ["gift_wrap_price", "object"],
        "GiftWrapTax": ["gift_wrap_tax", "object"],
        "OrderItemId": ["order_item_id", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class PointsGrantedDetail(BaseObject):
    """
    The number of Amazon Points offered with the purchase of an item, and their monetary value.
    """

    points_monetary_value: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    points_number: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of Amazon Points granted with the purchase of an item.
    """

    _attrs_config = {
        "PointsMonetaryValue": ["points_monetary_value", "object"],
        "PointsNumber": ["points_number", "integer"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProductInfoDetail(BaseObject):
    """
    Product information on the number of items.
    """

    number_of_items: Optional[int] = attrs.field(
        default=None,
    )
    """
    The total number of items that are included in the ASIN.
    """

    _attrs_config = {"NumberOfItems": ["number_of_items", "integer"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyerCustomizedInfoDetail(BaseObject):
    """
    Buyer information for custom orders from the Amazon Custom program.
    """

    customized_url: Optional[str] = attrs.field(
        default=None,
    )
    """
    The location of a zip file containing Amazon Custom data.
    """

    _attrs_config = {"CustomizedURL": ["customized_url", "string"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxCollection(BaseObject):
    """
    Information about withheld taxes.
    """

    model: Optional[Union[Literal["MarketplaceFacilitator"]]] = attrs.field(
        default=None,
    )
    """
    The tax collection model applied to the item.
    """

    responsible_party: Optional[Union[Literal["Amazon Services, Inc."]]] = attrs.field(
        default=None,
    )
    """
    The party responsible for withholding the taxes and remitting them to the taxing authority.
    """

    _attrs_config = {"Model": ["model", "string"], "ResponsibleParty": ["responsible_party", "string"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyerTaxInformation(BaseObject):
    """
    Contains the business invoice tax information. Available only in the TR marketplace.
    """

    buyer_business_address: Optional[str] = attrs.field(
        default=None,
    )
    """
    Business buyer's address.
    """

    buyer_legal_company_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    Business buyer's company legal name.
    """

    buyer_tax_office: Optional[str] = attrs.field(
        default=None,
    )
    """
    Business buyer's tax office.
    """

    buyer_tax_registration_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    Business buyer's tax registration ID.
    """

    _attrs_config = {
        "BuyerBusinessAddress": ["buyer_business_address", "string"],
        "BuyerLegalCompanyName": ["buyer_legal_company_name", "string"],
        "BuyerTaxOffice": ["buyer_tax_office", "string"],
        "BuyerTaxRegistrationId": ["buyer_tax_registration_id", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentInstruction(BaseObject):
    """
    Contains the instructions about the fulfillment like where should it be fulfilled from.
    """

    fulfillment_supply_source_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    Denotes the recommended sourceId where the order should be fulfilled from.
    """

    _attrs_config = {"FulfillmentSupplySourceId": ["fulfillment_supply_source_id", "string"]}


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyerInfo(BaseObject):
    """
    Buyer information
    """

    buyer_county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The county of the buyer.
    """

    buyer_email: Optional[str] = attrs.field(
        default=None,
    )
    """
    The anonymized email address of the buyer.
    """

    buyer_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The name of the buyer.
    """

    buyer_tax_info: Optional["BuyerTaxInfo"] = attrs.field(
        default=None,
    )
    """
    Tax information about the buyer.
    """

    purchase_order_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The purchase order (PO) number entered by the buyer at checkout. Returned only for orders where the buyer entered a
    PO number at checkout.
    """

    _attrs_config = {
        "BuyerCounty": ["buyer_county", "string"],
        "BuyerEmail": ["buyer_email", "string"],
        "BuyerName": ["buyer_name", "string"],
        "BuyerTaxInfo": ["buyer_tax_info", "object"],
        "PurchaseOrderNumber": ["purchase_order_number", "string"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemBuyerInfo(BaseObject):
    """
    A single item's buyer information.
    """

    buyer_customized_info: Optional["BuyerCustomizedInfoDetail"] = attrs.field(
        default=None,
    )
    """
    Buyer information for custom orders from the Amazon Custom program.
    """

    gift_message_text: Optional[str] = attrs.field(
        default=None,
    )
    """
    A gift message provided by the buyer.
    """

    gift_wrap_level: Optional[str] = attrs.field(
        default=None,
    )
    """
    The gift wrap level specified by the buyer.
    """

    gift_wrap_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    gift_wrap_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The monetary value of the order.
    """

    _attrs_config = {
        "BuyerCustomizedInfo": ["buyer_customized_info", "object"],
        "GiftMessageText": ["gift_message_text", "string"],
        "GiftWrapLevel": ["gift_wrap_level", "string"],
        "GiftWrapPrice": ["gift_wrap_price", "object"],
        "GiftWrapTax": ["gift_wrap_tax", "object"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class AutomatedShippingSettings(BaseObject):
    """
    Contains information regarding the Shipping Settings Automation program, such as whether the order's shipping
    settings were generated automatically, and what those settings are.
    """

    automated_carrier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Auto-generated carrier for SSA orders.
    """

    automated_ship_method: Optional[str] = attrs.field(
        default=None,
    )
    """
    Auto-generated ship method for SSA orders.
    """

    has_automated_shipping_settings: Optional[bool] = attrs.field(
        default=None,
    )
    """
    If true, this order has automated shipping settings generated by Amazon. This order could be identified as an SSA
    order.
    """

    _attrs_config = {
        "AutomatedCarrier": ["automated_carrier", "string"],
        "AutomatedShipMethod": ["automated_ship_method", "string"],
        "HasAutomatedShippingSettings": ["has_automated_shipping_settings", "boolean"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyerRequestedCancel(BaseObject):
    """
    Information about whether or not a buyer requested cancellation.
    """

    buyer_cancel_reason: Optional[str] = attrs.field(
        default=None,
    )
    """
    Reason for buyer requesting cancel
    """

    is_buyer_requested_cancel: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the buyer has requested cancellation.
    """

    _attrs_config = {
        "BuyerCancelReason": ["buyer_cancel_reason", "string"],
        "IsBuyerRequestedCancel": ["is_buyer_requested_cancel", "boolean"],
    }


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error(BaseObject):
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field(
        default=None,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        default=None,
    )
    """
    A message that describes the error condition in a human-readable form.
    """

    _attrs_config = {"code": ["code", "string"], "details": ["details", "string"], "message": ["message", "string"]}


class OrdersV0Client(BaseClient):
    def get_order(
        self,
        order_id: str,
    ) -> Union["GetOrderResponse"]:
        """
        Returns the order indicated by the specified order ID.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested
        operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table
        above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
        """
        url = "/orders/v0/orders/{orderId}"
        values = (order_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_order_params,
            self._get_order_responses,
        )
        return response

    _get_order_params = (("orderId", "path"),)  # name, param in

    _get_order_responses = {
        200: "GetOrderResponse",
        400: "GetOrderResponse",
        403: "GetOrderResponse",
        404: "GetOrderResponse",
        429: "GetOrderResponse",
        500: "GetOrderResponse",
        503: "GetOrderResponse",
    }

    def get_order_address(
        self,
        order_id: str,
    ) -> Union["GetOrderAddressResponse"]:
        """
        Returns the shipping address for the specified order.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested
        operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table
        above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format.
        """
        url = "/orders/v0/orders/{orderId}/address"
        values = (order_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_order_address_params,
            self._get_order_address_responses,
        )
        return response

    _get_order_address_params = (("orderId", "path"),)  # name, param in

    _get_order_address_responses = {
        200: "GetOrderAddressResponse",
        400: "GetOrderAddressResponse",
        403: "GetOrderAddressResponse",
        404: "GetOrderAddressResponse",
        429: "GetOrderAddressResponse",
        500: "GetOrderAddressResponse",
        503: "GetOrderAddressResponse",
    }

    def get_order_buyer_info(
        self,
        order_id: str,
    ) -> Union["GetOrderBuyerInfoResponse"]:
        """
        Returns buyer information for the specified order.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested
        operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table
        above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format.
        """
        url = "/orders/v0/orders/{orderId}/buyerInfo"
        values = (order_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_order_buyer_info_params,
            self._get_order_buyer_info_responses,
        )
        return response

    _get_order_buyer_info_params = (("orderId", "path"),)  # name, param in

    _get_order_buyer_info_responses = {
        200: "GetOrderBuyerInfoResponse",
        400: "GetOrderBuyerInfoResponse",
        403: "GetOrderBuyerInfoResponse",
        404: "GetOrderBuyerInfoResponse",
        429: "GetOrderBuyerInfoResponse",
        500: "GetOrderBuyerInfoResponse",
        503: "GetOrderBuyerInfoResponse",
    }

    def get_order_items(
        self,
        order_id: str,
        next_token: str = None,
    ) -> Union["GetOrderItemsResponse"]:
        """
        Returns detailed order item information for the order indicated by the specified order ID. If NextToken is
        provided, it's used to retrieve the next page of order items.
        Note: When an order is in the Pending state (the order has been placed but payment has not been authorized), the
        getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or
        promotions for the order items in the order. After an order leaves the Pending state (this occurs when payment
        has been authorized) and enters the Unshipped, Partially Shipped, or Shipped state, the getOrderItems operation
        returns information about pricing, taxes, shipping charges, gift status and promotions for the order items in
        the order.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested
        operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table
        above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
            next_token: A string token returned in the response of your previous request.
        """
        url = "/orders/v0/orders/{orderId}/orderItems"
        values = (
            order_id,
            next_token,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_order_items_params,
            self._get_order_items_responses,
        )
        return response

    _get_order_items_params = (  # name, param in
        ("orderId", "path"),
        ("NextToken", "query"),
    )

    _get_order_items_responses = {
        200: "GetOrderItemsResponse",
        400: "GetOrderItemsResponse",
        403: "GetOrderItemsResponse",
        404: "GetOrderItemsResponse",
        429: "GetOrderItemsResponse",
        500: "GetOrderItemsResponse",
        503: "GetOrderItemsResponse",
    }

    def get_order_items_buyer_info(
        self,
        order_id: str,
        next_token: str = None,
    ) -> Union["GetOrderItemsBuyerInfoResponse"]:
        """
        Returns buyer information for the order items in the specified order.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested
        operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table
        above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
            next_token: A string token returned in the response of your previous request.
        """
        url = "/orders/v0/orders/{orderId}/orderItems/buyerInfo"
        values = (
            order_id,
            next_token,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_order_items_buyer_info_params,
            self._get_order_items_buyer_info_responses,
        )
        return response

    _get_order_items_buyer_info_params = (  # name, param in
        ("orderId", "path"),
        ("NextToken", "query"),
    )

    _get_order_items_buyer_info_responses = {
        200: "GetOrderItemsBuyerInfoResponse",
        400: "GetOrderItemsBuyerInfoResponse",
        403: "GetOrderItemsBuyerInfoResponse",
        404: "GetOrderItemsBuyerInfoResponse",
        429: "GetOrderItemsBuyerInfoResponse",
        500: "GetOrderItemsBuyerInfoResponse",
        503: "GetOrderItemsBuyerInfoResponse",
    }

    def get_order_regulated_info(
        self,
        order_id: str,
    ) -> Union["GetOrderRegulatedInfoResponse"]:
        """
        Returns regulated information for the order indicated by the specified order ID.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested
        operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table
        above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format.
        """
        url = "/orders/v0/orders/{orderId}/regulatedInfo"
        values = (order_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_order_regulated_info_params,
            self._get_order_regulated_info_responses,
        )
        return response

    _get_order_regulated_info_params = (("orderId", "path"),)  # name, param in

    _get_order_regulated_info_responses = {
        200: "GetOrderRegulatedInfoResponse",
        400: "GetOrderRegulatedInfoResponse",
        403: "GetOrderRegulatedInfoResponse",
        404: "GetOrderRegulatedInfoResponse",
        429: "GetOrderRegulatedInfoResponse",
        500: "GetOrderRegulatedInfoResponse",
        503: "GetOrderRegulatedInfoResponse",
    }

    def get_orders(
        self,
        marketplace_ids: List[str],
        created_after: str = None,
        created_before: str = None,
        last_updated_after: str = None,
        last_updated_before: str = None,
        order_statuses: List[str] = None,
        fulfillment_channels: List[str] = None,
        payment_methods: List[str] = None,
        buyer_email: str = None,
        seller_order_id: str = None,
        max_results_per_page: int = None,
        easy_ship_shipment_statuses: List[str] = None,
        next_token: str = None,
        amazon_order_ids: List[str] = None,
        actual_fulfillment_supply_source_id: str = None,
        is_ispu: bool = None,
        store_chain_store_id: str = None,
    ) -> Union["GetOrdersResponse"]:
        """
        Returns orders created or updated during the time frame indicated by the specified parameters. You can also
        apply a range of filtering criteria to narrow the list of orders returned. If NextToken is present, that will be
        used to retrieve the orders instead of other criteria.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested
        operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table
        above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            created_after: A date used for selecting orders created after (or at) a specified time. Only orders placed
                after the specified time are returned. Either the CreatedAfter parameter or the LastUpdatedAfter
                parameter is required. Both cannot be empty. The date must be in ISO 8601 format.
            created_before: A date used for selecting orders created before (or at) a specified time. Only orders placed
                before the specified time are returned. The date must be in ISO 8601 format.
            last_updated_after: A date used for selecting orders that were last updated after (or at) a specified time.
                An update is defined as any change in order status, including the creation of a new order. Includes
                updates made by Amazon and by the seller. The date must be in ISO 8601 format.
            last_updated_before: A date used for selecting orders that were last updated before (or at) a specified
                time. An update is defined as any change in order status, including the creation of a new order.
                Includes updates made by Amazon and by the seller. The date must be in ISO 8601 format.
            order_statuses: A list of OrderStatus values used to filter the results. Possible values:
                PendingAvailability (This status is available for pre-orders only. The order has been placed, payment
                has not been authorized, and the release date of the item is in the future.); Pending (The order has
                been placed but payment has not been authorized); Unshipped (Payment has been authorized and the order
                is ready for shipment, but no items in the order have been shipped); PartiallyShipped (One or more, but
                not all, items in the order have been shipped); Shipped (All items in the order have been shipped);
                InvoiceUnconfirmed (All items in the order have been shipped. The seller has not yet given confirmation
                to Amazon that the invoice has been shipped to the buyer.); Canceled (The order has been canceled); and
                Unfulfillable (The order cannot be fulfilled. This state applies only to Multi-Channel Fulfillment
                orders.).
            marketplace_ids: A list of MarketplaceId values. Used to select orders that were placed in the specified
                marketplaces.
            See the [Selling Partner API Developer Guide](doc:marketplace-ids) for a complete list of marketplaceId
                values.
            fulfillment_channels: A list that indicates how an order was fulfilled. Filters the results by fulfillment
                channel. Possible values: AFN (Fulfillment by Amazon); MFN (Fulfilled by the seller).
            payment_methods: A list of payment method values. Used to select orders paid using the specified payment
                methods. Possible values: COD (Cash on delivery); CVS (Convenience store payment); Other (Any payment
                method other than COD or CVS).
            buyer_email: The email address of a buyer. Used to select orders that contain the specified email address.
            seller_order_id: An order identifier that is specified by the seller. Used to select only the orders that
                match the order identifier. If SellerOrderId is specified, then FulfillmentChannels, OrderStatuses,
                PaymentMethod, LastUpdatedAfter, LastUpdatedBefore, and BuyerEmail cannot be specified.
            max_results_per_page: A number that indicates the maximum number of orders that can be returned per page.
                Value must be 1 - 100. Default 100.
            easy_ship_shipment_statuses: A list of EasyShipShipmentStatus values. Used to select Easy Ship orders with
                statuses that match the specified  values. If EasyShipShipmentStatus is specified, only Amazon Easy Ship
                orders are returned.Possible values: PendingPickUp (Amazon has not yet picked up the package from the
                seller). LabelCanceled (The seller canceled the pickup). PickedUp (Amazon has picked up the package from
                the seller). AtOriginFC (The packaged is at the origin fulfillment center). AtDestinationFC (The package
                is at the destination fulfillment center). OutForDelivery (The package is out for delivery). Damaged
                (The package was damaged by the carrier). Delivered (The package has been delivered to the buyer).
                RejectedByBuyer (The package has been rejected by the buyer). Undeliverable (The package cannot be
                delivered). ReturnedToSeller (The package was not delivered to the buyer and was returned to the
                seller). ReturningToSeller (The package was not delivered to the buyer and is being returned to the
                seller).
            next_token: A string token returned in the response of your previous request.
            amazon_order_ids: A list of AmazonOrderId values. An AmazonOrderId is an Amazon-defined order identifier, in
                3-7-7 format.
            actual_fulfillment_supply_source_id: Denotes the recommended sourceId where the order should be fulfilled
                from.
            is_ispu: When true, this order is marked to be picked up from a store rather than delivered.
            store_chain_store_id: The store chain store identifier. Linked to a specific store in a store chain.
        """
        url = "/orders/v0/orders"
        values = (
            created_after,
            created_before,
            last_updated_after,
            last_updated_before,
            order_statuses,
            marketplace_ids,
            fulfillment_channels,
            payment_methods,
            buyer_email,
            seller_order_id,
            max_results_per_page,
            easy_ship_shipment_statuses,
            next_token,
            amazon_order_ids,
            actual_fulfillment_supply_source_id,
            is_ispu,
            store_chain_store_id,
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
        ("CreatedAfter", "query"),
        ("CreatedBefore", "query"),
        ("LastUpdatedAfter", "query"),
        ("LastUpdatedBefore", "query"),
        ("OrderStatuses", "query"),
        ("MarketplaceIds", "query"),
        ("FulfillmentChannels", "query"),
        ("PaymentMethods", "query"),
        ("BuyerEmail", "query"),
        ("SellerOrderId", "query"),
        ("MaxResultsPerPage", "query"),
        ("EasyShipShipmentStatuses", "query"),
        ("NextToken", "query"),
        ("AmazonOrderIds", "query"),
        ("ActualFulfillmentSupplySourceId", "query"),
        ("IsISPU", "query"),
        ("StoreChainStoreId", "query"),
    )

    _get_orders_responses = {
        200: "GetOrdersResponse",
        400: "GetOrdersResponse",
        403: "GetOrdersResponse",
        404: "GetOrdersResponse",
        429: "GetOrdersResponse",
        500: "GetOrdersResponse",
        503: "GetOrdersResponse",
    }

    def update_shipment_status(
        self,
        order_id: str,
        marketplace_id: str,
        shipment_status: Union[Literal["ReadyForPickup"], Literal["PickedUp"], Literal["RefusedPickup"]],
        order_items: List["OrderItemsItem"] = None,
    ) -> Union["UpdateShipmentStatusErrorResponse"]:
        """
        Update the shipment status.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
            marketplace_id: the unobfuscated marketplace ID
            order_items: the list of order items and quantities when the seller wants to partially update the shipment
                status of the order
            shipment_status: the status of the shipment of the order to be updated
        """
        url = "/orders/v0/orders/{orderId}/shipment"
        values = (
            order_id,
            marketplace_id,
            order_items,
            shipment_status,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._update_shipment_status_params,
            self._update_shipment_status_responses,
        )
        return response

    _update_shipment_status_params = (  # name, param in
        ("orderId", "path"),
        ("marketplaceId", "body"),
        ("orderItems", "body"),
        ("shipmentStatus", "body"),
    )

    _update_shipment_status_responses = {
        400: "UpdateShipmentStatusErrorResponse",
        403: "UpdateShipmentStatusErrorResponse",
        404: "UpdateShipmentStatusErrorResponse",
        413: "UpdateShipmentStatusErrorResponse",
        415: "UpdateShipmentStatusErrorResponse",
        429: "UpdateShipmentStatusErrorResponse",
        500: "UpdateShipmentStatusErrorResponse",
        503: "UpdateShipmentStatusErrorResponse",
    }

    def update_verification_status(
        self,
        order_id: str,
        regulated_order_verification_status: "UpdateVerificationStatusRequestBody",
    ) -> Union["UpdateVerificationStatusErrorResponse"]:
        """
        Updates (approves or rejects) the verification status of an order containing regulated products.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested
        operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table
        above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format.
            regulated_order_verification_status: The updated values of the VerificationStatus field.
        """
        url = "/orders/v0/orders/{orderId}/regulatedInfo"
        values = (
            order_id,
            regulated_order_verification_status,
        )
        response = self._parse_args_and_request(
            url,
            "PATCH",
            values,
            self._update_verification_status_params,
            self._update_verification_status_responses,
        )
        return response

    _update_verification_status_params = (  # name, param in
        ("orderId", "path"),
        ("regulatedOrderVerificationStatus", "body"),
    )

    _update_verification_status_responses = {
        400: "UpdateVerificationStatusErrorResponse",
        403: "UpdateVerificationStatusErrorResponse",
        404: "UpdateVerificationStatusErrorResponse",
        413: "UpdateVerificationStatusErrorResponse",
        415: "UpdateVerificationStatusErrorResponse",
        429: "UpdateVerificationStatusErrorResponse",
        500: "UpdateVerificationStatusErrorResponse",
        503: "UpdateVerificationStatusErrorResponse",
    }

    pass
