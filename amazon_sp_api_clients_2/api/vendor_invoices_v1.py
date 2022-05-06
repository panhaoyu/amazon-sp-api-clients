"""
Selling Partner API for Retail Procurement Payments
=============================================================================================

The Selling Partner API for Retail Procurement Payments provides programmatic access to vendors payments data.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class AdditionalDetails:
    """
    Additional information provided by the selling party for tax-related or any other purpose.
    """

    detail: str = attrs.field(
        kw_only=True,
    )
    """
    The detail of the additional information provided by the selling party.
    """

    language_code: str = attrs.field(
        kw_only=True,
    )
    """
    The language code of the additional information detail.
    """

    type: Union[Literal["SUR"], Literal["OCR"], Literal["CartonCount"]] = attrs.field(
        kw_only=True,
    )
    """
    The type of the additional information provided by the selling party.
    """


@attrs.define
class Address:
    """
    A physical address.
    """

    address_line1: str = attrs.field(
        kw_only=True,
    )
    """
    First line of street address.
    """

    address_line2: str = attrs.field(
        kw_only=True,
    )
    """
    Additional address information, if required.
    """

    address_line3: str = attrs.field(
        kw_only=True,
    )
    """
    Additional address information, if required.
    """

    city: str = attrs.field(
        kw_only=True,
    )
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.

    Extra fields:
    {'maxLength': 2}
    """

    county: str = attrs.field(
        kw_only=True,
    )
    """
    The county where person, business or institution is located.
    """

    district: str = attrs.field(
        kw_only=True,
    )
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the person, business or institution at that address.
    """

    phone: str = attrs.field(
        kw_only=True,
    )
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_or_zip_code: str = attrs.field(
        kw_only=True,
    )
    """
    The postal or zip code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: str = attrs.field(
        kw_only=True,
    )
    """
    The state or region where person, business or institution is located.
    """


