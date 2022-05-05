"""
Selling Partner API for Retail Procurement Transaction Status
=============================================================================================
The Selling Partner API for Retail Procurement Transaction Status provides programmatic access to status information on specific asynchronous POST transactions for vendors.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class VendorTransactionStatusV1Client(BaseClient):
    def get_transaction(
        self,
        transaction_id: str,
    ):
        """
        Returns the status of the transaction that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            transaction_id: The GUID provided by Amazon in the 'transactionId' field in response to the post request of a specific transaction.
        """
        path_parameters = {}
        url = "/vendor/transactions/v1/transactions/{transactionId}"
        params = (("transactionId", "path", transaction_id, True),)  # name, param in, value, required
