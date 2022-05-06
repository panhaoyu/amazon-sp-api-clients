"""
Selling Partner API for Notifications
=============================================================================================

The Selling Partner API for Notifications lets you subscribe to notifications that are relevant to a selling partner's business. Using this API you can create a destination to receive notifications, subscribe to notifications, delete notification subscriptions, and more.

For more information, see the [Notifications Use Case Guide](doc:notifications-api-v1-use-case-guide)
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class CreateDestinationRequest:
    """
    The request schema for the createDestination operation.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    A developer-defined name to help identify this destination.
    """

    resource_specification: "DestinationResourceSpecification" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CreateDestinationResponse:
    """
    The response schema for the createDestination operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Destination" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CreateSubscriptionRequest:
    """
    The request schema for the createSubscription operation.
    """

    destination_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the destination where notifications will be delivered.
    """

    payload_version: str = attrs.field(
        kw_only=True,
    )
    """
    The version of the payload object to be used in the notification.
    """


@attrs.define
class CreateSubscriptionResponse:
    """
    The response schema for the createSubscription operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Subscription" = attrs.field(
        kw_only=True,
    )


@attrs.define
class DeleteDestinationResponse:
    """
    The response schema for the deleteDestination operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class DeleteSubscriptionByIdResponse:
    """
    The response schema for the deleteSubscriptionById operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Destination:
    """
    Represents a destination created when you call the createDestination operation.
    """

    destination_id: str = attrs.field(
        kw_only=True,
    )
    """
    The destination identifier generated when you created the destination.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The developer-defined name for this destination.

    Extra fields:
    {'maxLength': 256}
    """

    resource: "DestinationResource" = attrs.field(
        kw_only=True,
    )


@attrs.define
class DestinationList:
    """
    A list of destinations.
    """

    pass


@attrs.define
class DestinationResource:
    """
    The destination resource types.
    """

    event_bridge: "EventBridgeResource" = attrs.field(
        kw_only=True,
    )

    sqs: "SqsResource" = attrs.field(
        kw_only=True,
    )


@attrs.define
class DestinationResourceSpecification:
    """
    The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination.
    """

    event_bridge: "EventBridgeResourceSpecification" = attrs.field(
        kw_only=True,
    )

    sqs: "SqsResource" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Error:
    """
    Error response returned when the request is unsuccessful.
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
class EventBridgeResource:
    """
    Represents an Amazon EventBridge destination.
    """

    account_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the AWS account that is responsible for charges related to receiving notifications.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the partner event source associated with the destination.

    Extra fields:
    {'maxLength': 256}
    """

    region: str = attrs.field(
        kw_only=True,
    )
    """
    The AWS region in which you receive the notifications. For AWS regions that are supported in Amazon EventBridge, see https://docs.aws.amazon.com/general/latest/gr/ev.html.
    """


@attrs.define
class EventBridgeResourceSpecification:
    """
    The information required to create an Amazon EventBridge destination.
    """

    account_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the AWS account that is responsible for charges related to receiving notifications.
    """

    region: str = attrs.field(
        kw_only=True,
    )
    """
    The AWS region in which you will be receiving the notifications.
    """


@attrs.define
class GetDestinationResponse:
    """
    The response schema for the getDestination operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Destination" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetDestinationsResponse:
    """
    The response schema for the getDestinations operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "DestinationList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetSubscriptionByIdResponse:
    """
    The response schema for the getSubscriptionById operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Subscription" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetSubscriptionResponse:
    """
    The response schema for the getSubscription operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Subscription" = attrs.field(
        kw_only=True,
    )


@attrs.define
class SqsResource:
    """
    The information required to create an Amazon Simple Queue Service (Amazon SQS) queue destination.
    """

    arn: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Resource Name (ARN) associated with the SQS queue.

    Extra fields:
    {'maxLength': 1000, 'pattern': '^arn:aws:sqs:\\S+:\\S+:\\S+'}
    """