@attrs.define
class AllowanceDetails:
    """
    Monetary and tax details of the allowance.
    """

    allowance_amount: "Money" = attrs.field(
        kw_only=True,
    )

    description: str = attrs.field(
        kw_only=True,
    )
    """
    Description of the allowance.
    """

    tax_details: List["TaxDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Tax amount details applied on this allowance.
    """

    type: Union[
        Literal["Discount"],
        Literal["DiscountIncentive"],
        Literal["Defective"],
        Literal["Promotional"],
        Literal["UnsaleableMerchandise"],
        Literal["Special"],
    ] = attrs.field(
        kw_only=True,
    )
    """
    Type of the allowance applied.
    """


@attrs.define
class ChargeDetails:
    """
    Monetary and tax details of the charge.
    """

    charge_amount: "Money" = attrs.field(
        kw_only=True,
    )

    description: str = attrs.field(
        kw_only=True,
    )
    """
    Description of the charge.
    """

    tax_details: List["TaxDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Tax amount details applied on this charge.
    """

    type: Union[
        Literal["Freight"],
        Literal["Packing"],
        Literal["Duty"],
        Literal["Service"],
        Literal["SmallOrder"],
        Literal["InsurancePlacementCost"],
        Literal["InsuranceFee"],
        Literal["SpecialHandlingService"],
        Literal["CollectionAndRecyclingService"],
        Literal["EnvironmentalProtectionService"],
        Literal["TaxCollectedAtSource"],
    ] = attrs.field(
        kw_only=True,
    )
    """
    Type of the charge applied.
    """


@attrs.define
class CreditNoteDetails:
    """
    References required in order to process a credit note. This information is required only if InvoiceType is CreditNote.
    """

    consignors_reference_number: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies the consignor reference number (VRET number), if generated by Amazon.
    """

    coop_reference_number: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies the COOP reference used for COOP agreement. Failure to provide the COOP reference number or the Debit Note number may lead to a rejection of the Credit Note.
    """

    debit_note_number: str = attrs.field(
        kw_only=True,
    )
    """
    Debit Note Number as generated by Amazon. Recommended for Returns and COOP Credit Notes.
    """

    goods_return_date: "DateTime" = attrs.field(
        kw_only=True,
    )

    reference_invoice_number: str = attrs.field(
        kw_only=True,
    )
    """
    Original Invoice Number when sending a credit note relating to an existing invoice. One Invoice only to be processed per Credit Note. This is mandatory for AP Credit Notes.
    """

    returns_reference_number: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies the Returns Notice Number. Mandatory for all Returns Credit Notes.
    """

    rma_id: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies the Returned Merchandise Authorization ID, if generated.
    """


@attrs.define
class DateTime:
    """
    Defines a date and time according to ISO8601.
    """

    pass


@attrs.define
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    pass


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
    A message that describes the error condition.
    """


@attrs.define
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class Invoice:

    additional_details: List["AdditionalDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Additional details provided by the selling party, for tax related or other purposes.
    """

    allowance_details: List["AllowanceDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Total allowance amount details for all line items.
    """

    bill_to_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    charge_details: List["ChargeDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Total charge amount details for all line items.
    """

    date: "DateTime" = attrs.field(
        kw_only=True,
    )

    id: str = attrs.field(
        kw_only=True,
    )
    """
    Unique number relating to the charges defined in this document. This will be invoice number if the document type is Invoice or CreditNote number if the document type is Credit Note. Failure to provide this reference will result in a rejection.
    """

    invoice_total: "Money" = attrs.field(
        kw_only=True,
    )

    invoice_type: Union[Literal["Invoice"], Literal["CreditNote"]] = attrs.field(
        kw_only=True,
    )
    """
    Identifies the type of invoice.
    """

    items: List["InvoiceItem"] = attrs.field(
        kw_only=True,
    )
    """
    The list of invoice items.
    """

    payment_terms: "PaymentTerms" = attrs.field(
        kw_only=True,
    )

    reference_number: str = attrs.field(
        kw_only=True,
    )
    """
    An additional unique reference number used for regulatory or other purposes.
    """

    remit_to_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    ship_from_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    ship_to_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    tax_details: List["TaxDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Total tax amount details for all line items.
    """


@attrs.define
class InvoiceItem:
    """
    Details of the item being invoiced.
    """

    allowance_details: List["AllowanceDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Individual allowance details per line item.
    """

    amazon_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon Standard Identification Number (ASIN) of an item.
    """

    charge_details: List["ChargeDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Individual charge details per line item.
    """

    credit_note_details: "CreditNoteDetails" = attrs.field(
        kw_only=True,
    )

    hsn_code: str = attrs.field(
        kw_only=True,
    )
    """
    HSN Tax code. The HSN number cannot contain alphabets.
    """

    invoiced_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )

    item_sequence_number: int = attrs.field(
        kw_only=True,
    )
    """
    Unique number related to this line item.
    """

    net_cost: "Money" = attrs.field(
        kw_only=True,
    )

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon purchase order number for this invoiced line item. Formatting Notes: 8-character alpha-numeric code. This value is mandatory only when invoiceType is Invoice, and is not required when invoiceType is CreditNote.
    """

    tax_details: List["TaxDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Individual tax details per line item.
    """

    vendor_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor selected product identifier of the item. Should be the same as was provided in the purchase order.
    """


@attrs.define
class ItemQuantity:
    """
    Details of quantity.
    """

    amount: int = attrs.field(
        kw_only=True,
    )
    """
    Quantity of an item. This value should not be zero.
    """

    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]] = attrs.field(
        kw_only=True,
    )
    """
    Unit of measure for the quantity.
    """

    unit_size: int = attrs.field(
        kw_only=True,
    )
    """
    The case size, if the unit of measure value is Cases.
    """


@attrs.define
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    amount: "Decimal" = attrs.field(
        kw_only=True,
    )

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    Three-digit currency code in ISO 4217 format.
    """


@attrs.define
class PartyIdentification:

    address: "Address" = attrs.field(
        kw_only=True,
    )

    party_id: str = attrs.field(
        kw_only=True,
    )
    """
    Assigned identification for the party.
    """

    tax_registration_details: List["TaxRegistrationDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Tax registration details of the party.
    """


@attrs.define
class PaymentTerms:
    """
    Terms of the payment for the invoice. The basis of the payment terms is the invoice date.
    """

    discount_due_days: float = attrs.field(
        kw_only=True,
    )
    """
    The number of calendar days from the Base date (Invoice date) until the discount is no longer valid.
    """

    discount_percent: "Decimal" = attrs.field(
        kw_only=True,
    )

    net_due_days: float = attrs.field(
        kw_only=True,
    )
    """
    The number of calendar days from the base date (invoice date) until the total amount on the invoice is due.
    """

    type: Union[
        Literal["Basic"],
        Literal["EndOfMonth"],
        Literal["FixedDate"],
        Literal["Proximo"],
        Literal["PaymentDueUponReceiptOfInvoice"],
        Literal["LetterofCredit"],
    ] = attrs.field(
        kw_only=True,
    )
    """
    The payment term type for the invoice.
    """


@attrs.define
class SubmitInvoicesRequest:
    """
    The request schema for the submitInvoices operation.
    """

    invoices: List["Invoice"] = attrs.field(
        kw_only=True,
    )


@attrs.define
class SubmitInvoicesResponse:
    """
    The response schema for the submitInvoices operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "TransactionId" = attrs.field(
        kw_only=True,
    )


@attrs.define
class TaxDetails:
    """
    Details of tax amount applied.
    """

    tax_amount: "Money" = attrs.field(
        kw_only=True,
    )

    tax_rate: "Decimal" = attrs.field(
        kw_only=True,
    )

    tax_type: Union[
        Literal["CGST"],
        Literal["SGST"],
        Literal["CESS"],
        Literal["UTGST"],
        Literal["IGST"],
        Literal["MwSt."],
        Literal["PST"],
        Literal["TVA"],
        Literal["VAT"],
        Literal["GST"],
        Literal["ST"],
        Literal["Consumption"],
        Literal["MutuallyDefined"],
        Literal["DomesticVAT"],
    ] = attrs.field(
        kw_only=True,
    )
    """
    Type of the tax applied.
    """

    taxable_amount: "Money" = attrs.field(
        kw_only=True,
    )


@attrs.define
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    tax_registration_number: str = attrs.field(
        kw_only=True,
    )
    """
    The tax registration number for the entity. For example, VAT ID.
    """

    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field(
        kw_only=True,
    )
    """
    The tax registration type for the entity.
    """


@attrs.define
class TransactionId:

    transaction_id: str = attrs.field(
        kw_only=True,
    )
    """
    GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


class VendorInvoicesV1Client(BaseClient):
    def submit_invoices(
        self,
        invoices: List["Invoice"] = None,
    ):
        """
        Submit new invoices to Amazon.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            invoices: no description.
        """
        url = "/vendor/payments/v1/invoices"
        values = (invoices,)
        response = self._parse_args_and_request(url, "POST", values, self._submit_invoices_params)
        return response

    _submit_invoices_params = (("invoices", "body"),)  # name, param in
