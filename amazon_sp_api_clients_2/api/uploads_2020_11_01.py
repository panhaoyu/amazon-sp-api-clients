"""
Selling Partner API for Uploads
=============================================================================================

The Uploads API lets you upload files that you can programmatically access using other Selling Partner APIs, such as the A+ Content API and the Messaging API.
API Version: 2020-11-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateUploadDestinationResponse:
    """
    The response schema for the createUploadDestination operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_upload_destination_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CreateUploadDestinationResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["UploadDestination"] = attrs.field(
        default=None,
    )
    """
    Information about an upload destination.
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
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class UploadDestination:
    """
    Information about an upload destination.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _upload_destination_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return UploadDestination(**data)

    headers: Optional["UploadDestinationHeaders"] = attrs.field(
        default=None,
    )
    """
    The headers to include in the upload request.
    """

    upload_destination_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The unique identifier for the upload destination.
    """

    url: Optional[str] = attrs.field(
        default=None,
    )
    """
    The URL for the upload destination.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class UploadDestinationHeaders:
    """
    The headers to include in the upload request.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _upload_destination_headers_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return UploadDestinationHeaders(**data)

    pass


_create_upload_destination_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_upload_destination_name_convert = {
    "headers": "headers",
    "uploadDestinationId": "upload_destination_id",
    "url": "url",
}

_upload_destination_headers_name_convert = {}


class Uploads20201101Client(BaseClient):
    def create_upload_destination_for_resource(
        self,
        marketplace_ids: List[str],
        content_md5: str,
        resource: str,
        content_type: str = None,
    ) -> Union[CreateUploadDestinationResponse]:
        """
        Creates an upload destination, returning the information required to upload a file to the destination and to programmatically access the file.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | .1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_ids: A list of marketplace identifiers. This specifies the marketplaces where the upload will be available. Only one marketplace can be specified.
            content_md5: An MD5 hash of the content to be submitted to the upload destination. This value is used to determine if the data has been corrupted or tampered with during transit.
            resource: The resource for the upload destination that you are creating. For example, if you are creating an upload destination for the createLegalDisclosure operation of the Messaging API, the {resource} would be /messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure, and the entire path would be /uploads/2020-11-01/uploadDestinations/messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure.
            content_type: The content type of the file to be uploaded.
        """
        url = "/uploads/2020-11-01/uploadDestinations/{resource}"
        values = (
            marketplace_ids,
            content_md5,
            resource,
            content_type,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_upload_destination_for_resource_params,
            self._create_upload_destination_for_resource_responses,
        )
        return response

    _create_upload_destination_for_resource_params = (  # name, param in
        ("marketplaceIds", "query"),
        ("contentMD5", "query"),
        ("resource", "path"),
        ("contentType", "query"),
    )

    _create_upload_destination_for_resource_responses = {
        201: CreateUploadDestinationResponse,
        400: CreateUploadDestinationResponse,
        403: CreateUploadDestinationResponse,
        404: CreateUploadDestinationResponse,
        413: CreateUploadDestinationResponse,
        415: CreateUploadDestinationResponse,
        429: CreateUploadDestinationResponse,
        500: CreateUploadDestinationResponse,
        503: CreateUploadDestinationResponse,
    }
