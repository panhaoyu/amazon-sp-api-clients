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

    address_line1: str = attrs.field(
        kw_only=True,
    )
    """
    First line of the address.
    """

    address_line2: str = attrs.field(
        kw_only=True,
    )
    """
    Additional street address information, if required.
    """

    address_line3: str = attrs.field(
        kw_only=True,
    )
    """
    Additional street address information, if required.
    """

    city: str = attrs.field(
        kw_only=True,
    )
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The two digit country code in ISO 3166-1 alpha-2 format.
    """

    county: str = attrs.field(
        kw_only=True,
    )
    """
    The county where person, business or institution is located.
    """

    district: str = attrs.field(
        kw_only=True,
    )
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the person, business or institution at that address.
    """

    phone: str = attrs.field(
        kw_only=True,
    )
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_code: str = attrs.field(
        kw_only=True,
    )
    """
    The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: str = attrs.field(
        kw_only=True,
    )
    """
    The state or region where person, business or institution is located.
    """

    pass


@attrs.define
class Container:

    carrier: str = attrs.field(
        kw_only=True,
    )
    """
    Carrier required for EU VOC vendors only.
    """

    container_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    The container identifier.
    """

    container_sequence_number: int = attrs.field(
        kw_only=True,
    )
    """
    An integer that must be submitted for multi-box shipments only, where one item may come in separate packages.
    """

    container_type: Union[Literal["carton"], Literal["pallet"]] = attrs.field(
        kw_only=True,
    )
    """
    The type of container.
    """

    manifest_date: str = attrs.field(
        kw_only=True,
    )
    """
    The date of the manifest.
    """

    manifest_id: str = attrs.field(
        kw_only=True,
    )
    """
    The manifest identifier.
    """

    packed_items: list["PackedItem"] = attrs.field(
        kw_only=True,
    )
    """
    A list of packed items.
    """

    scac_code: str = attrs.field(
        kw_only=True,
    )
    """
    SCAC code required for NA VOC vendors only.
    """

    ship_method: str = attrs.field(
        kw_only=True,
    )
    """
    The shipment method.
    """

    tracking_number: str = attrs.field(
        kw_only=True,
    )
    """
    The tracking number.
    """

    dimensions: "Dimensions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CustomerInvoice:

    content: str = attrs.field(
        kw_only=True,
    )
    """
    The Base64encoded customer invoice.
    """

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The purchase order number for this order.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """

    pass


@attrs.define
class CustomerInvoiceList:

    customer_invoices: list["CustomerInvoice"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pagination: "Pagination" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Dimensions:

    unit_of_measure: Union[Literal["IN"], Literal["CM"]] = attrs.field(
        kw_only=True,
    )
    """
    The unit of measure for dimensions.
    """

    height: "Decimal" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    length: "Decimal" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    width: "Decimal" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Error:

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: str = attrs.field(
        kw_only=True,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition.
    """

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetCustomerInvoiceResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "CustomerInvoice" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetCustomerInvoicesResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "CustomerInvoiceList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetPackingSlipListResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "PackingSlipList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetPackingSlipResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "PackingSlip" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetShippingLabelListResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "ShippingLabelList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetShippingLabelResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "ShippingLabel" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Item:

    buyer_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Buyer's Standard Identification Number (ASIN) of an item. Either buyerProductIdentifier or vendorProductIdentifier is required.
    """

    item_sequence_number: int = attrs.field(
        kw_only=True,
    )
    """
    Item Sequence Number for the item. This must be the same value as sent in order for a given item.
    """

    vendor_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor selected product identification of the item. Should be the same as was sent in the purchase order, like SKU Number.
    """

    shipped_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ItemQuantity:

    amount: int = attrs.field(
        kw_only=True,
    )
    """
    Quantity of units shipped for a specific item at a shipment level. If the item is present only in certain packages or pallets within the shipment, please provide this at the appropriate package or pallet level.
    """

    unit_of_measure: str = attrs.field(
        kw_only=True,
    )
    """
    Unit of measure for the shipped quantity.
    """

    pass


