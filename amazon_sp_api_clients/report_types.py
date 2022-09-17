from enum import IntEnum, Enum
from dataclasses import dataclass


class ReportTypeGroup(IntEnum):
    inventory_reports = 1
    order_reports = 2
    order_tracking_reports = 3
    pending_order_reports = 4
    returns_reports = 5
    performance_reports = 6
    settlement_reports = 7
    fulfillment_by_amazon_fba_reports = 8
    tax_reports = 9
    browse_tree_report = 10
    easy_ship_reports = 11
    amazon_business_reports = 12
    amazon_pay_report = 13
    b2b_product_opportunities_reports = 14
    brand_analytics_reports = 15
    vendor_retail_analytics_reports = 16
    seller_retail_analytics_reports = 17
    invoice_data_reports = 18
    regulatory_compliance_reports = 19

    @property
    def reports(self):
        return (report for report in ReportType if report.group == self)


@dataclass
class __ReportTypeDefinition:
    group_index: int
    report_index: int
    upload_name: str

    @property
    def index(self):
        return self.group_index * 100 + self.report_index

    @property
    def group(self) -> ReportTypeGroup:
        return ReportTypeGroup(self.group_index)


class ReportType(__ReportTypeDefinition, Enum):
    get_flat_file_open_listings_data = 1, 1, "GET_FLAT_FILE_OPEN_LISTINGS_DATA"
    get_merchant_listings_all_data = 1, 2, "GET_MERCHANT_LISTINGS_ALL_DATA"
    get_merchant_listings_data = 1, 3, "GET_MERCHANT_LISTINGS_DATA"
    get_merchant_listings_inactive_data = 1, 4, "GET_MERCHANT_LISTINGS_INACTIVE_DATA"
    get_merchant_listings_data_back_compat = 1, 5, "GET_MERCHANT_LISTINGS_DATA_BACK_COMPAT"
    get_merchant_listings_data_lite = 1, 6, "GET_MERCHANT_LISTINGS_DATA_LITE"
    get_merchant_listings_data_liter = 1, 7, "GET_MERCHANT_LISTINGS_DATA_LITER"
    get_merchant_cancelled_listings_data = 1, 8, "GET_MERCHANT_CANCELLED_LISTINGS_DATA"
    get_merchant_listings_defect_data = 1, 9, "GET_MERCHANT_LISTINGS_DEFECT_DATA"
    get_flat_file_geo_opportunities = 1, 10, "GET_FLAT_FILE_GEO_OPPORTUNITIES"
    get_referral_fee_preview_report = 1, 11, "GET_REFERRAL_FEE_PREVIEW_REPORT"
    get_flat_file_actionable_order_data_shipping = 2, 1, "GET_FLAT_FILE_ACTIONABLE_ORDER_DATA_SHIPPING"
    get_flat_file_order_report_data_shipping = 2, 2, "GET_FLAT_FILE_ORDER_REPORT_DATA_SHIPPING"
    get_flat_file_all_orders_data_by_last_update_general = 3, 1, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    get_flat_file_all_orders_data_by_order_date_general = 3, 2, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    get_flat_file_archived_orders_data_by_order_date = 3, 3, "GET_FLAT_FILE_ARCHIVED_ORDERS_DATA_BY_ORDER_DATE"
    get_xml_all_orders_data_by_last_update_general = 3, 4, "GET_XML_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    get_xml_all_orders_data_by_order_date_general = 3, 5, "GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    get_flat_file_pending_orders_data = 4, 1, "GET_FLAT_FILE_PENDING_ORDERS_DATA"
    get_pending_orders_data = 4, 2, "GET_PENDING_ORDERS_DATA"
    get_converged_flat_file_pending_orders_data = 4, 3, "GET_CONVERGED_FLAT_FILE_PENDING_ORDERS_DATA"
    get_xml_returns_data_by_return_date = 5, 1, "GET_XML_RETURNS_DATA_BY_RETURN_DATE"
    get_flat_file_returns_data_by_return_date = 5, 2, "GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE"
    get_xml_mfn_prime_returns_report = 5, 3, "GET_XML_MFN_PRIME_RETURNS_REPORT"
    get_csv_mfn_prime_returns_report = 5, 4, "GET_CSV_MFN_PRIME_RETURNS_REPORT"
    get_xml_mfn_sku_return_attributes_report = 5, 5, "GET_XML_MFN_SKU_RETURN_ATTRIBUTES_REPORT"
    get_flat_file_mfn_sku_return_attributes_report = 5, 6, "GET_FLAT_FILE_MFN_SKU_RETURN_ATTRIBUTES_REPORT"
    get_seller_feedback_data = 6, 1, "GET_SELLER_FEEDBACK_DATA"
    get_v1_seller_performance_report = 6, 2, "GET_V1_SELLER_PERFORMANCE_REPORT"
    get_v2_seller_performance_report = 6, 3, "GET_V2_SELLER_PERFORMANCE_REPORT"
    get_v2_settlement_report_data_flat_file = 7, 1, "GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE"
    get_v2_settlement_report_data_xml = 7, 2, "GET_V2_SETTLEMENT_REPORT_DATA_XML"
    get_v2_settlement_report_data_flat_file_v2 = 7, 3, "GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2"
    get_amazon_fulfilled_shipments_data_general = 8, 1, "GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL"
    get_amazon_fulfilled_shipments_data_invoicing = 8, 2, "GET_AMAZON_FULFILLED_SHIPMENTS_DATA_INVOICING"
    get_amazon_fulfilled_shipments_data_tax = 8, 3, "GET_AMAZON_FULFILLED_SHIPMENTS_DATA_TAX"
    get_flat_file_all_orders_data_by_last_update_general_deprecated = 8, 4, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    get_flat_file_all_orders_data_by_order_date_general_deprecated = 8, 5, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    get_xml_all_orders_data_by_last_update_general_deprecated = 8, 6, "GET_XML_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    get_xml_all_orders_data_by_order_date_general_deprecated = 8, 7, "GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    get_fba_fulfillment_customer_shipment_sales_data = 8, 8, "GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA"
    get_fba_fulfillment_customer_shipment_promotion_data = 8, 9, "GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_PROMOTION_DATA"
    get_fba_fulfillment_customer_taxes_data = 8, 10, "GET_FBA_FULFILLMENT_CUSTOMER_TAXES_DATA"
    get_remote_fulfillment_eligibility = 8, 11, "GET_REMOTE_FULFILLMENT_ELIGIBILITY"
    get_flat_file_sales_tax_data = 9, 1, "GET_FLAT_FILE_SALES_TAX_DATA"
    sc_vat_tax_report = 9, 2, "SC_VAT_TAX_REPORT"
    get_vat_transaction_data = 9, 3, "GET_VAT_TRANSACTION_DATA"
    get_gst_mtr_b2b_custom = 9, 4, "GET_GST_MTR_B2B_CUSTOM"
    get_gst_mtr_b2c_custom = 9, 5, "GET_GST_MTR_B2C_CUSTOM"
    get_xml_browse_tree_data = 10, 1, "GET_XML_BROWSE_TREE_DATA"
    get_easyship_documents = 11, 1, "GET_EASYSHIP_DOCUMENTS"
    get_easyship_pickedup = 11, 2, "GET_EASYSHIP_PICKEDUP"
    get_easyship_waiting_for_pickup = 11, 3, "GET_EASYSHIP_WAITING_FOR_PICKUP"
    rfqd_bulk_download = 12, 1, "RFQD_BULK_DOWNLOAD"
    fee_discounts_report = 12, 2, "FEE_DISCOUNTS_REPORT"
    get_flat_file_offamazonpayments_sandbox_settlement_data = 13, 1, "GET_FLAT_FILE_OFFAMAZONPAYMENTS_SANDBOX_SETTLEMENT_DATA"
    get_b2b_product_opportunities_recommended_for_you = 14, 1, "GET_B2B_PRODUCT_OPPORTUNITIES_RECOMMENDED_FOR_YOU"
    get_b2b_product_opportunities_not_yet_on_amazon = 14, 2, "GET_B2B_PRODUCT_OPPORTUNITIES_NOT_YET_ON_AMAZON"
    # for compatibility reasons, keep the previous name
    inventory_report = get_flat_file_open_listings_data
    all_listings_report = get_merchant_listings_all_data
    active_listings_report = get_merchant_listings_data
    inactive_listings_report = get_merchant_listings_inactive_data
    open_listings_report = get_merchant_listings_data_back_compat
    open_listings_report_lite = get_merchant_listings_data_lite
    open_listings_report_liter = get_merchant_listings_data_liter
    canceled_listings_report = get_merchant_cancelled_listings_data
    listing_quality_and_suppressed_listing_report = get_merchant_listings_defect_data
    global_expansion_opportunities_report = get_flat_file_geo_opportunities
    referral_fee_preview_report = get_referral_fee_preview_report
    unshipped_orders_report = get_flat_file_actionable_order_data_shipping
    requested_or_scheduled_flat_file_order_report_shipping = get_flat_file_order_report_data_shipping
    flat_file_orders_by_last_update_report = get_flat_file_all_orders_data_by_last_update_general
    flat_file_orders_by_order_date_report = get_flat_file_all_orders_data_by_order_date_general
    flat_file_archived_orders_report = get_flat_file_archived_orders_data_by_order_date
    xml_orders_by_last_update_report = get_xml_all_orders_data_by_last_update_general
    xml_orders_by_order_date_report = get_xml_all_orders_data_by_order_date_general
    flat_file_pending_orders_report = get_flat_file_pending_orders_data
    xml_pending_orders_report = get_pending_orders_data
    converged_flat_file_pending_orders_report = get_converged_flat_file_pending_orders_data
    xml_returns_report_by_return_date = get_xml_returns_data_by_return_date
    flat_file_returns_report_by_return_date = get_flat_file_returns_data_by_return_date
    xml_prime_returns_report_by_return_date = get_xml_mfn_prime_returns_report
    csv_prime_returns_report_by_return_date = get_csv_mfn_prime_returns_report
    xml_return_attributes_report_by_return_date = get_xml_mfn_sku_return_attributes_report
    flat_file_return_attributes_report_by_return_date = get_flat_file_mfn_sku_return_attributes_report
    flat_file_feedback_report = get_seller_feedback_data
    xml_customer_metrics_report = get_v1_seller_performance_report
    seller_performance_report = get_v2_seller_performance_report
    flat_file_settlement_report = get_v2_settlement_report_data_flat_file
    xml_settlement_report = get_v2_settlement_report_data_xml
    flat_file_v2_settlement_report = get_v2_settlement_report_data_flat_file_v2
    fba_amazon_fulfilled_shipments_report = get_amazon_fulfilled_shipments_data_general
    fba_amazon_fulfilled_shipments_report_invoicing = get_amazon_fulfilled_shipments_data_invoicing
    fba_amazon_fulfilled_shipments_report_tax = get_amazon_fulfilled_shipments_data_tax
    flat_file_all_orders_report_by_last_update = get_flat_file_all_orders_data_by_last_update_general
    flat_file_all_orders_report_by_order_date = get_flat_file_all_orders_data_by_order_date_general
    xml_all_orders_report_by_last_update = get_xml_all_orders_data_by_last_update_general
    xml_all_orders_report_by_order_date = get_xml_all_orders_data_by_order_date_general
    fba_customer_shipment_sales_report = get_fba_fulfillment_customer_shipment_sales_data
    fba_promotions_report = get_fba_fulfillment_customer_shipment_promotion_data
    fba_customer_taxes = get_fba_fulfillment_customer_taxes_data
    remote_fulfillment_eligibility = get_remote_fulfillment_eligibility
    sales_tax_report = get_flat_file_sales_tax_data
    amazon_vat_calculation_report = sc_vat_tax_report
    amazon_vat_transactions_report = get_vat_transaction_data
    on_demand_gst_merchant_tax_report_b2b = get_gst_mtr_b2b_custom
    on_demand_gst_merchant_tax_report_b2c = get_gst_mtr_b2c_custom
    browse_tree_report = get_xml_browse_tree_data
    easyship_report = get_easyship_documents
    easyship_picked_up_report = get_easyship_pickedup
    easyship_waiting_for_pick_up_report = get_easyship_waiting_for_pickup
    manage_quotes_report = rfqd_bulk_download
    referral_fee_discounts_report = fee_discounts_report
    amazonpay_sandbox_settlement_report = get_flat_file_offamazonpayments_sandbox_settlement_data
    b2b_product_opportunities_recommended_for_you_report = get_b2b_product_opportunities_recommended_for_you
    b2b_product_opportunities_not_yet_on_amazon = get_b2b_product_opportunities_not_yet_on_amazon
