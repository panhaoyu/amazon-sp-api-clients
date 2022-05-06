"""
Selling Partner API for Fulfillment Inbound
=============================================================================================

The Selling Partner API for Fulfillment Inbound lets you create applications that create and update inbound shipments of inventory to Amazon's fulfillment network.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class ASINInboundGuidance:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    guidance_reason_list: "GuidanceReasonList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    inbound_guidance: "InboundGuidance" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ASINInboundGuidanceList:

    pass


@attrs.define
class ASINPrepInstructions:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    barcode_instruction: "BarcodeInstruction" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    prep_guidance: "PrepGuidance" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    prep_instruction_list: "PrepInstructionList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ASINPrepInstructionsList:

    pass


@attrs.define
class Address:

    address_line1: str = attrs.field(
        kw_only=True,
    )
    """
    The street address information.

    Extra fields:
    {'maxLength': 180}
    """

    address_line2: str = attrs.field(
        kw_only=True,
    )
    """
    Additional street address information, if required.

    Extra fields:
    {'maxLength': 60}
    """

    city: str = attrs.field(
        kw_only=True,
    )
    """
    The city.

    Extra fields:
    {'maxLength': 30}
    """

    country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The country code in two-character ISO 3166-1 alpha-2 format.
    """

    district_or_county: str = attrs.field(
        kw_only=True,
    )
    """
    The district or county.

    Extra fields:
    {'maxLength': 25}
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    Name of the individual or business.

    Extra fields:
    {'maxLength': 50}
    """

    postal_code: str = attrs.field(
        kw_only=True,
    )
    """
    The postal code.
        If postal codes are used in your marketplace, we recommended that you include one with your request. This helps Amazon select the most appropriate Amazon fulfillment center for the inbound shipment plan.

    Extra fields:
    {'maxLength': 30}
    """

    state_or_province_code: str = attrs.field(
        kw_only=True,
    )
    """
    The state or province code.
        If state or province codes are used in your marketplace, it is recommended that you include one with your request. This helps Amazon to select the most appropriate Amazon fulfillment center for your inbound shipment plan.
    """

    pass


@attrs.define
class AmazonPrepFeesDetails:

    fee_per_unit: "Amount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    prep_instruction: "PrepInstruction" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AmazonPrepFeesDetailsList:

    pass


@attrs.define
class Amount:

    currency_code: "CurrencyCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    value: "BigDecimalType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class BarcodeInstruction:

    pass


@attrs.define
class BigDecimalType:

    pass


@attrs.define
class BillOfLadingDownloadURL:

    download_url: str = attrs.field(
        kw_only=True,
    )
    """
    URL to download the bill of lading for the package. Note: The URL will only be valid for 15 seconds
    """

    pass


@attrs.define
class BoxContentsFeeDetails:

    fee_per_unit: "Amount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_fee: "Amount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_units: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class BoxContentsSource:

    pass


@attrs.define
class CommonTransportResult:

    transport_result: "TransportResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Condition:

    pass


@attrs.define
class ConfirmPreorderResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "ConfirmPreorderResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ConfirmPreorderResult:

    confirmed_fulfillable_date: "DateStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    confirmed_need_by_date: "DateStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ConfirmTransportResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "CommonTransportResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Contact:

    email: str = attrs.field(
        kw_only=True,
    )
    """
    The email address of the contact person.

    Extra fields:
    {'maxLength': 50}
    """

    fax: str = attrs.field(
        kw_only=True,
    )
    """
    The fax number of the contact person.

    Extra fields:
    {'maxLength': 20}
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the contact person.

    Extra fields:
    {'maxLength': 50}
    """

    phone: str = attrs.field(
        kw_only=True,
    )
    """
    The phone number of the contact person.

    Extra fields:
    {'maxLength': 20}
    """

    pass


