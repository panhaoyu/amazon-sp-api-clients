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
class PackingSlip:
    pass


@attrs.define
class PackingSlipList:
    pass


@attrs.define
class GetPackingSlipListResponse:
    pass


@attrs.define
class GetPackingSlipResponse:
    pass


@attrs.define
class SubmitShippingLabelsRequest:
    pass


@attrs.define
class ShippingLabelRequest:
    pass


@attrs.define
class Item:
    pass


@attrs.define
class PackedItem:
    pass


@attrs.define
class PartyIdentification:
    pass


@attrs.define
class ShipmentDetails:
    pass


@attrs.define
class StatusUpdateDetails:
    pass


@attrs.define
class TaxRegistrationDetails:
    pass


@attrs.define
class Address:
    pass


@attrs.define
class Dimensions:
    pass


@attrs.define
class Weight:
    pass


@attrs.define
class Decimal:
    pass


@attrs.define
class ItemQuantity:
    pass


@attrs.define
class SubmitShipmentConfirmationsResponse:
    pass


@attrs.define
class SubmitShipmentStatusUpdatesResponse:
    pass


@attrs.define
class GetShippingLabelListResponse:
    pass


@attrs.define
class GetShippingLabelResponse:
    pass


@attrs.define
class ShippingLabelList:
    pass


@attrs.define
class LabelData:
    pass


@attrs.define
class ShippingLabel:
    pass


@attrs.define
class SubmitShippingLabelsResponse:
    pass


@attrs.define
class SubmitShipmentConfirmationsRequest:
    pass


@attrs.define
class ShipmentConfirmation:
    pass


@attrs.define
class SubmitShipmentStatusUpdatesRequest:
    pass


@attrs.define
class ShipmentStatusUpdate:
    pass


@attrs.define
class GetCustomerInvoicesResponse:
    pass


@attrs.define
class GetCustomerInvoiceResponse:
    pass


@attrs.define
class CustomerInvoiceList:
    pass


@attrs.define
class Pagination:
    pass


@attrs.define
class CustomerInvoice:
    pass


@attrs.define
class TransactionReference:
    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class Error:
    pass


@attrs.define
class Container:
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