@attrs.define
class LabelData:

    content: str = attrs.field(
        kw_only=True,
    )
    """
    This field will contain the Base64encoded string of the shipment label content.
    """

    package_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Identifier for the package. The first package will be 001, the second 002, and so on. This number is used as a reference to refer to this package from the pallet level.
    """

    ship_method: str = attrs.field(
        kw_only=True,
    )
    """
    Ship method to be used for shipping the order. Amazon defines Ship Method Codes indicating shipping carrier and shipment service level. Ship Method Codes are case and format sensitive. The same ship method code should returned on the shipment confirmation. Note that the Ship Method Codes are vendor specific and will be provided to each vendor during the implementation.
    """

    ship_method_name: str = attrs.field(
        kw_only=True,
    )
    """
    Shipping method name for internal reference.
    """

    tracking_number: str = attrs.field(
        kw_only=True,
    )
    """
    Package tracking identifier from the shipping carrier.
    """

    pass


@attrs.define
class PackedItem:

    buyer_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Buyer's Standard Identification Number (ASIN) of an item. Either buyerProductIdentifier or vendorProductIdentifier is required.
    """

    item_sequence_number: int = attrs.field(
        kw_only=True,
    )
    """
    Item Sequence Number for the item. This must be the same value as sent in the order for a given item.
    """

    vendor_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor selected product identification of the item. Should be the same as was sent in the Purchase Order, like SKU Number.
    """

    packed_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PackingSlip:

    content: str = attrs.field(
        kw_only=True,
    )
    """
    A Base64encoded string of the packing slip PDF.
    """

    content_type: Union[Literal["application/pdf"]] = attrs.field(
        kw_only=True,
    )
    """
    The format of the file such as PDF, JPEG etc.
    """

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    Purchase order number of the shipment that the packing slip is for.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """

    pass


@attrs.define
class PackingSlipList:

    packing_slips: list["PackingSlip"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pagination: "Pagination" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Pagination:

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.
    """

    pass


@attrs.define
class PartyIdentification:

    party_id: str = attrs.field(
        kw_only=True,
    )
    """
    Assigned Identification for the party.
    """

    tax_registration_details: list["TaxRegistrationDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Tax registration details of the entity.
    """

    address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentConfirmation:

    containers: list["Container"] = attrs.field(
        kw_only=True,
    )
    """
    Provide the details of the items in this shipment. If any of the item details field is common at a package or a pallet level, then provide them at the corresponding package.
    """

    items: list["Item"] = attrs.field(
        kw_only=True,
    )
    """
    Provide the details of the items in this shipment. If any of the item details field is common at a package or a pallet level, then provide them at the corresponding package.
    """

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    Purchase order number corresponding to the shipment.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """

    selling_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_details: "ShipmentDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentDetails:

    estimated_delivery_date: str = attrs.field(
        kw_only=True,
    )
    """
    Date on which the shipment is expected to reach the buyer's warehouse. It needs to be an estimate based on the average transit time between the ship-from location and the destination. The exact appointment time will be provided by buyer and is potentially not known when creating the shipment confirmation.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    is_priority_shipment: bool = attrs.field(
        kw_only=True,
    )
    """
    Provide the priority of the shipment.
    """

    shipment_status: Union[Literal["SHIPPED"], Literal["FLOOR_DENIAL"]] = attrs.field(
        kw_only=True,
    )
    """
    Indicate the shipment status.
    """

    shipped_date: str = attrs.field(
        kw_only=True,
    )
    """
    This field indicates the date of the departure of the shipment from vendor's location. Vendors are requested to send ASNs within 30 minutes of departure from their warehouse/distribution center or at least 6 hours prior to the appointment time at the Amazon destination warehouse, whichever is sooner. Shipped date mentioned in the Shipment Confirmation should not be in the future.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    vendor_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor order number is a unique identifier generated by a vendor for their reference.
    """

    pass