@attrs.define
class CreateInboundShipmentPlanRequest:

    ship_to_country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The two-character country code for the country where the inbound shipment is to be sent.
        Note: Not required. Specifying both ShipToCountryCode and ShipToCountrySubdivisionCode returns an error.
        Values:
        ShipToCountryCode values for North America:
        * CA – Canada
        * MX - Mexico
        * US - United States
        ShipToCountryCode values for MCI sellers in Europe:
        * DE – Germany
        * ES – Spain
        * FR – France
        * GB – United Kingdom
        * IT – Italy
        Default: The country code for the seller's home marketplace.
    """

    ship_to_country_subdivision_code: str = attrs.field(
        kw_only=True,
    )
    """
    The two-character country code, followed by a dash and then up to three characters that represent the subdivision of the country where the inbound shipment is to be sent. For example, "IN-MH". In full ISO 3166-2 format.
        Note: Not required. Specifying both ShipToCountryCode and ShipToCountrySubdivisionCode returns an error.
    """

    inbound_shipment_plan_request_items: "InboundShipmentPlanRequestItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_prep_preference: "LabelPrepPreference" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateInboundShipmentPlanResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "CreateInboundShipmentPlanResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateInboundShipmentPlanResult:

    inbound_shipment_plans: "InboundShipmentPlanList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CurrencyCode:

    pass


@attrs.define
class DateStringType:

    pass


@attrs.define
class Dimensions:

    height: "BigDecimalType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    length: "BigDecimalType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    unit: "UnitOfMeasurement" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    width: "BigDecimalType" = attrs.field(
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
    An error code that identifies the type of error that occured.
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
    A message that describes the error condition in a human-readable form.
    """

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class ErrorReason:

    pass


@attrs.define
class EstimateTransportResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "CommonTransportResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetBillOfLadingResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "BillOfLadingDownloadURL" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetInboundGuidanceResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetInboundGuidanceResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetInboundGuidanceResult:

    asininbound_guidance_list: "ASINInboundGuidanceList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    invalid_asinlist: "InvalidASINList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    invalid_skulist: "InvalidSKUList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    skuinbound_guidance_list: "SKUInboundGuidanceList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetLabelsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "LabelDownloadURL" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetPreorderInfoResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetPreorderInfoResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetPreorderInfoResult:

    shipment_confirmed_for_preorder: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether this shipment has been confirmed for pre-order.
    """

    shipment_contains_preorderable_items: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether the shipment contains items that have been enabled for pre-order. For more information about enabling items for pre-order, see the Seller Central Help.
    """

    confirmed_fulfillable_date: "DateStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    need_by_date: "DateStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetPrepInstructionsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetPrepInstructionsResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetPrepInstructionsResult:

    asinprep_instructions_list: "ASINPrepInstructionsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    invalid_asinlist: "InvalidASINList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    invalid_skulist: "InvalidSKUList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    skuprep_instructions_list: "SKUPrepInstructionsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetShipmentItemsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetShipmentItemsResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetShipmentItemsResult:

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """

    item_data: "InboundShipmentItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetShipmentsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetShipmentsResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetShipmentsResult:

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """

    shipment_data: "InboundShipmentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetTransportDetailsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetTransportDetailsResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetTransportDetailsResult:

    transport_content: "TransportContent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GuidanceReason:

    pass


@attrs.define
class GuidanceReasonList:

    pass


@attrs.define
class InboundGuidance:

    pass


@attrs.define
class InboundShipmentHeader:

    are_cases_required: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether or not an inbound shipment contains case-packed boxes. Note: A shipment must contain either all case-packed boxes or all individually packed boxes.
        Possible values:
        true - All boxes in the shipment must be case packed.
        false - All boxes in the shipment must be individually packed.
        Note: If AreCasesRequired = true for an inbound shipment, then the value of QuantityInCase must be greater than zero for every item in the shipment. Otherwise the service returns an error.
    """

    destination_fulfillment_center_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the fulfillment center to which the shipment will be shipped. Get this value from the InboundShipmentPlan object in the response returned by the createInboundShipmentPlan operation.
    """

    shipment_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name for the shipment. Use a naming convention that helps distinguish between shipments over time, such as the date the shipment was created.
    """

    intended_box_contents_source: "IntendedBoxContentsSource" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_prep_preference: "LabelPrepPreference" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_status: "ShipmentStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InboundShipmentInfo:

    are_cases_required: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether or not an inbound shipment contains case-packed boxes. When AreCasesRequired = true for an inbound shipment, all items in the inbound shipment must be case packed.
    """

    destination_fulfillment_center_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon fulfillment center identifier created by Amazon.
    """

    shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    The shipment identifier submitted in the request.
    """

    shipment_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name for the inbound shipment.
    """

    box_contents_source: "BoxContentsSource" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    confirmed_need_by_date: "DateStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    estimated_box_contents_fee: "BoxContentsFeeDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_prep_type: "LabelPrepType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_status: "ShipmentStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InboundShipmentItem:

    fulfillment_network_sku: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon's fulfillment network SKU of the item.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    A shipment identifier originally returned by the createInboundShipmentPlan operation.
    """

    prep_details_list: "PrepDetailsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity_in_case: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity_received: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity_shipped: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    release_date: "DateStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InboundShipmentItemList:

    pass


