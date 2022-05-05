"""
Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data
=============================================================================================

The Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data provides programmatic access to vendor direct fulfillment sandbox test data.
API Version: 2021-10-28
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'items': Reference(ref='#/components/schemas/Error'), 'type': 'array'}

    pass


@attrs.define
class GenerateOrderScenarioRequest:

    orders: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'items': Reference(ref='#/components/schemas/OrderScenarioRequest'), 'type': 'array'}

    pass


@attrs.define
class OrderScenarioRequest:

    selling_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>}
    ship_from_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>}
    pass


@attrs.define
class Pagination:

    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'type': 'string'}

    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'type': 'string'}

    pass


@attrs.define
class Scenario:

    orders: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'items': Reference(ref='#/components/schemas/TestOrder'), 'type': 'array'}
    scenario_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'type': 'string'}

    pass


@attrs.define
class TestCaseData:

    scenarios: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'items': Reference(ref='#/components/schemas/Scenario'), 'type': 'array'}

    pass


@attrs.define
class TestOrder:

    order_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'type': 'string'}

    pass


@attrs.define
class Transaction:

    status: Union[Literal["FAILURE"], Literal["PROCESSING"], Literal["SUCCESS"]]
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'enum': ['FAILURE', 'PROCESSING', 'SUCCESS'], 'type': 'string'}
    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'type': 'string'}

    test_case_data: dict[str, Any]
    # {'ref': '#/components/schemas/TestCaseData', 'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>}
    pass


@attrs.define
class TransactionReference:

    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>, 'type': 'string'}

    pass


@attrs.define
class TransactionStatus:

    transaction_status: dict[str, Any]
    # {'ref': '#/components/schemas/Transaction', 'generator': <__mp_main__.Generator object at 0x000001B2839E1F30>}
    pass


class VendorDirectFulfillmentSandboxTestData20211028Client(BaseClient):
    def generate_order_scenarios(
        self,
    ):
        """
        Submits a request to generate test order data for Vendor Direct Fulfillment API entities.

        Args:
        """
        url = "/vendor/directFulfillment/sandbox/2021-10-28/orders"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._generate_order_scenarios_params)
        return response

    _generate_order_scenarios_params = ()  # name, param in

    def get_order_scenarios(
        self,
        transaction_id: str,
    ):
        """
        Returns the status of the transaction indicated by the specified transactionId. If the transaction was successful, also returns the requested test order data.

        Args:
            transaction_id: The transaction identifier returned in the response to the generateOrderScenarios operation.
        """
        url = "/vendor/directFulfillment/sandbox/2021-10-28/transactions/{transactionId}"
        values = (transaction_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_order_scenarios_params)
        return response

    _get_order_scenarios_params = (("transactionId", "path"),)  # name, param in
