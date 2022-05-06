"""
Selling Partner API for Feeds
=============================================================================================

The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.
API Version: 2020-09-04
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class CancelFeedResponse:
    """
    Response schema.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CreateFeedDocumentResponse:
    """
    The response for the createFeedDocument operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "CreateFeedDocumentResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CreateFeedDocumentResult:
    """
    Information required to encrypt and upload a feed document's contents.
    """

    feed_document_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier of the feed document.
    """

    url: str = attrs.field(
        kw_only=True,
    )
    """
    The presigned URL for uploading the feed contents. This URL expires after 5 minutes.
    """

    encryption_details: "FeedDocumentEncryptionDetails" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CreateFeedDocumentSpecification:

    content_type: str = attrs.field(
        kw_only=True,
    )
    """
    The content type of the feed.
    """


@attrs.define
class CreateFeedResponse:
    """
    Response schema.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "CreateFeedResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CreateFeedResult:

    feed_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the feed. This identifier is unique only in combination with a seller ID.
    """


@attrs.define
class CreateFeedSpecification:

    feed_type: str = attrs.field(
        kw_only=True,
    )
    """
    The feed type.
    """

    input_feed_document_id: str = attrs.field(
        kw_only=True,
    )
    """
    The document identifier returned by the createFeedDocument operation. Encrypt and upload the feed document contents before calling the createFeed operation.
    """

    marketplace_ids: List[str] = attrs.field(
        kw_only=True,
    )
    """
    A list of identifiers for marketplaces that you want the feed to be applied to.

    Extra fields:
    {'maxItems': 25, 'minItems': 1}
    """

    feed_options: "FeedOptions" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Error:
    """
    An error response returned when the request is unsuccessful.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
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


@attrs.define
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class Feed:

    created_time: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date and time when the feed was created, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    feed_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the feed. This identifier is unique only in combination with a seller ID.
    """

    feed_type: str = attrs.field(
        kw_only=True,
    )
    """
    The feed type.
    """

    marketplace_ids: List[str] = attrs.field(
        kw_only=True,
    )
    """
    A list of identifiers for the marketplaces that the feed is applied to.
    """

    processing_end_time: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date and time when feed processing completed, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    processing_start_time: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date and time when feed processing started, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    processing_status: Union[
        Literal["CANCELLED"], Literal["DONE"], Literal["FATAL"], Literal["IN_PROGRESS"], Literal["IN_QUEUE"]
    ] = attrs.field(
        kw_only=True,
    )
    """
    The processing status of the feed.
    """

    result_feed_document_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the feed document. This identifier is unique only in combination with a seller ID.
    """


@attrs.define
class FeedDocument:

    compression_algorithm: Union[Literal["GZIP"]] = attrs.field(
        kw_only=True,
    )
    """
    If present, the feed document contents are compressed using the indicated algorithm.
    """

    feed_document_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the feed document. This identifier is unique only in combination with a seller ID.
    """

    url: str = attrs.field(
        kw_only=True,
    )
    """
    A presigned URL for the feed document. This URL expires after 5 minutes.
    """

    encryption_details: "FeedDocumentEncryptionDetails" = attrs.field(
        kw_only=True,
    )


@attrs.define
class FeedDocumentEncryptionDetails:
    """
    Encryption details for required client-side encryption and decryption of document contents.
    """

    initialization_vector: str = attrs.field(
        kw_only=True,
    )
    """
    The vector to encrypt or decrypt the document contents using Cipher Block Chaining (CBC).
    """

    key: str = attrs.field(
        kw_only=True,
    )
    """
    The encryption key used to encrypt or decrypt the document contents.
    """

    standard: Union[Literal["AES"]] = attrs.field(
        kw_only=True,
    )
    """
    The encryption standard required to encrypt or decrypt the document contents.
    """


@attrs.define
class FeedList:

    pass


@attrs.define
class FeedOptions:
    """
    Additional options to control the feed. For feeds that use the feedOptions parameter, you can find the parameter values in the feed description in [feedType values](doc:feed-type-values).
    """

    pass


@attrs.define
class GetFeedDocumentResponse:
    """
    Response schema.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "FeedDocument" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetFeedResponse:
    """
    Response schema.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Feed" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetFeedsResponse:
    """
    Response schema.
    """

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    Returned when the number of results exceeds pageSize. To get the next page of results, call the getFeeds operation with this token as the only parameter.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "FeedList" = attrs.field(
        kw_only=True,
    )


