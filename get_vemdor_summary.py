from sqlalchemy import create_engine
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def get_vendor_summary(engine):
    '''Generates a summary of vendor sales and purchases'''
    Vendor_sales_summary = pd.read_sql_query("""
    WITH FreightSummary AS (
        SELECT 
            "VendorNumber", 
            SUM("Freight") AS "FreightCost"
        FROM vendor_invoice 
        GROUP BY "VendorNumber"
    ),
    PurchaseSummary AS (
        SELECT 
            p."VendorNumber",
            p."VendorName",
            p."Brand",
            p."Description",
            p."PurchasePrice",
            pp."Price" AS "ActualPrice",
            pp."Volume",
            SUM(p."Quantity") AS "TotalPurchaseQuantity",
            SUM(p."Dollars") AS "TotalPurchaseDollars"
        FROM purchases p
        JOIN purchase_prices pp
          ON p."Brand" = pp."Brand"
        WHERE p."PurchasePrice" > 0
        GROUP BY p."VendorNumber", p."VendorName", p."Brand", p."Description", p."PurchasePrice", pp."Volume", pp."Price"
    ),
    SalesSummary AS (
        SELECT
            "VendorNo",
            "Brand",
            SUM("SalesQuantity") AS "TotalSalesQuantity",
            SUM("SalesDollars") AS "TotalSalesDollars",  
            SUM("SalesPrice") AS "TotalSalesPrice",
            SUM("ExciseTax") AS "TotalExciseTax"
        FROM sales
        GROUP BY "VendorNo", "Brand"
    )
    SELECT
        ps."VendorNumber",
        ps."VendorName",
        ps."Brand",
        ps."Description",
        ps."PurchasePrice",
        ps."ActualPrice",
        ps."Volume",                                 
        ps."TotalPurchaseQuantity",                      
        ps."TotalPurchaseDollars",
        ss."TotalSalesQuantity",
        ss."TotalSalesDollars",
        ss."TotalSalesPrice",
        ss."TotalExciseTax",
        fs."FreightCost"
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps."VendorNumber" = ss."VendorNo" AND ps."Brand" = ss."Brand"
    LEFT JOIN FreightSummary fs
        ON ps."VendorNumber" = fs."VendorNumber"
    ORDER BY ps."TotalPurchaseDollars" DESC;
""", engine)
    
    return Vendor_sales_summary

def clean_data(df):
    # change TotalPurchaseQuantity to int
    df['TotalPurchaseQuantity'] = df['TotalPurchaseQuantity'].fillna(0).astype(int)
    df['Volume'] = df['Volume'].astype('float64')
    df.fillna(0, inplace=True)
    df['VendorName'] = df['VendorName'].str.strip()


    # Creating new features
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars']) * 100
    df['StockTurnover'] = df['TotalSalesQuantity']/df['TotalPurchaseQuantity']
    df['SalestoPurchaseRatio'] = df['TotalSalesDollars']/df['TotalPurchaseDollars']

    return df


if __name__ == "__main__":
    engine = create_engine("postgresql://postgres:0101@localhost:5432/inventory_management")
    logging.info('Starting vendor summary generation')
    try:
        vendor_summary_df = get_vendor_summary(engine)
        logging.info('Vendor summary data fetched successfully')
        
        vendor_summary_df = clean_data(vendor_summary_df)
        logging.info('Vendor summary data cleaned successfully')
        
        ingest_db(vendor_summary_df, 'vendor_sales_summary', engine=engine)
        logging.info('Vendor summary data ingested into database successfully')
    except Exception as e:
        logging.error(f'❌ Failed to generate or ingest vendor summary: {e}')