"""
Selling Partner API for Shipment Invoicing
=============================================================================================

The Selling Partner API for Shipment Invoicing helps you programmatically retrieve shipment invoice information in the Brazil marketplace for a selling partner’s Fulfillment by Amazon (FBA) orders.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    The shipping address details of the shipment.
    """

    address_line1: Optional[str] = attrs.field()
    """
    The street address.
    """

    address_line2: Optional[str] = attrs.field()
    """
    Additional street address information, if required.
    """

    address_line3: Optional[str] = attrs.field()
    """
    Additional street address information, if required.
    """

    address_type: Optional["AddressTypeEnum"] = attrs.field()

    city: Optional[str] = attrs.field()
    """
    The city.
    """

    country_code: Optional[str] = attrs.field()
    """
    The country code.
    """

    county: Optional[str] = attrs.field()
    """
    The county.
    """

    district: Optional[str] = attrs.field()
    """
    The district.
    """

    name: Optional[str] = attrs.field()
    """
    The name.
    """

    phone: Optional[str] = attrs.field()
    """
    The phone number.
    """

    postal_code: Optional[str] = attrs.field()
    """
    The postal code.
    """

    state_or_region: Optional[str] = attrs.field()
    """
    The state or region.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressTypeEnum:
    """
    The shipping address type.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Blob:
    """
    Shipment invoice document content.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyerTaxInfo:
    """
    Tax information about the buyer.
    """

    company_legal_name: Optional[str] = attrs.field()
    """
    The legal name of the company.
    """

    tax_classifications: Optional["TaxClassificationList"] = attrs.field()

    taxing_region: Optional[str] = attrs.field()
    """
    The country or region imposing the tax.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    An error response returned when the request is unsuccessful.
    """

    code: Optional[str] = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: Optional[str] = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetInvoiceStatusResponse:
    """
    The response schema for the getInvoiceStatus operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["ShipmentInvoiceStatusResponse"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentDetailsResponse:
    """
    The response schema for the getShipmentDetails operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["ShipmentDetail"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class MarketplaceTaxInfo:
    """
    Tax information about the marketplace.
    """

    company_legal_name: Optional[str] = attrs.field()
    """
    The legal name of the company.
    """

    tax_classifications: Optional["TaxClassificationList"] = attrs.field()

    taxing_region: Optional[str] = attrs.field()
    """
    The country or region imposing the tax.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    The currency type and amount.
    """

    amount: Optional[str] = attrs.field()
    """
    The currency amount.
    """

    currency_code: Optional[str] = attrs.field()
    """
    Three-digit currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PaymentMethodDetailItemList:
    """
    The list of payment method details.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SerialNumbersList:
    """
    The list of serial numbers.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentDetail:
    """
    The information required by a selling partner to issue a shipment invoice.
    """

    amazon_order_id: Optional[str] = attrs.field()
    """
    The Amazon-defined identifier for the order.
    """

    amazon_shipment_id: Optional[str] = attrs.field()
    """
    The Amazon-defined identifier for the shipment.
    """

    buyer_county: Optional[str] = attrs.field()
    """
    The county of the buyer.
    """

    buyer_name: Optional[str] = attrs.field()
    """
    The name of the buyer.
    """

    buyer_tax_info: Optional["BuyerTaxInfo"] = attrs.field()

    marketplace_id: Optional[str] = attrs.field()
    """
    The identifier for the marketplace where the order was placed.
    """

    marketplace_tax_info: Optional["MarketplaceTaxInfo"] = attrs.field()

    payment_method_details: Optional["PaymentMethodDetailItemList"] = attrs.field()

    purchase_date: Optional[datetime] = attrs.field()
    """
    The date and time when the order was created.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    seller_display_name: Optional[str] = attrs.field()
    """
    The seller’s friendly name registered in the marketplace.
    """

    seller_id: Optional[str] = attrs.field()
    """
    The seller identifier.
    """

    shipment_items: Optional["ShipmentItems"] = attrs.field()

    shipping_address: Optional["Address"] = attrs.field()

    warehouse_id: Optional[str] = attrs.field()
    """
    The Amazon-defined identifier for the warehouse.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentInvoiceStatus:
    """
    The shipment invoice status.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentInvoiceStatusInfo:
    """
    The shipment invoice status information.
    """

    amazon_shipment_id: Optional[str] = attrs.field()
    """
    The Amazon-defined shipment identifier.
    """

    invoice_status: Optional["ShipmentInvoiceStatus"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentInvoiceStatusResponse:
    """
    The shipment invoice status response.
    """

    shipments: Optional["ShipmentInvoiceStatusInfo"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentItem:
    """
    The shipment item information required by a seller to issue a shipment invoice.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    gift_wrap_price: Optional["Money"] = attrs.field()

    item_price: Optional["Money"] = attrs.field()

    order_item_id: Optional[str] = attrs.field()
    """
    The Amazon-defined identifier for the order item.
    """

    promotion_discount: Optional["Money"] = attrs.field()

    quantity_ordered: Optional[float] = attrs.field()
    """
    The number of items ordered.
    """

    seller_sku: Optional[str] = attrs.field()
    """
    The seller SKU of the item.
    """

    serial_numbers: Optional["SerialNumbersList"] = attrs.field()

    shipping_discount: Optional["Money"] = attrs.field()

    shipping_price: Optional["Money"] = attrs.field()

    title: Optional[str] = attrs.field()
    """
    The name of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentItems:
    """
    A list of shipment items.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoiceRequest:
    """
    The request schema for the submitInvoice operation.
    """

    content_md5value: Optional[str] = attrs.field()
    """
    MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).
    """

    invoice_content: Optional["Blob"] = attrs.field()

    marketplace_id: Optional[str] = attrs.field()
    """
    An Amazon marketplace identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoiceResponse:
    """
    The response schema for the submitInvoice operation.
    """

    errors: Optional["ErrorList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxClassification:
    """
    The tax classification for the entity.
    """

    name: Optional[str] = attrs.field()
    """
    The type of tax.
    """

    value: Optional[str] = attrs.field()
    """
    The entity's tax identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxClassificationList:
    """
    The list of tax classifications.
    """

    pass


class ShipmentInvoicingV0Client(BaseClient):
    def get_invoice_status(
        self,
        shipment_id: str,
    ):
        """
        Returns the invoice status for the shipment you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The shipment identifier for the shipment.
        """
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice/status"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_invoice_status_params)
        return response

    _get_invoice_status_params = (("shipmentId", "path"),)  # name, param in

    def get_shipment_details(
        self,
        shipment_id: str,
    ):
        """
        Returns the shipment details required to issue an invoice for the specified shipment.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The identifier for the shipment. Get this value from the FBAOutboundShipmentStatus notification. For information about subscribing to notifications, see the [Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        """
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_shipment_details_params)
        return response

    _get_shipment_details_params = (("shipmentId", "path"),)  # name, param in

    def submit_invoice(
        self,
        shipment_id: str,
        content_md5value: str,
        invoice_content: bytes,
        marketplace_id: str = None,
    ):
        """
        Submits a shipment invoice document for a given shipment.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The identifier for the shipment.
            content_md5value: MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).
            invoice_content: Shipment invoice document content.
            marketplace_id: An Amazon marketplace identifier.
        """
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice"
        values = (
            shipment_id,
            content_md5value,
            invoice_content,
            marketplace_id,
        )
        response = self._parse_args_and_request(url, "POST", values, self._submit_invoice_params)
        return response

    _submit_invoice_params = (  # name, param in
        ("shipmentId", "path"),
        ("ContentMD5Value", "body"),
        ("InvoiceContent", "body"),
        ("MarketplaceId", "body"),
    )