class Feeds20200904Client(BaseClient):
    def cancel_feed(
        self,
        feed_id: str,
    ):
        """
        Cancels the feed that you specify. Only feeds with processingStatus=IN_QUEUE can be cancelled. Cancelled feeds are returned in subsequent calls to the getFeed and getFeeds operations.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_id: The identifier for the feed. This identifier is unique only in combination with a seller ID.
        """
        url = "/feeds/2020-09-04/feeds/{feedId}"
        values = (feed_id,)
        response = self._parse_args_and_request(url, "DELETE", values, self._cancel_feed_params)
        return response

    _cancel_feed_params = (("feedId", "path"),)  # name, param in

    def create_feed(
        self,
        feed_type: str,
        input_feed_document_id: str,
        marketplace_ids: List[str],
        feed_options: Dict[str, Any] = None,
    ):
        """
        Creates a feed. Encrypt and upload the contents of the feed document before calling this operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_options: Additional options to control the feed. For feeds that use the feedOptions parameter, you can find the parameter values in the feed description in [feedType values](doc:feed-type-values).
            feed_type: The feed type.
            input_feed_document_id: The document identifier returned by the createFeedDocument operation. Encrypt and upload the feed document contents before calling the createFeed operation.
            marketplace_ids: A list of identifiers for marketplaces that you want the feed to be applied to.
        """
        url = "/feeds/2020-09-04/feeds"
        values = (
            feed_options,
            feed_type,
            input_feed_document_id,
            marketplace_ids,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_feed_params)
        return response

    _create_feed_params = (  # name, param in
        ("feedOptions", "body"),
        ("feedType", "body"),
        ("inputFeedDocumentId", "body"),
        ("marketplaceIds", "body"),
    )

    def create_feed_document(
        self,
        content_type: str,
    ):
        """
        Creates a feed document for the feed type that you specify. This operation returns encryption details for encrypting the contents of the document, as well as a presigned URL for uploading the encrypted feed document contents. It also returns a feedDocumentId value that you can pass in with a subsequent call to the createFeed operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_type: The content type of the feed.
        """
        url = "/feeds/2020-09-04/documents"
        values = (content_type,)
        response = self._parse_args_and_request(url, "POST", values, self._create_feed_document_params)
        return response

    _create_feed_document_params = (("contentType", "body"),)  # name, param in

    def get_feed(
        self,
        feed_id: str,
    ):
        """
        Returns feed details (including the resultDocumentId, if available) for the feed that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2.0 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_id: The identifier for the feed. This identifier is unique only in combination with a seller ID.
        """
        url = "/feeds/2020-09-04/feeds/{feedId}"
        values = (feed_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_feed_params)
        return response

    _get_feed_params = (("feedId", "path"),)  # name, param in

    def get_feed_document(
        self,
        feed_document_id: str,
    ):
        """
        Returns the information required for retrieving a feed document's contents. This includes a presigned URL for the feed document as well as the information required to decrypt the document's contents.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_document_id: The identifier of the feed document.
        """
        url = "/feeds/2020-09-04/documents/{feedDocumentId}"
        values = (feed_document_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_feed_document_params)
        return response

    _get_feed_document_params = (("feedDocumentId", "path"),)  # name, param in

    def get_feeds(
        self,
        feed_types: List[str] = None,
        marketplace_ids: List[str] = None,
        page_size: int = None,
        processing_statuses: List[
            Union[Literal["CANCELLED"], Literal["DONE"], Literal["FATAL"], Literal["IN_PROGRESS"], Literal["IN_QUEUE"]]
        ] = None,
        created_since: datetime = None,
        created_until: datetime = None,
        next_token: str = None,
    ):
        """
        Returns feed details for the feeds that match the filters that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_types: A list of feed types used to filter feeds. When feedTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either feedTypes or nextToken is required.
            marketplace_ids: A list of marketplace identifiers used to filter feeds. The feeds returned will match at least one of the marketplaces that you specify.
            page_size: The maximum number of feeds to return in a single call.
            processing_statuses: A list of processing statuses used to filter feeds.
            created_since: The earliest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is 90 days ago. Feeds are retained for a maximum of 90 days.
            created_until: The latest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is now.
            next_token: A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getFeeds operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.
        """
        url = "/feeds/2020-09-04/feeds"
        values = (
            feed_types,
            marketplace_ids,
            page_size,
            processing_statuses,
            created_since,
            created_until,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_feeds_params)
        return response

    _get_feeds_params = (  # name, param in
        ("feedTypes", "query"),
        ("marketplaceIds", "query"),
        ("pageSize", "query"),
        ("processingStatuses", "query"),
        ("createdSince", "query"),
        ("createdUntil", "query"),
        ("nextToken", "query"),
    )
