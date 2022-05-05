"""
Selling Partner API for Direct Fulfillment Shipping
=============================================================================================
The Selling Partner API for Direct Fulfillment Shipping provides programmatic access to a direct fulfillment vendor's shipping data.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2021-12-28
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class VendorDirectFulfillmentShipping20211228Client(BaseClient):
    def submit_shipping_label_request(
        self,
    ):
        """
        Creates a shipping label for a purchase order and returns a transactionId for reference.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        """
        path_parameters = {}

        url = "/vendor/directFulfillment/shipping/2021-12-28/shippingLabels".format(**path_parameters)

        query_parameters = {}

    def get_shipping_labels(
        self,
        ship_from_party_id: str = None,
        limit: int = None,
        created_after: str,
        created_before: str,
        sort_order: str = None,
        next_token: str = None,
    ):
        """
        Returns a list of shipping labels created during the time frame that you specify. You define that time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must not be more than 7 days.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            ship_from_party_id: The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            limit: The limit to the number of records returned.
            created_after: Shipping labels that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Shipping labels that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort ASC or DESC by order creation date.
            next_token: Used for pagination when there are more ship labels than the specified result size limit. The token value is returned in the previous API call.
        """
        path_parameters = {}

        url = "/vendor/directFulfillment/shipping/2021-12-28/shippingLabels".format(**path_parameters)

        query_parameters = {}

        if ship_from_party_id is not None:
            query_parameters["shipFromPartyId"] = ship_from_party_id

        if limit is not None:
            query_parameters["limit"] = limit

        query_parameters["createdAfter"] = created_after

        query_parameters["createdBefore"] = created_before

        if sort_order is not None:
            query_parameters["sortOrder"] = sort_order

        if next_token is not None:
            query_parameters["nextToken"] = next_token

    def get_shipping_label(
        self,
        purchase_order_number: str,
    ):
        """
        Returns a shipping label for the purchaseOrderNumber that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            purchase_order_number: The purchase order number for which you want to return the shipping label. It should be the same purchaseOrderNumber as received in the order.
        """
        path_parameters = {}

        path_parameters["purchaseOrderNumber"] = purchase_order_number

        url = "/vendor/directFulfillment/shipping/2021-12-28/shippingLabels/{purchaseOrderNumber}".format(
            **path_parameters
        )

        query_parameters = {}
