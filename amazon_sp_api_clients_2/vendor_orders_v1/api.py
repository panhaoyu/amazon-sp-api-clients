"""
Selling Partner API for Retail Procurement Orders
=============================================================================================
The Selling Partner API for Retail Procurement Orders provides programmatic access to vendor orders data.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient


class VendorOrdersV1Client(BaseClient):
    def get_purchase_orders(
        self,
        limit=None,
        created_after=None,
        created_before=None,
        sort_order=None,
        next_token=None,
        include_details=None,
        changed_after=None,
        changed_before=None,
        po_item_state=None,
        is_pochanged=None,
        purchase_order_state=None,
        ordering_vendor_code=None,
    ):
        """
        Returns a list of purchase orders created or changed during the time frame that you specify. You define the time frame using the createdAfter, createdBefore, changedAfter and changedBefore parameters. The date range to search must not be more than 7 days. You can choose to get only the purchase order numbers by setting includeDetails to false. You can then use the getPurchaseOrder operation to receive details for a specific purchase order.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            limit: The limit to the number of records returned. Default value is 100 records.
            created_after: Purchase orders that became available after this time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Purchase orders that became available before this time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort in ascending or descending order by purchase order creation date.
            next_token: Used for pagination when there is more purchase orders than the specified result size limit. The token value is returned in the previous API call
            include_details: When true, returns purchase orders with complete details. Otherwise, only purchase order numbers are returned. Default value is true.
            changed_after: Purchase orders that changed after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            changed_before: Purchase orders that changed before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            po_item_state: Current state of the purchase order item. If this value is Cancelled, this API will return purchase orders which have one or more items cancelled by Amazon with updated item quantity as zero.
            is_pochanged: When true, returns purchase orders which were modified after the order was placed. Vendors are required to pull the changed purchase order and fulfill the updated purchase order and not the original one. Default value is false.
            purchase_order_state: Filters purchase orders based on the purchase order state.
            ordering_vendor_code: Filters purchase orders based on the specified ordering vendor code. This value should be same as 'sellingParty.partyId' in the purchase order. If not included in the filter, all purchase orders for all of the vendor codes that exist in the vendor group used to authorize the API client application are returned.
        """
        url = "/vendor/orders/v1/purchaseOrders"

    def get_purchase_order(
        self,
        purchase_order_number,
    ):
        """
        Returns a purchase order based on the purchaseOrderNumber value that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchase_order_number: The purchase order identifier for the order that you want. Formatting Notes: 8-character alpha-numeric code.
        """
        url = "/vendor/orders/v1/purchaseOrders/{purchaseOrderNumber}"

    def submit_acknowledgement(
        self,
    ):
        """
        Submits acknowledgements for one or more purchase orders.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/vendor/orders/v1/acknowledgements"

    def get_purchase_orders_status(
        self,
        limit=None,
        sort_order=None,
        next_token=None,
        created_after=None,
        created_before=None,
        updated_after=None,
        updated_before=None,
        purchase_order_number=None,
        purchase_order_status=None,
        item_confirmation_status=None,
        item_receive_status=None,
        ordering_vendor_code=None,
        ship_to_party_id=None,
    ):
        """
        Returns purchase order statuses based on the filters that you specify. Date range to search must not be more than 7 days. You can return a list of purchase order statuses using the available filters, or a single purchase order status by providing the purchase order number.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            limit: The limit to the number of records returned. Default value is 100 records.
            sort_order: Sort in ascending or descending order by purchase order creation date.
            next_token: Used for pagination when there are more purchase orders than the specified result size limit.
            created_after: Purchase orders that became available after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Purchase orders that became available before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            updated_after: Purchase orders for which the last purchase order update happened after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            updated_before: Purchase orders for which the last purchase order update happened before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            purchase_order_number: Provides purchase order status for the specified purchase order number.
            purchase_order_status: Filters purchase orders based on the specified purchase order status. If not included in filter, this will return purchase orders for all statuses.
            item_confirmation_status: Filters purchase orders based on their item confirmation status. If the item confirmation status is not included in the filter, purchase orders for all confirmation statuses are included.
            item_receive_status: Filters purchase orders based on the purchase order's item receive status. If the item receive status is not included in the filter, purchase orders for all receive statuses are included.
            ordering_vendor_code: Filters purchase orders based on the specified ordering vendor code. This value should be same as 'sellingParty.partyId' in the purchase order. If not included in filter, all purchase orders for all the vendor codes that exist in the vendor group used to authorize API client application are returned.
            ship_to_party_id: Filters purchase orders for a specific buyer's Fulfillment Center/warehouse by providing ship to location id here. This value should be same as 'shipToParty.partyId' in the purchase order. If not included in filter, this will return purchase orders for all the buyer's warehouses used for vendor group purchase orders.
        """
        url = "/vendor/orders/v1/purchaseOrdersStatus"