@attrs.define
class Subscription:
    """
    Represents a subscription to receive notifications.
    """

    destination_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the destination where notifications will be delivered.
    """

    payload_version: str = attrs.field(
        kw_only=True,
    )
    """
    The version of the payload object to be used in the notification.
    """

    subscription_id: str = attrs.field(
        kw_only=True,
    )
    """
    The subscription identifier generated when the subscription is created.
    """


class NotificationsV1Client(BaseClient):
    def create_destination(
        self,
        name: str,
        resource_specification: Dict[str, Any],
    ):
        """
        Creates a destination resource to receive notifications. The createDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            name: A developer-defined name to help identify this destination.
            resource_specification: The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination.
        """
        url = "/notifications/v1/destinations"
        values = (
            name,
            resource_specification,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_destination_params)
        return response

    _create_destination_params = (  # name, param in
        ("name", "body"),
        ("resourceSpecification", "body"),
    )

    def create_subscription(
        self,
        notification_type: str,
        destination_id: str = None,
        payload_version: str = None,
    ):
        """
        Creates a subscription for the specified notification type to be delivered to the specified destination. Before you can subscribe, you must first create the destination by calling the createDestination operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            notification_type: The type of notification.
                For more information about notification types, see [the Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
            destination_id: The identifier for the destination where notifications will be delivered.
            payload_version: The version of the payload object to be used in the notification.
        """
        url = "/notifications/v1/subscriptions/{notificationType}"
        values = (
            notification_type,
            destination_id,
            payload_version,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_subscription_params)
        return response

    _create_subscription_params = (  # name, param in
        ("notificationType", "path"),
        ("destinationId", "body"),
        ("payloadVersion", "body"),
    )

    def delete_destination(
        self,
        destination_id: str,
    ):
        """
        Deletes the destination that you specify. The deleteDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            destination_id: The identifier for the destination that you want to delete.
        """
        url = "/notifications/v1/destinations/{destinationId}"
        values = (destination_id,)
        response = self._parse_args_and_request(url, "DELETE", values, self._delete_destination_params)
        return response

    _delete_destination_params = (("destinationId", "path"),)  # name, param in

    def delete_subscription_by_id(
        self,
        subscription_id: str,
        notification_type: str,
    ):
        """
        Deletes the subscription indicated by the subscription identifier and notification type that you specify. The subscription identifier can be for any subscription associated with your application. After you successfully call this operation, notifications will stop being sent for the associated subscription. The deleteSubscriptionById API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            subscription_id: The identifier for the subscription that you want to delete.
            notification_type: The type of notification.
                For more information about notification types, see [the Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        """
        url = "/notifications/v1/subscriptions/{notificationType}/{subscriptionId}"
        values = (
            subscription_id,
            notification_type,
        )
        response = self._parse_args_and_request(url, "DELETE", values, self._delete_subscription_by_id_params)
        return response

    _delete_subscription_by_id_params = (  # name, param in
        ("subscriptionId", "path"),
        ("notificationType", "path"),
    )

    def get_destination(
        self,
        destination_id: str,
    ):
        """
        Returns information about the destination that you specify. The getDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            destination_id: The identifier generated when you created the destination.
        """
        url = "/notifications/v1/destinations/{destinationId}"
        values = (destination_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_destination_params)
        return response

    _get_destination_params = (("destinationId", "path"),)  # name, param in

    def get_destinations(
        self,
    ):
        """
        Returns information about all destinations. The getDestinations API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/notifications/v1/destinations"
        values = ()
        response = self._parse_args_and_request(url, "GET", values, self._get_destinations_params)
        return response

    _get_destinations_params = ()  # name, param in

    def get_subscription(
        self,
        notification_type: str,
    ):
        """
        Returns information about subscriptions of the specified notification type. You can use this API to get subscription information when you do not have a subscription identifier.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            notification_type: The type of notification.
                For more information about notification types, see [the Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        """
        url = "/notifications/v1/subscriptions/{notificationType}"
        values = (notification_type,)
        response = self._parse_args_and_request(url, "GET", values, self._get_subscription_params)
        return response

    _get_subscription_params = (("notificationType", "path"),)  # name, param in

    def get_subscription_by_id(
        self,
        subscription_id: str,
        notification_type: str,
    ):
        """
        Returns information about a subscription for the specified notification type. The getSubscriptionById API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            subscription_id: The identifier for the subscription that you want to get.
            notification_type: The type of notification.
                For more information about notification types, see [the Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        """
        url = "/notifications/v1/subscriptions/{notificationType}/{subscriptionId}"
        values = (
            subscription_id,
            notification_type,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_subscription_by_id_params)
        return response

    _get_subscription_by_id_params = (  # name, param in
        ("subscriptionId", "path"),
        ("notificationType", "path"),
    )