@attrs.define
class InboundShipmentList:

    pass


@attrs.define
class InboundShipmentPlan:

    destination_fulfillment_center_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon fulfillment center identifier created by Amazon.
    """

    shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    A shipment identifier originally returned by the createInboundShipmentPlan operation.
    """

    estimated_box_contents_fee: "BoxContentsFeeDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    items: "InboundShipmentPlanItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_prep_type: "LabelPrepType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_to_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InboundShipmentPlanItem:

    fulfillment_network_sku: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon's fulfillment network SKU of the item.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    prep_details_list: "PrepDetailsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InboundShipmentPlanItemList:

    pass


@attrs.define
class InboundShipmentPlanList:

    pass


@attrs.define
class InboundShipmentPlanRequestItem:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    condition: "Condition" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    prep_details_list: "PrepDetailsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity_in_case: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InboundShipmentPlanRequestItemList:

    pass


@attrs.define
class InboundShipmentRequest:

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    A marketplace identifier. Specifies the marketplace where the product would be stored.
    """

    inbound_shipment_header: "InboundShipmentHeader" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    inbound_shipment_items: "InboundShipmentItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InboundShipmentResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "InboundShipmentResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InboundShipmentResult:

    shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    The shipment identifier submitted in the request.
    """

    pass


@attrs.define
class IntendedBoxContentsSource:

    pass


@attrs.define
class InvalidASIN:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    error_reason: "ErrorReason" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InvalidASINList:

    pass


@attrs.define
class InvalidSKU:

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    error_reason: "ErrorReason" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InvalidSKUList:

    pass


@attrs.define
class LabelDownloadURL:

    download_url: str = attrs.field(
        kw_only=True,
    )
    """
    URL to download the label for the package. Note: The URL will only be valid for 15 seconds
    """

    pass


@attrs.define
class LabelPrepPreference:

    pass


@attrs.define
class LabelPrepType:

    pass


@attrs.define
class NonPartneredLtlDataInput:

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The carrier that you are using for the inbound shipment.
    """

    pro_number: "ProNumber" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class NonPartneredLtlDataOutput:

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The carrier that you are using for the inbound shipment.
    """

    pro_number: "ProNumber" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class NonPartneredSmallParcelDataInput:

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The carrier that you are using for the inbound shipment.
    """

    package_list: "NonPartneredSmallParcelPackageInputList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class NonPartneredSmallParcelDataOutput:

    package_list: "NonPartneredSmallParcelPackageOutputList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class NonPartneredSmallParcelPackageInput:

    tracking_id: "TrackingId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class NonPartneredSmallParcelPackageInputList:

    pass


@attrs.define
class NonPartneredSmallParcelPackageOutput:

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The carrier that you are using for the inbound shipment.
    """

    package_status: "PackageStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tracking_id: "TrackingId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class NonPartneredSmallParcelPackageOutputList:

    pass


@attrs.define
class PackageStatus:

    pass


@attrs.define
class Pallet:

    is_stacked: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether pallets will be stacked when carrier arrives for pick-up.
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
class PalletList:

    pass


