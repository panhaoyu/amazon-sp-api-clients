"""
Selling Partner API for A+ Content Management
=============================================================================================

With the A+ Content API, you can build applications that help selling partners add rich marketing content to their Amazon product detail pages. A+ content helps selling partners share their brand and product story, which helps buyers make informed purchasing decisions. Selling partners assemble content by choosing from content modules and adding images and text.
API Version: 2020-11-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class AplusPaginatedResponse:

    pass


@attrs.define
class AplusResponse:

    warnings: list[dict[str, Any]]
    # {'ref': '#/components/schemas/MessageSet', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class Asin:

    pass


@attrs.define
class AsinBadge:

    pass


@attrs.define
class AsinBadgeSet:

    pass


@attrs.define
class AsinMetadata:

    image_url: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1}
    title: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1}

    asin: str
    # {'ref': '#/components/schemas/Asin', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    badge_set: list[
        Union[
            Literal["BRAND_NOT_ELIGIBLE"],
            Literal["CATALOG_NOT_FOUND"],
            Literal["CONTENT_NOT_PUBLISHED"],
            Literal["CONTENT_PUBLISHED"],
        ]
    ]
    # {'ref': '#/components/schemas/AsinBadgeSet', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    content_reference_key_set: list[str]
    # {'ref': '#/components/schemas/ContentReferenceKeySet', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    parent: str
    # {'ref': '#/components/schemas/Asin', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class AsinMetadataSet:

    pass


@attrs.define
class AsinSet:

    pass


@attrs.define
class ColorType:

    pass


@attrs.define
class ContentBadge:

    pass


@attrs.define
class ContentBadgeSet:

    pass


@attrs.define
class ContentDocument:

    name: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1, 'maxLength': 100}

    content_module_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ContentModuleList', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    content_sub_type: str
    # {'ref': '#/components/schemas/ContentSubType', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    content_type: Union[Literal["EBC"], Literal["EMC"]]
    # {'ref': '#/components/schemas/ContentType', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    locale: str
    # {'ref': '#/components/schemas/LanguageTag', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class ContentMetadata:

    name: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1, 'maxLength': 100}
    update_time: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string'}

    badge_set: list[
        Union[Literal["BULK"], Literal["GENERATED"], Literal["LAUNCHPAD"], Literal["PREMIUM"], Literal["STANDARD"]]
    ]
    # {'ref': '#/components/schemas/ContentBadgeSet', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    marketplace_id: str
    # {'ref': '#/components/schemas/MarketplaceId', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    status: Union[Literal["APPROVED"], Literal["DRAFT"], Literal["REJECTED"], Literal["SUBMITTED"]]
    # {'ref': '#/components/schemas/ContentStatus', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class ContentMetadataRecord:

    content_metadata: dict[str, Any]
    # {'ref': '#/components/schemas/ContentMetadata', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    content_reference_key: str
    # {'ref': '#/components/schemas/ContentReferenceKey', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class ContentMetadataRecordList:

    pass


@attrs.define
class ContentModule:

    content_module_type: Union[
        Literal["STANDARD_COMPANY_LOGO"],
        Literal["STANDARD_COMPARISON_TABLE"],
        Literal["STANDARD_FOUR_IMAGE_TEXT"],
        Literal["STANDARD_FOUR_IMAGE_TEXT_QUADRANT"],
        Literal["STANDARD_HEADER_IMAGE_TEXT"],
        Literal["STANDARD_IMAGE_SIDEBAR"],
        Literal["STANDARD_IMAGE_TEXT_OVERLAY"],
        Literal["STANDARD_MULTIPLE_IMAGE_TEXT"],
        Literal["STANDARD_PRODUCT_DESCRIPTION"],
        Literal["STANDARD_SINGLE_IMAGE_HIGHLIGHTS"],
        Literal["STANDARD_SINGLE_IMAGE_SPECS_DETAIL"],
        Literal["STANDARD_SINGLE_SIDE_IMAGE"],
        Literal["STANDARD_TECH_SPECS"],
        Literal["STANDARD_TEXT"],
        Literal["STANDARD_THREE_IMAGE_TEXT"],
    ]
    # {'ref': '#/components/schemas/ContentModuleType', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_company_logo: dict[str, Any]
    # {'ref': '#/components/schemas/StandardCompanyLogoModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_comparison_table: dict[str, Any]
    # {'ref': '#/components/schemas/StandardComparisonTableModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_four_image_text: dict[str, Any]
    # {'ref': '#/components/schemas/StandardFourImageTextModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_four_image_text_quadrant: dict[str, Any]
    # {'ref': '#/components/schemas/StandardFourImageTextQuadrantModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_header_image_text: dict[str, Any]
    # {'ref': '#/components/schemas/StandardHeaderImageTextModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_image_sidebar: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageSidebarModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_image_text_overlay: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextOverlayModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_multiple_image_text: dict[str, Any]
    # {'ref': '#/components/schemas/StandardMultipleImageTextModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_product_description: dict[str, Any]
    # {'ref': '#/components/schemas/StandardProductDescriptionModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_single_image_highlights: dict[str, Any]
    # {'ref': '#/components/schemas/StandardSingleImageHighlightsModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_single_image_specs_detail: dict[str, Any]
    # {'ref': '#/components/schemas/StandardSingleImageSpecsDetailModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_single_side_image: dict[str, Any]
    # {'ref': '#/components/schemas/StandardSingleSideImageModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_tech_specs: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTechSpecsModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_text: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    standard_three_image_text: dict[str, Any]
    # {'ref': '#/components/schemas/StandardThreeImageTextModule', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class ContentModuleList:

    pass


@attrs.define
class ContentModuleType:

    pass


@attrs.define
class ContentRecord:

    content_document: dict[str, Any]
    # {'ref': '#/components/schemas/ContentDocument', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    content_metadata: dict[str, Any]
    # {'ref': '#/components/schemas/ContentMetadata', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    content_reference_key: str
    # {'ref': '#/components/schemas/ContentReferenceKey', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class ContentReferenceKey:

    pass


@attrs.define
class ContentReferenceKeySet:

    pass


@attrs.define
class ContentStatus:

    pass


@attrs.define
class ContentSubType:

    pass


@attrs.define
class ContentType:

    pass


@attrs.define
class Decorator:

    depth: int
    # {'maximum': 100.0, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'integer', 'minimum': 0.0}
    length: int
    # {'maximum': 10000.0, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'integer', 'minimum': 0.0}
    offset: int
    # {'maximum': 10000.0, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'integer', 'minimum': 0.0}

    type: Union[
        Literal["LIST_ITEM"],
        Literal["LIST_ORDERED"],
        Literal["LIST_UNORDERED"],
        Literal["STYLE_BOLD"],
        Literal["STYLE_ITALIC"],
        Literal["STYLE_LINEBREAK"],
        Literal["STYLE_PARAGRAPH"],
        Literal["STYLE_UNDERLINE"],
    ]
    # {'ref': '#/components/schemas/DecoratorType', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class DecoratorSet:

    pass


@attrs.define
class DecoratorType:

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/Error'), 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'array'}

    pass


@attrs.define
class GetContentDocumentResponse:

    pass


@attrs.define
class ImageComponent:

    alt_text: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1, 'maxLength': 100}
    upload_destination_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1}

    image_crop_specification: dict[str, Any]
    # {'ref': '#/components/schemas/ImageCropSpecification', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class ImageCropSpecification:

    offset: dict[str, Any]
    # {'ref': '#/components/schemas/ImageOffsets', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    size: dict[str, Any]
    # {'ref': '#/components/schemas/ImageDimensions', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class ImageDimensions:

    height: dict[str, Any]
    # {'ref': '#/components/schemas/IntegerWithUnits', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    width: dict[str, Any]
    # {'ref': '#/components/schemas/IntegerWithUnits', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class ImageOffsets:

    x: dict[str, Any]
    # {'ref': '#/components/schemas/IntegerWithUnits', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    y: dict[str, Any]
    # {'ref': '#/components/schemas/IntegerWithUnits', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class IntegerWithUnits:

    units: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string'}
    value: int
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'integer'}

    pass


@attrs.define
class LanguageTag:

    pass


@attrs.define
class ListContentDocumentAsinRelationsResponse:

    pass


@attrs.define
class MarketplaceId:

    pass


@attrs.define
class MessageSet:

    pass


@attrs.define
class PageToken:

    pass


@attrs.define
class ParagraphComponent:

    text_list: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/TextComponent'), 'maxItems': 100, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'minItems': 1, 'type': 'array'}

    pass


@attrs.define
class PlainTextItem:

    position: int
    # {'maximum': 100.0, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'integer', 'minimum': 1.0}
    value: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1, 'maxLength': 250}

    pass


@attrs.define
class PositionType:

    pass


@attrs.define
class PostContentDocumentApprovalSubmissionResponse:

    pass


@attrs.define
class PostContentDocumentAsinRelationsRequest:

    asin_set: list[str]
    # {'ref': '#/components/schemas/AsinSet', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class PostContentDocumentAsinRelationsResponse:

    pass


@attrs.define
class PostContentDocumentRequest:

    content_document: dict[str, Any]
    # {'ref': '#/components/schemas/ContentDocument', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class PostContentDocumentResponse:

    pass


@attrs.define
class PostContentDocumentSuspendSubmissionResponse:

    pass


@attrs.define
class PublishRecord:

    asin: str
    # {'ref': '#/components/schemas/Asin', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    content_reference_key: str
    # {'ref': '#/components/schemas/ContentReferenceKey', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    content_sub_type: str
    # {'ref': '#/components/schemas/ContentSubType', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    content_type: Union[Literal["EBC"], Literal["EMC"]]
    # {'ref': '#/components/schemas/ContentType', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    locale: str
    # {'ref': '#/components/schemas/LanguageTag', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    marketplace_id: str
    # {'ref': '#/components/schemas/MarketplaceId', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class PublishRecordList:

    pass


@attrs.define
class SearchContentDocumentsResponse:

    pass


@attrs.define
class SearchContentPublishRecordsResponse:

    pass


@attrs.define
class StandardCompanyLogoModule:

    company_logo: dict[str, Any]
    # {'ref': '#/components/schemas/ImageComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardComparisonProductBlock:

    highlight: bool
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'boolean'}
    metrics: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/PlainTextItem'), 'maxItems': 10, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'minItems': 0, 'type': 'array'}
    position: int
    # {'maximum': 6.0, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'integer', 'minimum': 1.0}
    title: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1, 'maxLength': 80}

    asin: str
    # {'ref': '#/components/schemas/Asin', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    image: dict[str, Any]
    # {'ref': '#/components/schemas/ImageComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardComparisonTableModule:

    metric_row_labels: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/PlainTextItem'), 'maxItems': 10, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'minItems': 0, 'type': 'array'}
    product_columns: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/StandardComparisonProductBlock'), 'maxItems': 6, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'minItems': 0, 'type': 'array'}

    pass


@attrs.define
class StandardFourImageTextModule:

    block1: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    block2: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    block3: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    block4: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardFourImageTextQuadrantModule:

    block1: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    block2: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    block3: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    block4: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardHeaderImageTextModule:

    block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardHeaderTextListBlock:

    block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextListBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardImageCaptionBlock:

    caption: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    image: dict[str, Any]
    # {'ref': '#/components/schemas/ImageComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardImageSidebarModule:

    description_list_block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextListBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    description_text_block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    image_caption_block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageCaptionBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    sidebar_image_text_block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    sidebar_list_block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextListBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardImageTextBlock:

    body: dict[str, Any]
    # {'ref': '#/components/schemas/ParagraphComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    image: dict[str, Any]
    # {'ref': '#/components/schemas/ImageComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardImageTextCaptionBlock:

    block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    caption: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardImageTextOverlayModule:

    block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    overlay_color_type: Union[Literal["DARK"], Literal["LIGHT"]]
    # {'ref': '#/components/schemas/ColorType', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardMultipleImageTextModule:

    blocks: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/StandardImageTextCaptionBlock'), 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'array'}

    pass


@attrs.define
class StandardProductDescriptionModule:

    body: dict[str, Any]
    # {'ref': '#/components/schemas/ParagraphComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardSingleImageHighlightsModule:

    bulleted_list_block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardHeaderTextListBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    image: dict[str, Any]
    # {'ref': '#/components/schemas/ImageComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    text_block1: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    text_block2: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    text_block3: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardSingleImageSpecsDetailModule:

    description_block1: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    description_block2: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    description_headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    image: dict[str, Any]
    # {'ref': '#/components/schemas/ImageComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    specification_headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    specification_list_block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardHeaderTextListBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    specification_text_block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardSingleSideImageModule:

    block: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    image_position_type: Union[Literal["LEFT"], Literal["RIGHT"]]
    # {'ref': '#/components/schemas/PositionType', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardTechSpecsModule:

    specification_list: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/StandardTextPairBlock'), 'maxItems': 16, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'minItems': 4, 'type': 'array'}
    table_count: int
    # {'maximum': 2.0, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'integer', 'minimum': 1.0}

    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardTextBlock:

    body: dict[str, Any]
    # {'ref': '#/components/schemas/ParagraphComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardTextListBlock:

    text_list: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/TextItem'), 'maxItems': 8, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'minItems': 0, 'type': 'array'}

    pass


@attrs.define
class StandardTextModule:

    body: dict[str, Any]
    # {'ref': '#/components/schemas/ParagraphComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardTextPairBlock:

    description: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    label: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class StandardThreeImageTextModule:

    block1: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    block2: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    block3: dict[str, Any]
    # {'ref': '#/components/schemas/StandardImageTextBlock', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    headline: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class TextComponent:

    value: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'string', 'minLength': 1, 'maxLength': 10000}

    decorator_set: list[dict[str, Any]]
    # {'ref': '#/components/schemas/DecoratorSet', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class TextItem:

    position: int
    # {'maximum': 100.0, 'generator': <__mp_main__.Generator object at 0x000001FB33337310>, 'type': 'integer', 'minimum': 1.0}

    text: dict[str, Any]
    # {'ref': '#/components/schemas/TextComponent', 'generator': <__mp_main__.Generator object at 0x000001FB33337310>}
    pass


@attrs.define
class ValidateContentDocumentAsinRelationsResponse:

    pass


class AplusContent20201101Client(BaseClient):
    def create_content_document(
        self,
        marketplace_id: str,
        content_document: dict[str, Any],
    ):
        """
        Creates a new A+ Content document.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            content_document: The A+ Content document. This is the enhanced content that is published to product detail pages.
        """
        url = "/aplus/2020-11-01/contentDocuments"
        values = (
            marketplace_id,
            content_document,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_content_document_params)
        return response

    _create_content_document_params = (  # name, param in
        ("marketplaceId", "query"),
        ("contentDocument", "body"),
    )

    def get_content_document(
        self,
        content_reference_key: str,
        marketplace_id: str,
        included_data_set: list[Union[Literal["CONTENTS"], Literal["METADATA"]]],
    ):
        """
        Returns an A+ Content document, if available.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ Content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            included_data_set: The set of A+ Content data types to include in the response.
        """
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}"
        values = (
            content_reference_key,
            marketplace_id,
            included_data_set,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_content_document_params)
        return response

    _get_content_document_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("includedDataSet", "query"),
    )

    def list_content_document_asin_relations(
        self,
        content_reference_key: str,
        marketplace_id: str,
        included_data_set: list[Union[Literal["METADATA"]]] = None,
        asin_set: list[str] = None,
        page_token: str = None,
    ):
        """
        Returns a list of ASINs related to the specified A+ Content document, if available. If you do not include the asinSet parameter, the operation returns all ASINs related to the content document.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ Content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            included_data_set: The set of A+ Content data types to include in the response. If you do not include this parameter, the operation returns the related ASINs without metadata.
            asin_set: The set of ASINs.
            page_token: A page token from the nextPageToken response element returned by your previous call to this operation. nextPageToken is returned when the results of a call exceed the page size. To get the next page of results, call the operation and include pageToken as the only parameter. Specifying pageToken with any other parameter will cause the request to fail. When no nextPageToken value is returned there are no more pages to return. A pageToken value is not usable across different operations.
        """
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins"
        values = (
            content_reference_key,
            marketplace_id,
            included_data_set,
            asin_set,
            page_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._list_content_document_asin_relations_params)
        return response

    _list_content_document_asin_relations_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("includedDataSet", "query"),
        ("asinSet", "query"),
        ("pageToken", "query"),
    )

    def post_content_document_approval_submission(
        self,
        content_reference_key: str,
        marketplace_id: str,
    ):
        """
        Submits an A+ Content document for review, approval, and publishing.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
        """
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/approvalSubmissions"
        values = (
            content_reference_key,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url, "POST", values, self._post_content_document_approval_submission_params
        )
        return response

    _post_content_document_approval_submission_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
    )

    def post_content_document_asin_relations(
        self,
        content_reference_key: str,
        marketplace_id: str,
        asin_set: list[str],
    ):
        """
        Replaces all ASINs related to the specified A+ Content document, if available. This may add or remove ASINs, depending on the current set of related ASINs. Removing an ASIN has the side effect of suspending the content document from that ASIN.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            asin_set: The set of ASINs.
        """
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins"
        values = (
            content_reference_key,
            marketplace_id,
            asin_set,
        )
        response = self._parse_args_and_request(url, "POST", values, self._post_content_document_asin_relations_params)
        return response

    _post_content_document_asin_relations_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("asinSet", "body"),
    )

    def post_content_document_suspend_submission(
        self,
        content_reference_key: str,
        marketplace_id: str,
    ):
        """
        Submits a request to suspend visible A+ Content. This neither deletes the content document nor the ASIN relations.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
        """
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/suspendSubmissions"
        values = (
            content_reference_key,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url, "POST", values, self._post_content_document_suspend_submission_params
        )
        return response

    _post_content_document_suspend_submission_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
    )

    def search_content_documents(
        self,
        marketplace_id: str,
        page_token: str = None,
    ):
        """
        Returns a list of all A+ Content documents assigned to a selling partner. This operation returns only the metadata of the A+ Content documents. Call the getContentDocument operation to get the actual contents of the A+ Content documents.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            page_token: A page token from the nextPageToken response element returned by your previous call to this operation. nextPageToken is returned when the results of a call exceed the page size. To get the next page of results, call the operation and include pageToken as the only parameter. Specifying pageToken with any other parameter will cause the request to fail. When no nextPageToken value is returned there are no more pages to return. A pageToken value is not usable across different operations.
        """
        url = "/aplus/2020-11-01/contentDocuments"
        values = (
            marketplace_id,
            page_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._search_content_documents_params)
        return response

    _search_content_documents_params = (  # name, param in
        ("marketplaceId", "query"),
        ("pageToken", "query"),
    )

    def search_content_publish_records(
        self,
        marketplace_id: str,
        asin: str,
        page_token: str = None,
    ):
        """
        Searches for A+ Content publishing records, if available.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            asin: The Amazon Standard Identification Number (ASIN).
            page_token: A page token from the nextPageToken response element returned by your previous call to this operation. nextPageToken is returned when the results of a call exceed the page size. To get the next page of results, call the operation and include pageToken as the only parameter. Specifying pageToken with any other parameter will cause the request to fail. When no nextPageToken value is returned there are no more pages to return. A pageToken value is not usable across different operations.
        """
        url = "/aplus/2020-11-01/contentPublishRecords"
        values = (
            marketplace_id,
            asin,
            page_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._search_content_publish_records_params)
        return response

    _search_content_publish_records_params = (  # name, param in
        ("marketplaceId", "query"),
        ("asin", "query"),
        ("pageToken", "query"),
    )

    def update_content_document(
        self,
        content_reference_key: str,
        marketplace_id: str,
        content_document: dict[str, Any],
    ):
        """
        Updates an existing A+ Content document.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ Content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            content_document: The A+ Content document. This is the enhanced content that is published to product detail pages.
        """
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}"
        values = (
            content_reference_key,
            marketplace_id,
            content_document,
        )
        response = self._parse_args_and_request(url, "POST", values, self._update_content_document_params)
        return response

    _update_content_document_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("contentDocument", "body"),
    )

    def validate_content_document_asin_relations(
        self,
        marketplace_id: str,
        content_document: dict[str, Any],
        asin_set: list[str] = None,
    ):
        """
        Checks if the A+ Content document is valid for use on a set of ASINs.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            asin_set: The set of ASINs.
            content_document: The A+ Content document. This is the enhanced content that is published to product detail pages.
        """
        url = "/aplus/2020-11-01/contentAsinValidations"
        values = (
            marketplace_id,
            asin_set,
            content_document,
        )
        response = self._parse_args_and_request(
            url, "POST", values, self._validate_content_document_asin_relations_params
        )
        return response

    _validate_content_document_asin_relations_params = (  # name, param in
        ("marketplaceId", "query"),
        ("asinSet", "query"),
        ("contentDocument", "body"),
    )
