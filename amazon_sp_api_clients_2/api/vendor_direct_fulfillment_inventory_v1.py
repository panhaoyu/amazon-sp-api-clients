"""
Selling Partner API for Direct Fulfillment Inventory Updates
=============================================================================================

The Selling Partner API for Direct Fulfillment Inventory Updates provides programmatic access to a direct fulfillment vendor's inventory updates.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Error(**data)

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
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InventoryUpdate:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _inventory_update_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return InventoryUpdate(**data)

    is_full_update: bool = attrs.field(
        default=None,
    )
    """
    When true, this request contains a full feed. Otherwise, this request contains a partial feed. When sending a full feed, you must send information about all items in the warehouse. Any items not in the full feed are updated as not available. When sending a partial feed, only include the items that need an update to inventory. The status of other items will remain unchanged.
    """

    items: List["ItemDetails"] = attrs.field(
        default=None,
    )
    """
    A list of inventory items with updated details, including quantity available.
    """

    selling_party: "PartyIdentification" = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemDetails:
    """
    Updated inventory details for an item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ItemDetails(**data)

    available_quantity: "ItemQuantity" = attrs.field(
        default=None,
    )
    """
    Details of item quantity.
    """

    buyer_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The buyer selected product identification of the item. Either buyerProductIdentifier or vendorProductIdentifier should be submitted.
    """

    is_obsolete: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the item is permanently unavailable.
    """

    vendor_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor selected product identification of the item. Either buyerProductIdentifier or vendorProductIdentifier should be submitted.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    Details of item quantity.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_quantity_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ItemQuantity(**data)

    amount: Optional[int] = attrs.field(
        default=None,
    )
    """
    Quantity of units available for a specific item.
    """

    unit_of_measure: str = attrs.field(
        default=None,
    )
    """
    Unit of measure for the available quantity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _party_identification_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return PartyIdentification(**data)

    party_id: str = attrs.field(
        default=None,
    )
    """
    Assigned identification for the party.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInventoryUpdateRequest:
    """
    The request body for the submitInventoryUpdate operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_inventory_update_request_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SubmitInventoryUpdateRequest(**data)

    inventory: Optional["InventoryUpdate"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInventoryUpdateResponse:
    """
    The response schema for the submitInventoryUpdate operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_inventory_update_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SubmitInventoryUpdateResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionReference"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionReference:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transaction_reference_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return TransactionReference(**data)

    transaction_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_inventory_update_name_convert = {
    "isFullUpdate": "is_full_update",
    "items": "items",
    "sellingParty": "selling_party",
}

_item_details_name_convert = {
    "availableQuantity": "available_quantity",
    "buyerProductIdentifier": "buyer_product_identifier",
    "isObsolete": "is_obsolete",
    "vendorProductIdentifier": "vendor_product_identifier",
}

_item_quantity_name_convert = {
    "amount": "amount",
    "unitOfMeasure": "unit_of_measure",
}

_party_identification_name_convert = {
    "partyId": "party_id",
}

_submit_inventory_update_request_name_convert = {
    "inventory": "inventory",
}

_submit_inventory_update_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_transaction_reference_name_convert = {
    "transactionId": "transaction_id",
}


class VendorDirectFulfillmentInventoryV1Client(BaseClient):
    def submit_inventory_update(
        self,
        warehouse_id: str,
        inventory: Dict[str, Any] = None,
    ) -> Union[SubmitInventoryUpdateResponse]:
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
            inventory: no description.
        """
        url = "/vendor/directFulfillment/inventory/v1/warehouses/{warehouseId}/items"
        values = (
            warehouse_id,
            inventory,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_inventory_update_params,
            self._submit_inventory_update_responses,
        )
        return response

    _submit_inventory_update_params = (  # name, param in
        ("warehouseId", "path"),
        ("inventory", "body"),
    )

    _submit_inventory_update_responses = {
        202: SubmitInventoryUpdateResponse,
        400: SubmitInventoryUpdateResponse,
        403: SubmitInventoryUpdateResponse,
        404: SubmitInventoryUpdateResponse,
        413: SubmitInventoryUpdateResponse,
        415: SubmitInventoryUpdateResponse,
        429: SubmitInventoryUpdateResponse,
        500: SubmitInventoryUpdateResponse,
        503: SubmitInventoryUpdateResponse,
    }
