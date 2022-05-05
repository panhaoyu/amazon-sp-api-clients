"""
Selling Partner API for FBA Inventory
=============================================================================================

The Selling Partner API for FBA Inventory lets you programmatically retrieve information about inventory in Amazon's fulfillment network.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:

    code: str
    details: str
    message: str

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetInventorySummariesResponse:

    errors: "ErrorList"
    pagination: "Pagination"
    payload: "GetInventorySummariesResult"
    pass


@attrs.define
class GetInventorySummariesResult:

    granularity: "Granularity"
    inventory_summaries: "InventorySummaries"
    pass


@attrs.define
class Granularity:

    granularity_id: str
    granularity_type: str

    pass


@attrs.define
class InventoryDetails:

    fulfillable_quantity: int
    inbound_receiving_quantity: int
    inbound_shipped_quantity: int
    inbound_working_quantity: int

    researching_quantity: "ResearchingQuantity"
    reserved_quantity: "ReservedQuantity"
    unfulfillable_quantity: "UnfulfillableQuantity"
    pass


@attrs.define
class InventorySummaries:

    pass


@attrs.define
class InventorySummary:

    asin: str
    condition: str
    fn_sku: str
    last_updated_time: str
    # {'schema_format': 'date-time'}
    product_name: str
    seller_sku: str
    total_quantity: int

    inventory_details: "InventoryDetails"
    pass


@attrs.define
class Pagination:

    next_token: str

    pass


@attrs.define
class ResearchingQuantity:

    researching_quantity_breakdown: list["ResearchingQuantityEntry"]
    total_researching_quantity: int

    pass


@attrs.define
class ResearchingQuantityEntry:

    name: Union[
        Literal["researchingQuantityInShortTerm"],
        Literal["researchingQuantityInMidTerm"],
        Literal["researchingQuantityInLongTerm"],
    ]
    quantity: int

    pass


@attrs.define
class ReservedQuantity:

    fc_processing_quantity: int
    pending_customer_order_quantity: int
    pending_transshipment_quantity: int
    total_reserved_quantity: int

    pass


@attrs.define
class UnfulfillableQuantity:

    carrier_damaged_quantity: int
    customer_damaged_quantity: int
    defective_quantity: int
    distributor_damaged_quantity: int
    expired_quantity: int
    total_unfulfillable_quantity: int
    warehouse_damaged_quantity: int

    pass


class FbaInventoryV1Client(BaseClient):
    def get_inventory_summaries(
        self,
        granularity_type: Union[Literal["Marketplace"]],
        granularity_id: str,
        marketplace_ids: list[str],
        details: bool = None,
        start_date_time: str = None,
        seller_skus: list[str] = None,
        next_token: str = None,
    ):
        """
        Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the startDateTime and sellerSkus parameters:

        - All inventory summaries with available details are returned when the startDateTime and sellerSkus parameters are omitted.
        - When startDateTime is provided, the operation returns inventory summaries that have had changes after the date and time specified. The sellerSkus parameter is ignored.
        - When the sellerSkus parameter is provided, the operation returns inventory summaries for only the specified sellerSkus.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 2 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            details: true to return inventory summaries with additional summarized inventory details and quantities. Otherwise, returns inventory summaries only (default value).
            granularity_type: The granularity type for the inventory aggregation level.
            granularity_id: The granularity ID for the inventory aggregation level.
            start_date_time: A start date and time in ISO8601 format. If specified, all inventory summaries that have changed since then are returned. You must specify a date and time that is no earlier than 18 months prior to the date and time when you call the API. Note: Changes in inboundWorkingQuantity, inboundShippedQuantity and inboundReceivingQuantity are not detected.
            seller_skus: A list of seller SKUs for which to return inventory summaries. You may specify up to 50 SKUs.
            next_token: String token returned in the response of your previous request.
            marketplace_ids: The marketplace ID for the marketplace for which to return inventory summaries.
        """
        url = "/fba/inventory/v1/summaries"
        values = (
            details,
            granularity_type,
            granularity_id,
            start_date_time,
            seller_skus,
            next_token,
            marketplace_ids,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_inventory_summaries_params)
        return response

    _get_inventory_summaries_params = (  # name, param in
        ("details", "query"),
        ("granularityType", "query"),
        ("granularityId", "query"),
        ("startDateTime", "query"),
        ("sellerSkus", "query"),
        ("nextToken", "query"),
        ("marketplaceIds", "query"),
    )