@attrs.define
class PartneredEstimate:

    amount: "Amount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    confirm_deadline: "TimeStampStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    void_deadline: "TimeStampStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PartneredLtlDataInput:

    box_count: "UnsignedIntType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    contact: "Contact" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    freight_ready_date: "DateStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pallet_list: "PalletList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    seller_declared_value: "Amount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    seller_freight_class: "SellerFreightClass" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PartneredLtlDataOutput:

    amazon_reference_id: str = attrs.field(
        kw_only=True,
    )
    """
    A unique identifier created by Amazon that identifies this Amazon-partnered, Less Than Truckload/Full Truckload (LTL/FTL) shipment.
    """

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The carrier for the inbound shipment.
    """

    is_bill_of_lading_available: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether the bill of lading for the shipment is available.
    """

    amazon_calculated_value: "Amount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    box_count: "UnsignedIntType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    contact: "Contact" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    freight_ready_date: "DateStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pallet_list: "PalletList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    partnered_estimate: "PartneredEstimate" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    preview_delivery_date: "DateStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    preview_freight_class: "SellerFreightClass" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    preview_pickup_date: "DateStringType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    seller_declared_value: "Amount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    seller_freight_class: "SellerFreightClass" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PartneredSmallParcelDataInput:

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-partnered carrier to use for the inbound shipment.
    """

    package_list: "PartneredSmallParcelPackageInputList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PartneredSmallParcelDataOutput:

    package_list: "PartneredSmallParcelPackageOutputList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    partnered_estimate: "PartneredEstimate" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PartneredSmallParcelPackageInput:

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
class PartneredSmallParcelPackageInputList:

    pass


@attrs.define
class PartneredSmallParcelPackageOutput:

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The carrier specified with a previous call to putTransportDetails.
    """

    dimensions: "Dimensions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    package_status: "PackageStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tracking_id: "TrackingId" = attrs.field(
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
class PartneredSmallParcelPackageOutputList:

    pass


@attrs.define
class PrepDetails:

    prep_instruction: "PrepInstruction" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    prep_owner: "PrepOwner" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PrepDetailsList:

    pass


@attrs.define
class PrepGuidance:

    pass


@attrs.define
class PrepInstruction:

    pass


@attrs.define
class PrepInstructionList:

    pass


@attrs.define
class PrepOwner:

    pass


@attrs.define
class ProNumber:

    pass


@attrs.define
class PutTransportDetailsRequest:

    is_partnered: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether a putTransportDetails request is for an Amazon-partnered carrier.
    """

    shipment_type: "ShipmentType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    transport_details: "TransportDetailInput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PutTransportDetailsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "CommonTransportResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Quantity:

    pass


@attrs.define
class SKUInboundGuidance:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    guidance_reason_list: "GuidanceReasonList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    inbound_guidance: "InboundGuidance" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SKUInboundGuidanceList:

    pass


@attrs.define
class SKUPrepInstructions:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    amazon_prep_fees_details_list: "AmazonPrepFeesDetailsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    barcode_instruction: "BarcodeInstruction" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    prep_guidance: "PrepGuidance" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    prep_instruction_list: "PrepInstructionList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SKUPrepInstructionsList:

    pass


@attrs.define
class SellerFreightClass:

    pass


@attrs.define
class ShipmentStatus:

    pass


@attrs.define
class ShipmentType:

    pass


@attrs.define
class TimeStampStringType:

    pass


@attrs.define
class TrackingId:

    pass


@attrs.define
class TransportContent:

    transport_details: "TransportDetailOutput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    transport_header: "TransportHeader" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    transport_result: "TransportResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TransportDetailInput:

    non_partnered_ltl_data: "NonPartneredLtlDataInput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    non_partnered_small_parcel_data: "NonPartneredSmallParcelDataInput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    partnered_ltl_data: "PartneredLtlDataInput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    partnered_small_parcel_data: "PartneredSmallParcelDataInput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TransportDetailOutput:

    non_partnered_ltl_data: "NonPartneredLtlDataOutput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    non_partnered_small_parcel_data: "NonPartneredSmallParcelDataOutput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    partnered_ltl_data: "PartneredLtlDataOutput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    partnered_small_parcel_data: "PartneredSmallParcelDataOutput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TransportHeader:

    is_partnered: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether a putTransportDetails request is for a partnered carrier.
        Possible values:
        * true – Request is for an Amazon-partnered carrier.
        * false – Request is for a non-Amazon-partnered carrier.
    """

    seller_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon seller identifier.
    """

    shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    A shipment identifier originally returned by the createInboundShipmentPlan operation.
    """

    shipment_type: "ShipmentType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TransportResult:

    error_code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occured.
    """

    error_description: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition.
    """

    transport_status: "TransportStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TransportStatus:

    pass


@attrs.define
class UnitOfMeasurement:

    pass


@attrs.define
class UnitOfWeight:

    pass


@attrs.define
class UnsignedIntType:

    pass


@attrs.define
class VoidTransportResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "CommonTransportResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Weight:

    unit: "UnitOfWeight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    value: "BigDecimalType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


class FulfillmentInboundV0Client(BaseClient):
    def confirm_preorder(
        self,
        shipment_id: str,
        need_by_date: str,
        marketplace_id: str,
    ):
        """
        Returns information needed to confirm a shipment for pre-order. Call this operation after calling the getPreorderInfo operation to get the NeedByDate value and other pre-order information about the shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            need_by_date: Date that the shipment must arrive at the Amazon fulfillment center to avoid delivery promise breaks for pre-ordered items. Must be in YYYY-MM-DD format. The response to the getPreorderInfo operation returns this value.
            marketplace_id: A marketplace identifier. Specifies the marketplace the shipment is tied to.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/preorder/confirm"
        values = (
            shipment_id,
            need_by_date,
            marketplace_id,
        )
        response = self._parse_args_and_request(url, "PUT", values, self._confirm_preorder_params)
        return response

    _confirm_preorder_params = (  # name, param in
        ("shipmentId", "path"),
        ("NeedByDate", "query"),
        ("MarketplaceId", "query"),
    )

    def confirm_transport(
        self,
        shipment_id: str,
    ):
        """
        Confirms that the seller accepts the Amazon-partnered shipping estimate, agrees to allow Amazon to charge their account for the shipping cost, and requests that the Amazon-partnered carrier ship the inbound shipment.

        Prior to calling the confirmTransport operation, you should call the getTransportDetails operation to get the Amazon-partnered shipping estimate.

        Important: After confirming the transportation request, if the seller decides that they do not want the Amazon-partnered carrier to ship the inbound shipment, you can call the voidTransport operation to cancel the transportation request. Note that for a Small Parcel shipment, the seller has 24 hours after confirming a transportation request to void the transportation request. For a Less Than Truckload/Full Truckload (LTL/FTL) shipment, the seller has one hour after confirming a transportation request to void it. After the grace period has expired the seller's account will be charged for the shipping cost.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/confirm"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "POST", values, self._confirm_transport_params)
        return response

    _confirm_transport_params = (("shipmentId", "path"),)  # name, param in

    def create_inbound_shipment(
        self,
        shipment_id: str,
        inbound_shipment_header: dict[str, Any],
        inbound_shipment_items: list["InboundShipmentItem"],
        marketplace_id: str,
    ):
        """
        Returns a new inbound shipment based on the specified shipmentId that was returned by the createInboundShipmentPlan operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            inbound_shipment_header: Inbound shipment information used to create and update inbound shipments.
            inbound_shipment_items: A list of inbound shipment item information.
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}"
        values = (
            shipment_id,
            inbound_shipment_header,
            inbound_shipment_items,
            marketplace_id,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_inbound_shipment_params)
        return response

    _create_inbound_shipment_params = (  # name, param in
        ("shipmentId", "path"),
        ("InboundShipmentHeader", "body"),
        ("InboundShipmentItems", "body"),
        ("MarketplaceId", "body"),
    )

    def create_inbound_shipment_plan(
        self,
    ):
        """
        Returns one or more inbound shipment plans, which provide the information you need to create one or more inbound shipments for a set of items that you specify. Multiple inbound shipment plans might be required so that items can be optimally placed in Amazon's fulfillment network—for example, positioning inventory closer to the customer. Alternatively, two inbound shipment plans might be created with the same Amazon fulfillment center destination if the two shipment plans require different processing—for example, items that require labels must be shipped separately from stickerless, commingled inventory.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/fba/inbound/v0/plans"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._create_inbound_shipment_plan_params)
        return response

    _create_inbound_shipment_plan_params = ()  # name, param in

    def estimate_transport(
        self,
        shipment_id: str,
    ):
        """
        Initiates the process of estimating the shipping cost for an inbound shipment by an Amazon-partnered carrier.

        Prior to calling the estimateTransport operation, you must call the putTransportDetails operation to provide Amazon with the transportation information for the inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/estimate"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "POST", values, self._estimate_transport_params)
        return response

    _estimate_transport_params = (("shipmentId", "path"),)  # name, param in

    def get_bill_of_lading(
        self,
        shipment_id: str,
    ):
        """
        Returns a bill of lading for a Less Than Truckload/Full Truckload (LTL/FTL) shipment. The getBillOfLading operation returns PDF document data for printing a bill of lading for an Amazon-partnered Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/billOfLading"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_bill_of_lading_params)
        return response

    _get_bill_of_lading_params = (("shipmentId", "path"),)  # name, param in

    def get_inbound_guidance(
        self,
        marketplace_id: str,
        seller_skulist: list[str] = None,
        asinlist: list[str] = None,
    ):
        """
        Returns information that lets a seller know if Amazon recommends sending an item to a given marketplace. In some cases, Amazon provides guidance for why a given SellerSKU or ASIN is not recommended for shipment to Amazon's fulfillment network. Sellers may still ship items that are not recommended, at their discretion.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
            seller_skulist: A list of SellerSKU values. Used to identify items for which you want inbound guidance for shipment to Amazon's fulfillment network. Note: SellerSKU is qualified by the SellerId, which is included with every Selling Partner API operation that you submit. If you specify a SellerSKU that identifies a variation parent ASIN, this operation returns an error. A variation parent ASIN represents a generic product that cannot be sold. Variation child ASINs represent products that have specific characteristics (such as size and color) and can be sold.
            asinlist: A list of ASIN values. Used to identify items for which you want inbound guidance for shipment to Amazon's fulfillment network. Note: If you specify a ASIN that identifies a variation parent ASIN, this operation returns an error. A variation parent ASIN represents a generic product that cannot be sold. Variation child ASINs represent products that have specific characteristics (such as size and color) and can be sold.
        """
        url = "/fba/inbound/v0/itemsGuidance"
        values = (
            marketplace_id,
            seller_skulist,
            asinlist,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_inbound_guidance_params)
        return response

    _get_inbound_guidance_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("SellerSKUList", "query"),
        ("ASINList", "query"),
    )

    def get_labels(
        self,
        shipment_id: str,
        page_type: Union[
            Literal["PackageLabel_Letter_2"],
            Literal["PackageLabel_Letter_4"],
            Literal["PackageLabel_Letter_6"],
            Literal["PackageLabel_Letter_6_CarrierLeft"],
            Literal["PackageLabel_A4_2"],
            Literal["PackageLabel_A4_4"],
            Literal["PackageLabel_Plain_Paper"],
            Literal["PackageLabel_Plain_Paper_CarrierBottom"],
            Literal["PackageLabel_Thermal"],
            Literal["PackageLabel_Thermal_Unified"],
            Literal["PackageLabel_Thermal_NonPCP"],
            Literal["PackageLabel_Thermal_No_Carrier_Rotation"],
        ],
        label_type: Union[Literal["BARCODE_2D"], Literal["UNIQUE"], Literal["PALLET"]],
        number_of_packages: int = None,
        package_labels_to_print: list[str] = None,
        number_of_pallets: int = None,
        page_size: int = None,
        page_start_index: int = None,
    ):
        """
        Returns package/pallet labels for faster and more accurate shipment processing at the Amazon fulfillment center.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            page_type: The page type to use to print the labels. Submitting a PageType value that is not supported in your marketplace returns an error.
            label_type: The type of labels requested.
            number_of_packages: The number of packages in the shipment.
            package_labels_to_print: A list of identifiers that specify packages for which you want package labels printed.
                Must match CartonId values previously passed using the FBA Inbound Shipment Carton Information Feed. If not, the operation returns the IncorrectPackageIdentifier error code.
            number_of_pallets: The number of pallets in the shipment. This returns four identical labels for each pallet.
            page_size: The page size for paginating through the total packages' labels. This is a required parameter for Non-Partnered LTL Shipments. Max value:1000.
            page_start_index: The page start index for paginating through the total packages' labels. This is a required parameter for Non-Partnered LTL Shipments.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/labels"
        values = (
            shipment_id,
            page_type,
            label_type,
            number_of_packages,
            package_labels_to_print,
            number_of_pallets,
            page_size,
            page_start_index,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_labels_params)
        return response

    _get_labels_params = (  # name, param in
        ("shipmentId", "path"),
        ("PageType", "query"),
        ("LabelType", "query"),
        ("NumberOfPackages", "query"),
        ("PackageLabelsToPrint", "query"),
        ("NumberOfPallets", "query"),
        ("PageSize", "query"),
        ("PageStartIndex", "query"),
    )

    def get_preorder_info(
        self,
        shipment_id: str,
        marketplace_id: str,
    ):
        """
        Returns pre-order information, including dates, that a seller needs before confirming a shipment for pre-order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            marketplace_id: A marketplace identifier. Specifies the marketplace the shipment is tied to.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/preorder"
        values = (
            shipment_id,
            marketplace_id,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_preorder_info_params)
        return response

    _get_preorder_info_params = (  # name, param in
        ("shipmentId", "path"),
        ("MarketplaceId", "query"),
    )

    def get_prep_instructions(
        self,
        ship_to_country_code: str,
        seller_skulist: list[str] = None,
        asinlist: list[str] = None,
    ):
        """
        Returns labeling requirements and item preparation instructions to help prepare items for shipment to Amazon's fulfillment network.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            ship_to_country_code: The country code of the country to which the items will be shipped. Note that labeling requirements and item preparation instructions can vary by country.
            seller_skulist: A list of SellerSKU values. Used to identify items for which you want labeling requirements and item preparation instructions for shipment to Amazon's fulfillment network. The SellerSKU is qualified by the Seller ID, which is included with every call to the Seller Partner API.
                Note: Include seller SKUs that you have used to list items on Amazon's retail website. If you include a seller SKU that you have never used to list an item on Amazon's retail website, the seller SKU is returned in the InvalidSKUList property in the response.
            asinlist: A list of ASIN values. Used to identify items for which you want item preparation instructions to help with item sourcing decisions.
                Note: ASINs must be included in the product catalog for at least one of the marketplaces that the seller  participates in. Any ASIN that is not included in the product catalog for at least one of the marketplaces that the seller participates in is returned in the InvalidASINList property in the response. You can find out which marketplaces a seller participates in by calling the getMarketplaceParticipations operation in the Selling Partner API for Sellers.
        """
        url = "/fba/inbound/v0/prepInstructions"
        values = (
            ship_to_country_code,
            seller_skulist,
            asinlist,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_prep_instructions_params)
        return response

    _get_prep_instructions_params = (  # name, param in
        ("ShipToCountryCode", "query"),
        ("SellerSKUList", "query"),
        ("ASINList", "query"),
    )

    def get_shipment_items(
        self,
        query_type: Union[Literal["DATE_RANGE"], Literal["NEXT_TOKEN"]],
        marketplace_id: str,
        last_updated_after: str = None,
        last_updated_before: str = None,
        next_token: str = None,
    ):
        """
        Returns a list of items in a specified inbound shipment, or a list of items that were updated within a specified time frame.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            last_updated_after: A date used for selecting inbound shipment items that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            last_updated_before: A date used for selecting inbound shipment items that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            query_type: Indicates whether items are returned using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or using NextToken, which continues returning items specified in a previous request.
            next_token: A string token returned in the response to your previous request.
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        url = "/fba/inbound/v0/shipmentItems"
        values = (
            last_updated_after,
            last_updated_before,
            query_type,
            next_token,
            marketplace_id,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_shipment_items_params)
        return response

    _get_shipment_items_params = (  # name, param in
        ("LastUpdatedAfter", "query"),
        ("LastUpdatedBefore", "query"),
        ("QueryType", "query"),
        ("NextToken", "query"),
        ("MarketplaceId", "query"),
    )

    def get_shipment_items_by_shipment_id(
        self,
        shipment_id: str,
        marketplace_id: str,
    ):
        """
        Returns a list of items in a specified inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier used for selecting items in a specific inbound shipment.
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/items"
        values = (
            shipment_id,
            marketplace_id,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_shipment_items_by_shipment_id_params)
        return response

    _get_shipment_items_by_shipment_id_params = (  # name, param in
        ("shipmentId", "path"),
        ("MarketplaceId", "query"),
    )

    def get_shipments(
        self,
        query_type: Union[Literal["SHIPMENT"], Literal["DATE_RANGE"], Literal["NEXT_TOKEN"]],
        marketplace_id: str,
        shipment_status_list: list[
            Union[
                Literal["WORKING"],
                Literal["SHIPPED"],
                Literal["RECEIVING"],
                Literal["CANCELLED"],
                Literal["DELETED"],
                Literal["CLOSED"],
                Literal["ERROR"],
                Literal["IN_TRANSIT"],
                Literal["DELIVERED"],
                Literal["CHECKED_IN"],
            ]
        ] = None,
        shipment_id_list: list[str] = None,
        last_updated_after: str = None,
        last_updated_before: str = None,
        next_token: str = None,
    ):
        """
        Returns a list of inbound shipments based on criteria that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_status_list: A list of ShipmentStatus values. Used to select shipments with a current status that matches the status values that you specify.
            shipment_id_list: A list of shipment IDs used to select the shipments that you want. If both ShipmentStatusList and ShipmentIdList are specified, only shipments that match both parameters are returned.
            last_updated_after: A date used for selecting inbound shipments that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            last_updated_before: A date used for selecting inbound shipments that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            query_type: Indicates whether shipments are returned using shipment information (by providing the ShipmentStatusList or ShipmentIdList parameters), using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or by using NextToken to continue returning items specified in a previous request.
            next_token: A string token returned in the response to your previous request.
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        url = "/fba/inbound/v0/shipments"
        values = (
            shipment_status_list,
            shipment_id_list,
            last_updated_after,
            last_updated_before,
            query_type,
            next_token,
            marketplace_id,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_shipments_params)
        return response

    _get_shipments_params = (  # name, param in
        ("ShipmentStatusList", "query"),
        ("ShipmentIdList", "query"),
        ("LastUpdatedAfter", "query"),
        ("LastUpdatedBefore", "query"),
        ("QueryType", "query"),
        ("NextToken", "query"),
        ("MarketplaceId", "query"),
    )

    def get_transport_details(
        self,
        shipment_id: str,
    ):
        """
        Returns current transportation information about an inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_transport_details_params)
        return response

    _get_transport_details_params = (("shipmentId", "path"),)  # name, param in

    def put_transport_details(
        self,
        shipment_id: str,
        is_partnered: bool,
        shipment_type: Union[Literal["SP"], Literal["LTL"]],
        transport_details: dict[str, Any],
    ):
        """
        Sends transportation information to Amazon about an inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            is_partnered: Indicates whether a putTransportDetails request is for an Amazon-partnered carrier.
            shipment_type: Specifies the carrier shipment type in a putTransportDetails request.
            transport_details: Information required to create an Amazon-partnered carrier shipping estimate, or to alert the Amazon fulfillment center to the arrival of an inbound shipment by a non-Amazon-partnered carrier.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport"
        values = (
            shipment_id,
            is_partnered,
            shipment_type,
            transport_details,
        )
        response = self._parse_args_and_request(url, "PUT", values, self._put_transport_details_params)
        return response

    _put_transport_details_params = (  # name, param in
        ("shipmentId", "path"),
        ("IsPartnered", "body"),
        ("ShipmentType", "body"),
        ("TransportDetails", "body"),
    )

    def update_inbound_shipment(
        self,
        shipment_id: str,
        inbound_shipment_header: dict[str, Any],
        inbound_shipment_items: list["InboundShipmentItem"],
        marketplace_id: str,
    ):
        """
        Updates or removes items from the inbound shipment identified by the specified shipment identifier. Adding new items is not supported.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            inbound_shipment_header: Inbound shipment information used to create and update inbound shipments.
            inbound_shipment_items: A list of inbound shipment item information.
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}"
        values = (
            shipment_id,
            inbound_shipment_header,
            inbound_shipment_items,
            marketplace_id,
        )
        response = self._parse_args_and_request(url, "PUT", values, self._update_inbound_shipment_params)
        return response

    _update_inbound_shipment_params = (  # name, param in
        ("shipmentId", "path"),
        ("InboundShipmentHeader", "body"),
        ("InboundShipmentItems", "body"),
        ("MarketplaceId", "body"),
    )

    def void_transport(
        self,
        shipment_id: str,
    ):
        """
        Cancels a previously-confirmed request to ship an inbound shipment using an Amazon-partnered carrier.

        To be successful, you must call this operation before the VoidDeadline date that is returned by the getTransportDetails operation.

        Important: The VoidDeadline date is 24 hours after you confirm a Small Parcel shipment transportation request or one hour after you confirm a Less Than Truckload/Full Truckload (LTL/FTL) shipment transportation request. After the void deadline passes, your account will be charged for the shipping cost.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/void"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "POST", values, self._void_transport_params)
        return response

    _void_transport_params = (("shipmentId", "path"),)  # name, param in