@attrs.define
class ShipmentStatusUpdate:

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    Purchase order number of the shipment for which to update the shipment status.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """

    selling_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    status_update_details: "StatusUpdateDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShippingLabel:

    label_data: list["LabelData"] = attrs.field(
        kw_only=True,
    )
    """
    Provides the details of the packages in this shipment.
    """

    label_format: Union[Literal["PNG"], Literal["ZPL"]] = attrs.field(
        kw_only=True,
    )
    """
    Format of the label.
    """

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    This field will contain the Purchase Order Number for this order.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """

    selling_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShippingLabelList:

    shipping_labels: list["ShippingLabel"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pagination: "Pagination" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShippingLabelRequest:

    containers: list["Container"] = attrs.field(
        kw_only=True,
    )
    """
    A list of the packages in this shipment.
    """

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    Purchase order number of the order for which to create a shipping label.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """

    selling_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StatusUpdateDetails:

    reason_code: str = attrs.field(
        kw_only=True,
    )
    """
    Provides a reason code for the status of the package that will provide additional information about the transportation status.
    """

    shipment_schedule: dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'properties': {'estimatedDeliveryDateTime': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='Date on which the shipment is expected to reach the customer delivery location. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.', schema_format='date-time', default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'apptWindowStartDateTime': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='This field indicates the date and time at the start of the appointment window scheduled to deliver the shipment. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.', schema_format='date-time', default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'apptWindowEndDateTime': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='This field indicates the date and time at the end of the appointment window scheduled to deliver the shipment. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.', schema_format='date-time', default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}}
    """

    status_code: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates the shipment status code of the package that provides transportation information for Amazon tracking systems and ultimately for the final customer.
    """

    status_date_time: str = attrs.field(
        kw_only=True,
    )
    """
    The date and time when the shipment status was updated. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    tracking_number: str = attrs.field(
        kw_only=True,
    )
    """
    This is required to be provided for every package and should match with the trackingNumber sent for the shipment confirmation.
    """

    status_location_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SubmitShipmentConfirmationsRequest:

    shipment_confirmations: list["ShipmentConfirmation"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SubmitShipmentConfirmationsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "TransactionReference" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SubmitShipmentStatusUpdatesRequest:

    shipment_status_updates: list["ShipmentStatusUpdate"] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'minItems': 1}
    """

    pass


@attrs.define
class SubmitShipmentStatusUpdatesResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "TransactionReference" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SubmitShippingLabelsRequest:

    shipping_label_requests: list["ShippingLabelRequest"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SubmitShippingLabelsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "TransactionReference" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_messages: str = attrs.field(
        kw_only=True,
    )
    """
    Tax registration message that can be used for additional tax related details.
    """

    tax_registration_number: str = attrs.field(
        kw_only=True,
    )
    """
    Tax registration number for the party. For example, VAT ID.
    """

    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field(
        kw_only=True,
    )
    """
    Tax registration type for the entity.
    """

    tax_registration_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TransactionReference:

    transaction_id: str = attrs.field(
        kw_only=True,
    )
    """
    GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """

    pass


@attrs.define
class Weight:

    unit_of_measure: Union[Literal["KG"], Literal["LB"]] = attrs.field(
        kw_only=True,
    )
    """
    The unit of measurement.
    """

    value: "Decimal" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

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
        shipment_confirmations: list["ShipmentConfirmation"] = None,
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
            shipment_confirmations: no description.
        """
        url = "/vendor/directFulfillment/shipping/v1/shipmentConfirmations"
        values = (shipment_confirmations,)
        response = self._parse_args_and_request(url, "POST", values, self._submit_shipment_confirmations_params)
        return response

    _submit_shipment_confirmations_params = (("shipmentConfirmations", "body"),)  # name, param in

    def submit_shipment_status_updates(
        self,
        shipment_status_updates: list["ShipmentStatusUpdate"] = None,
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
            shipment_status_updates: no description.
        """
        url = "/vendor/directFulfillment/shipping/v1/shipmentStatusUpdates"
        values = (shipment_status_updates,)
        response = self._parse_args_and_request(url, "POST", values, self._submit_shipment_status_updates_params)
        return response

    _submit_shipment_status_updates_params = (("shipmentStatusUpdates", "body"),)  # name, param in

    def submit_shipping_label_request(
        self,
        shipping_label_requests: list["ShippingLabelRequest"] = None,
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
            shipping_label_requests: no description.
        """
        url = "/vendor/directFulfillment/shipping/v1/shippingLabels"
        values = (shipping_label_requests,)
        response = self._parse_args_and_request(url, "POST", values, self._submit_shipping_label_request_params)
        return response

    _submit_shipping_label_request_params = (("shippingLabelRequests", "body"),)  # name, param in
