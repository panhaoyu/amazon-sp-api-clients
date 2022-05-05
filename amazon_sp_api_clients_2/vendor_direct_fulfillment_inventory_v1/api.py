"""
Selling Partner API for Direct Fulfillment Inventory Updates
=============================================================================================
The Selling Partner API for Direct Fulfillment Inventory Updates provides programmatic access to a direct fulfillment vendor's inventory updates.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class VendorDirectFulfillmentInventoryV1Client(BaseClient):
    def submit_inventory_update(
        self,
        warehouse_id: str,
    ):
        """
        Submits inventory updates for the specified warehouse for either a partial or full feed of inventory items.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            warehouse_id: Identifier for the warehouse for which to update inventory.
        """
        url = "/vendor/directFulfillment/inventory/v1/warehouses/{warehouseId}/items"
        values = (warehouse_id,)

    _submit_inventory_update_params = (("warehouseId", "path", True),)  # name, param in, required
