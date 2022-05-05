"""
Selling Partner API for Catalog Items
=============================================================================================
The Selling Partner API for Catalog Items provides programmatic access to information about items in the Amazon catalog.

For more information, see the [Catalog Items API Use Case Guide](doc:catalog-items-api-v2020-12-01-use-case-guide).
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2020-12-01
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class CatalogItems20201201Client(BaseClient):
    def search_catalog_items(
        self,
        keywords: list[str],
        marketplace_ids: list[str],
        included_data: list[
            Union[
                Literal["identifiers"],
                Literal["images"],
                Literal["productTypes"],
                Literal["salesRanks"],
                Literal["summaries"],
                Literal["variations"],
                Literal["vendorDetails"],
            ]
        ] = None,
        brand_names: list[str] = None,
        classification_ids: list[str] = None,
        page_size: int = None,
        page_token: str = None,
        keywords_locale: str = None,
        locale: str = None,
    ):
        """
        Search for and return a list of Amazon catalog items and associated information.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 5 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            keywords: A comma-delimited list of words or item identifiers to search the Amazon catalog for.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            included_data: A comma-delimited list of data sets to include in the response. Default: summaries.
            brand_names: A comma-delimited list of brand names to limit the search to.
            classification_ids: A comma-delimited list of classification identifiers to limit the search to.
            page_size: Number of results to be returned per page.
            page_token: A token to fetch a certain page when there are multiple pages worth of results.
            keywords_locale: The language the keywords are provided in. Defaults to the primary locale of the marketplace.
            locale: Locale for retrieving localized summaries. Defaults to the primary locale of the marketplace.
        """
        path_parameters = {}

        url = "/catalog/2020-12-01/items".format(**path_parameters)

        query_parameters = {}

        query_parameters["keywords"] = keywords

        query_parameters["marketplaceIds"] = marketplace_ids

        if included_data is not None:
            query_parameters["includedData"] = included_data

        if brand_names is not None:
            query_parameters["brandNames"] = brand_names

        if classification_ids is not None:
            query_parameters["classificationIds"] = classification_ids

        if page_size is not None:
            query_parameters["pageSize"] = page_size

        if page_token is not None:
            query_parameters["pageToken"] = page_token

        if keywords_locale is not None:
            query_parameters["keywordsLocale"] = keywords_locale

        if locale is not None:
            query_parameters["locale"] = locale

    def get_catalog_item(
        self,
        asin: str,
        marketplace_ids: list[str],
        included_data: list[
            Union[
                Literal["attributes"],
                Literal["identifiers"],
                Literal["images"],
                Literal["productTypes"],
                Literal["salesRanks"],
                Literal["summaries"],
                Literal["variations"],
                Literal["vendorDetails"],
            ]
        ] = None,
        locale: str = None,
    ):
        """
        Retrieves details for an item in the Amazon catalog.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 5 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            asin: The Amazon Standard Identification Number (ASIN) of the item.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers. Data sets in the response contain data only for the specified marketplaces.
            included_data: A comma-delimited list of data sets to include in the response. Default: summaries.
            locale: Locale for retrieving localized summaries. Defaults to the primary locale of the marketplace.
        """
        path_parameters = {}

        path_parameters["asin"] = asin

        url = "/catalog/2020-12-01/items/{asin}".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

        if included_data is not None:
            query_parameters["includedData"] = included_data

        if locale is not None:
            query_parameters["locale"] = locale
