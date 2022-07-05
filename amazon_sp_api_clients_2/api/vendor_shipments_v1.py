"""
Selling Partner API for Retail Procurement Shipments
=============================================================================================

The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.
API Version: v1
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
    Address of the party.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Address(**data)

    address_line1: str = attrs.field(
        default=None,
    )
    """
    First line of the address.
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

    city: Optional[str] = attrs.field(
        default=None,
    )
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field(
        default=None,
    )
    """
    The two digit country code in ISO 3166-1 alpha-2 format.
    """

    county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The county where person, business or institution is located.
    """

    district: Optional[str] = attrs.field(
        default=None,
    )
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field(
        default=None,
    )
    """
    The name of the person, business or institution at that address.
    """

    phone: Optional[str] = attrs.field(
        default=None,
    )
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: Optional[str] = attrs.field(
        default=None,
    )
    """
    The state or region where person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Carton:
    """
    Details of the carton/package being shipped.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _carton_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Carton(**data)

    carton_identifiers: Optional[List["ContainerIdentification"]] = attrs.field(
        default=None,
    )
    """
    A list of carton identifiers.
    """

    carton_sequence_number: str = attrs.field(
        default=None,
    )
    """
    Carton sequence number for the carton. The first carton will be 001, the second 002, and so on. This number is used as a reference to refer to this carton from the pallet level.
    """

    dimensions: Optional["Dimensions"] = attrs.field(
        default=None,
    )
    """
    Physical dimensional measurements of a container.
    """

    items: List["ContainerItem"] = attrs.field(
        default=None,
    )
    """
    A list of container item details.
    """

    tracking_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    This is required to be provided for every carton in the small parcel shipments.
    """

    weight: Optional["Weight"] = attrs.field(
        default=None,
    )
    """
    The weight.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CartonReferenceDetails:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _carton_reference_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CartonReferenceDetails(**data)

    carton_count: Optional[int] = attrs.field(
        default=None,
    )
    """
    Pallet level carton count is mandatory for single item pallet and optional for mixed item pallet.
    """

    carton_reference_numbers: List[str] = attrs.field(
        default=None,
    )
    """
    Array of reference numbers for the carton that are part of this pallet/shipment. Please provide the cartonSequenceNumber from the 'cartons' segment to refer to that carton's details here.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContainerIdentification:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _container_identification_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ContainerIdentification(**data)

    container_identification_number: str = attrs.field(
        default=None,
    )
    """
    Container identification number that adheres to the definition of the container identification type.
    """

    container_identification_type: Union[
        Literal["SSCC"], Literal["AMZNCC"], Literal["GTIN"], Literal["BPS"], Literal["CID"]
    ] = attrs.field(
        default=None,
    )
    """
    The container identification type.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContainerItem:
    """
    Carton/Pallet level details for the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _container_item_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ContainerItem(**data)

    item_details: Optional["ItemDetails"] = attrs.field(
        default=None,
    )
    """
    Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate.
    """

    item_reference: str = attrs.field(
        default=None,
    )
    """
    The reference number for the item. Please provide the itemSequenceNumber from the 'items' segment to refer to that item's details here.
    """

    shipped_quantity: "ItemQuantity" = attrs.field(
        default=None,
    )
    """
    Details of item quantity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _decimal_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Decimal(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Dimensions:
    """
    Physical dimensional measurements of a container.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _dimensions_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Dimensions(**data)

    height: "Decimal" = attrs.field(
        default=None,
    )
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    length: "Decimal" = attrs.field(
        default=None,
    )
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    unit_of_measure: Union[Literal["In"], Literal["Ft"], Literal["Meter"], Literal["Yard"]] = attrs.field(
        default=None,
    )
    """
    The unit of measure for dimensions.
    """

    width: "Decimal" = attrs.field(
        default=None,
    )
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Duration:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _duration_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Duration(**data)

    duration_unit: Union[Literal["Days"], Literal["Months"]] = attrs.field(
        default=None,
    )
    """
    Unit for duration.
    """

    duration_value: int = attrs.field(
        default=None,
    )
    """
    Value for the duration in terms of the durationUnit.
    """


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
class Expiry:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _expiry_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Expiry(**data)

    expiry_after_duration: Optional["Duration"] = attrs.field(
        default=None,
    )

    expiry_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date that determines the limit of consumption or use of a product. Its meaning is determined based on the trade item context.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    manufacturer_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    Production, packaging or assembly date determined by the manufacturer. Its meaning is determined based on the trade item context.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ImportDetails:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _import_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ImportDetails(**data)

    billable_weight: Optional["Weight"] = attrs.field(
        default=None,
    )
    """
    The weight.
    """

    estimated_ship_by_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    Date on which the shipment is expected to be shipped. This value should not be in the past and not more than 60 days out in the future.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    import_containers: Optional[str] = attrs.field(
        default=None,
    )
    """
    Types and numbers of container(s) for import purchase orders. Can be a comma-separated list if shipment has multiple containers.

    Extra fields:
    {'maxLength': 64}
    """

    method_of_payment: Optional[
        Union[
            Literal["PaidByBuyer"],
            Literal["CollectOnDelivery"],
            Literal["DefinedByBuyerAndSeller"],
            Literal["FOBPortOfCall"],
            Literal["PrepaidBySeller"],
            Literal["PaidBySeller"],
        ]
    ] = attrs.field(
        default=None,
    )
    """
    This is used for import purchase orders only. If the recipient requests, this field will contain the shipment method of payment.
    """

    route: Optional["Route"] = attrs.field(
        default=None,
    )
    """
    This is used only for direct import shipment confirmations.
    """

    seal_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The container's seal number.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Item:
    """
    Details of the item being shipped.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Item(**data)

    amazon_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Amazon Standard Identification Number (ASIN) of an item.
    """

    item_details: Optional["ItemDetails"] = attrs.field(
        default=None,
    )
    """
    Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate.
    """

    item_sequence_number: str = attrs.field(
        default=None,
    )
    """
    Item sequence number for the item. The first item will be 001, the second 002, and so on. This number is used as a reference to refer to this item from the carton or pallet level.
    """

    shipped_quantity: "ItemQuantity" = attrs.field(
        default=None,
    )
    """
    Details of item quantity.
    """

    vendor_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor selected product identification of the item. Should be the same as was sent in the purchase order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemDetails:
    """
    Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ItemDetails(**data)

    expiry: Optional["Expiry"] = attrs.field(
        default=None,
    )

    handling_code: Optional[
        Union[Literal["Oversized"], Literal["Fragile"], Literal["Food"], Literal["HandleWithCare"]]
    ] = attrs.field(
        default=None,
    )
    """
    Identification of the instructions on how specified item/carton/pallet should be handled.
    """

    lot_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The batch or lot number associates an item with information the manufacturer considers relevant for traceability of the trade item to which the Element String is applied. The data may refer to the trade item itself or to items contained. This field is mandatory for all perishable items.
    """

    maximum_retail_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    purchase_order_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon purchase order number for the shipment being confirmed. If the items in this shipment belong to multiple purchase order numbers that are in particular carton or pallet within the shipment, then provide the purchaseOrderNumber at the appropriate carton or pallet level. Formatting Notes: 8-character alpha-numeric code.
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

    amount: int = attrs.field(
        default=None,
    )
    """
    Amount of units shipped for a specific item at a shipment level. If the item is present only in certain cartons or pallets within the shipment, please provide this at the appropriate carton or pallet level.
    """

    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]] = attrs.field(
        default=None,
    )
    """
    Unit of measure for the shipped quantity.
    """

    unit_size: Optional[int] = attrs.field(
        default=None,
    )
    """
    The case size, in the event that we ordered using cases. Otherwise, 1.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Location:
    """
    Location identifier.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _location_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Location(**data)

    country_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.
    """

    location_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    Location code.
    """

    type: Optional[str] = attrs.field(
        default=None,
    )
    """
    Type of location identification.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _money_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Money(**data)

    amount: "Decimal" = attrs.field(
        default=None,
    )
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    currency_code: str = attrs.field(
        default=None,
    )
    """
    Three digit currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pallet:
    """
    Details of the Pallet/Tare being shipped.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _pallet_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Pallet(**data)

    block: Optional[int] = attrs.field(
        default=None,
    )
    """
    Number of cartons per layer on the pallet.
    """

    carton_reference_details: Optional["CartonReferenceDetails"] = attrs.field(
        default=None,
    )

    dimensions: Optional["Dimensions"] = attrs.field(
        default=None,
    )
    """
    Physical dimensional measurements of a container.
    """

    items: Optional[List["ContainerItem"]] = attrs.field(
        default=None,
    )
    """
    A list of container item details.
    """

    pallet_identifiers: List["ContainerIdentification"] = attrs.field(
        default=None,
    )
    """
    A list of pallet identifiers.
    """

    tier: Optional[int] = attrs.field(
        default=None,
    )
    """
    Number of layers per pallet.
    """

    weight: Optional["Weight"] = attrs.field(
        default=None,
    )
    """
    The weight.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _party_identification_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return PartyIdentification(**data)

    address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    Address of the party.
    """

    party_id: str = attrs.field(
        default=None,
    )
    """
    Assigned identification for the party.
    """

    tax_registration_details: Optional[List["TaxRegistrationDetails"]] = attrs.field(
        default=None,
    )
    """
    Tax registration details of the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Route:
    """
    This is used only for direct import shipment confirmations.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _route_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Route(**data)

    stops: List["Stop"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentConfirmation:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_confirmation_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ShipmentConfirmation(**data)

    amazon_reference_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon Reference Number is a unique identifier generated by Amazon for all Collect/WePay shipments when you submit  a routing request. This field is mandatory for Collect/WePay shipments.
    """

    cartons: Optional[List["Carton"]] = attrs.field(
        default=None,
    )
    """
    A list of the cartons in this shipment.
    """

    estimated_delivery_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date and time on which the shipment is expected to reach buyer's warehouse. It needs to be an estimate based on the average transit time between ship from location and the destination. The exact appointment time will be provided by the buyer and is potentially not known when creating the shipment confirmation.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    import_details: Optional["ImportDetails"] = attrs.field(
        default=None,
    )

    pallets: Optional[List["Pallet"]] = attrs.field(
        default=None,
    )
    """
    A list of the pallets in this shipment.
    """

    selling_party: "PartyIdentification" = attrs.field(
        default=None,
    )

    ship_from_party: "PartyIdentification" = attrs.field(
        default=None,
    )

    ship_to_party: "PartyIdentification" = attrs.field(
        default=None,
    )

    shipment_confirmation_date: datetime = attrs.field(
        default=None,
    )
    """
    Date on which the shipment confirmation was submitted.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    shipment_confirmation_type: Union[Literal["Original"], Literal["Replace"]] = attrs.field(
        default=None,
    )
    """
    Indicates if this shipment confirmation is the initial confirmation, or intended to replace an already posted shipment confirmation. If replacing an existing shipment confirmation, be sure to provide the identical shipmentIdentifier and sellingParty information as in the previous confirmation.
    """

    shipment_identifier: str = attrs.field(
        default=None,
    )
    """
    Unique shipment ID (not used over the last 365 days).
    """

    shipment_measurements: Optional["ShipmentMeasurements"] = attrs.field(
        default=None,
    )
    """
    Shipment measurement details.
    """

    shipment_structure: Optional[
        Union[
            Literal["PalletizedAssortmentCase"],
            Literal["LooseAssortmentCase"],
            Literal["PalletOfItems"],
            Literal["PalletizedStandardCase"],
            Literal["LooseStandardCase"],
            Literal["MasterPallet"],
            Literal["MasterCase"],
        ]
    ] = attrs.field(
        default=None,
    )
    """
    Shipment hierarchical structure.
    """

    shipment_type: Optional[
        Union[Literal["TruckLoad"], Literal["LessThanTruckLoad"], Literal["SmallParcel"]]
    ] = attrs.field(
        default=None,
    )
    """
    The type of shipment.
    """

    shipped_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date and time of the departure of the shipment from the vendor's location. Vendors are requested to send ASNs within 30 minutes of departure from their warehouse/distribution center or at least 6 hours prior to the appointment time at the Amazon destination warehouse, whichever is sooner. Shipped date mentioned in the shipment confirmation should not be in the future.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    shipped_items: List["Item"] = attrs.field(
        default=None,
    )
    """
    A list of the items in this shipment and their associated details. If any of the item detail fields are common at a carton or a pallet level, provide them at the corresponding carton or pallet level.
    """

    transportation_details: Optional["TransportationDetails"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentMeasurements:
    """
    Shipment measurement details.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_measurements_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ShipmentMeasurements(**data)

    carton_count: Optional[int] = attrs.field(
        default=None,
    )
    """
    Number of cartons present in the shipment. Provide the cartonCount only for unpalletized shipments.
    """

    gross_shipment_weight: Optional["Weight"] = attrs.field(
        default=None,
    )
    """
    The weight.
    """

    pallet_count: Optional[int] = attrs.field(
        default=None,
    )
    """
    Number of pallets present in the shipment. Provide the palletCount only for palletized shipments.
    """

    shipment_volume: Optional["Volume"] = attrs.field(
        default=None,
    )
    """
    The volume of the container.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Stop:
    """
    Contractual or operational port or point relevant to the movement of the cargo.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _stop_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Stop(**data)

    arrival_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    Date and time of the arrival of the cargo.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    departure_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    Date and time of the departure of the cargo.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    function_code: Union[
        Literal["PortOfDischarge"], Literal["FreightPayableAt"], Literal["PortOfLoading"]
    ] = attrs.field(
        default=None,
    )
    """
    Provide the function code.
    """

    location_identification: Optional["Location"] = attrs.field(
        default=None,
    )
    """
    Location identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitShipmentConfirmationsRequest:
    """
    The request schema for the SubmitShipmentConfirmations operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_shipment_confirmations_request_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SubmitShipmentConfirmationsRequest(**data)

    shipment_confirmations: Optional[List["ShipmentConfirmation"]] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitShipmentConfirmationsResponse:
    """
    The response schema for the SubmitShipmentConfirmations operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_shipment_confirmations_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SubmitShipmentConfirmationsResponse(**data)

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
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _tax_registration_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return TaxRegistrationDetails(**data)

    tax_registration_number: str = attrs.field(
        default=None,
    )
    """
    Tax registration number for the entity. For example, VAT ID.
    """

    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field(
        default=None,
    )
    """
    Tax registration type for the entity.
    """


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
    GUID assigned by Amazon to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransportationDetails:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transportation_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return TransportationDetails(**data)

    bill_of_lading_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    Bill Of Lading (BOL) number is the unique number assigned by the vendor. The BOL present in the Shipment Confirmation message ideally matches the paper BOL provided with the shipment, but that is no must. Instead of BOL, an alternative reference number (like Delivery Note Number) for the shipment can also be sent in this field.
    """

    carrier_scac: Optional[str] = attrs.field(
        default=None,
    )
    """
    Code that identifies the carrier for the shipment. The Standard Carrier Alpha Code (SCAC) is a unique two to four letter code used to identify a carrier. Carrier SCAC codes are assigned and maintained by the NMFTA (National Motor Freight Association). This field is mandatory for US, CA, MX shipment confirmations.
    """

    carrier_shipment_reference_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The field also known as PRO number is a unique number assigned by the carrier. It is used to identify and track the shipment that goes out for delivery. This field is mandatory for UA, CA, MX shipment confirmations.
    """

    transportation_mode: Optional[Union[Literal["Road"], Literal["Air"], Literal["Ocean"]]] = attrs.field(
        default=None,
    )
    """
    The mode of transportation for this shipment.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Volume:
    """
    The volume of the container.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _volume_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Volume(**data)

    unit_of_measure: Union[Literal["CuFt"], Literal["CuIn"], Literal["CuM"], Literal["CuY"]] = attrs.field(
        default=None,
    )
    """
    The unit of measurement.
    """

    value: "Decimal" = attrs.field(
        default=None,
    )
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Weight:
    """
    The weight.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _weight_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Weight(**data)

    unit_of_measure: Union[Literal["G"], Literal["Kg"], Literal["Oz"], Literal["Lb"]] = attrs.field(
        default=None,
    )
    """
    The unit of measurement.
    """

    value: "Decimal" = attrs.field(
        default=None,
    )
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """


_address_name_convert = {
    "addressLine1": "address_line1",
    "addressLine2": "address_line2",
    "addressLine3": "address_line3",
    "city": "city",
    "countryCode": "country_code",
    "county": "county",
    "district": "district",
    "name": "name",
    "phone": "phone",
    "postalCode": "postal_code",
    "stateOrRegion": "state_or_region",
}

_carton_name_convert = {
    "cartonIdentifiers": "carton_identifiers",
    "cartonSequenceNumber": "carton_sequence_number",
    "dimensions": "dimensions",
    "items": "items",
    "trackingNumber": "tracking_number",
    "weight": "weight",
}

_carton_reference_details_name_convert = {
    "cartonCount": "carton_count",
    "cartonReferenceNumbers": "carton_reference_numbers",
}

_container_identification_name_convert = {
    "containerIdentificationNumber": "container_identification_number",
    "containerIdentificationType": "container_identification_type",
}

_container_item_name_convert = {
    "itemDetails": "item_details",
    "itemReference": "item_reference",
    "shippedQuantity": "shipped_quantity",
}

_decimal_name_convert = {}

_dimensions_name_convert = {
    "height": "height",
    "length": "length",
    "unitOfMeasure": "unit_of_measure",
    "width": "width",
}

_duration_name_convert = {
    "durationUnit": "duration_unit",
    "durationValue": "duration_value",
}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_expiry_name_convert = {
    "expiryAfterDuration": "expiry_after_duration",
    "expiryDate": "expiry_date",
    "manufacturerDate": "manufacturer_date",
}

_import_details_name_convert = {
    "billableWeight": "billable_weight",
    "estimatedShipByDate": "estimated_ship_by_date",
    "importContainers": "import_containers",
    "methodOfPayment": "method_of_payment",
    "route": "route",
    "sealNumber": "seal_number",
}

_item_name_convert = {
    "amazonProductIdentifier": "amazon_product_identifier",
    "itemDetails": "item_details",
    "itemSequenceNumber": "item_sequence_number",
    "shippedQuantity": "shipped_quantity",
    "vendorProductIdentifier": "vendor_product_identifier",
}

_item_details_name_convert = {
    "expiry": "expiry",
    "handlingCode": "handling_code",
    "lotNumber": "lot_number",
    "maximumRetailPrice": "maximum_retail_price",
    "purchaseOrderNumber": "purchase_order_number",
}

_item_quantity_name_convert = {
    "amount": "amount",
    "unitOfMeasure": "unit_of_measure",
    "unitSize": "unit_size",
}

_location_name_convert = {
    "countryCode": "country_code",
    "locationCode": "location_code",
    "type": "type",
}

_money_name_convert = {
    "amount": "amount",
    "currencyCode": "currency_code",
}

_pallet_name_convert = {
    "block": "block",
    "cartonReferenceDetails": "carton_reference_details",
    "dimensions": "dimensions",
    "items": "items",
    "palletIdentifiers": "pallet_identifiers",
    "tier": "tier",
    "weight": "weight",
}

_party_identification_name_convert = {
    "address": "address",
    "partyId": "party_id",
    "taxRegistrationDetails": "tax_registration_details",
}

_route_name_convert = {
    "stops": "stops",
}

_shipment_confirmation_name_convert = {
    "amazonReferenceNumber": "amazon_reference_number",
    "cartons": "cartons",
    "estimatedDeliveryDate": "estimated_delivery_date",
    "importDetails": "import_details",
    "pallets": "pallets",
    "sellingParty": "selling_party",
    "shipFromParty": "ship_from_party",
    "shipToParty": "ship_to_party",
    "shipmentConfirmationDate": "shipment_confirmation_date",
    "shipmentConfirmationType": "shipment_confirmation_type",
    "shipmentIdentifier": "shipment_identifier",
    "shipmentMeasurements": "shipment_measurements",
    "shipmentStructure": "shipment_structure",
    "shipmentType": "shipment_type",
    "shippedDate": "shipped_date",
    "shippedItems": "shipped_items",
    "transportationDetails": "transportation_details",
}

_shipment_measurements_name_convert = {
    "cartonCount": "carton_count",
    "grossShipmentWeight": "gross_shipment_weight",
    "palletCount": "pallet_count",
    "shipmentVolume": "shipment_volume",
}

_stop_name_convert = {
    "arrivalTime": "arrival_time",
    "departureTime": "departure_time",
    "functionCode": "function_code",
    "locationIdentification": "location_identification",
}

_submit_shipment_confirmations_request_name_convert = {
    "shipmentConfirmations": "shipment_confirmations",
}

_submit_shipment_confirmations_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_tax_registration_details_name_convert = {
    "taxRegistrationNumber": "tax_registration_number",
    "taxRegistrationType": "tax_registration_type",
}

_transaction_reference_name_convert = {
    "transactionId": "transaction_id",
}

_transportation_details_name_convert = {
    "billOfLadingNumber": "bill_of_lading_number",
    "carrierScac": "carrier_scac",
    "carrierShipmentReferenceNumber": "carrier_shipment_reference_number",
    "transportationMode": "transportation_mode",
}

_volume_name_convert = {
    "unitOfMeasure": "unit_of_measure",
    "value": "value",
}

_weight_name_convert = {
    "unitOfMeasure": "unit_of_measure",
    "value": "value",
}


class VendorShipmentsV1Client(BaseClient):
    def submit_shipment_confirmations(
        self,
        shipment_confirmations: List["ShipmentConfirmation"] = None,
    ) -> Union[SubmitShipmentConfirmationsResponse]:
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
        url = "/vendor/shipping/v1/shipmentConfirmations"
        values = (shipment_confirmations,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_shipment_confirmations_params,
            self._submit_shipment_confirmations_responses,
        )
        return response

    _submit_shipment_confirmations_params = (("shipmentConfirmations", "body"),)  # name, param in

    _submit_shipment_confirmations_responses = {
        202: SubmitShipmentConfirmationsResponse,
        400: SubmitShipmentConfirmationsResponse,
        403: SubmitShipmentConfirmationsResponse,
        404: SubmitShipmentConfirmationsResponse,
        413: SubmitShipmentConfirmationsResponse,
        415: SubmitShipmentConfirmationsResponse,
        429: SubmitShipmentConfirmationsResponse,
        500: SubmitShipmentConfirmationsResponse,
        503: SubmitShipmentConfirmationsResponse,
    }
