# helper functions for loading the olist data
# I kept reloading everything manually so I put it in a function

import pandas as pd
import os


def load_all_tables(raw_path):
    # returns a dict of {table_name: dataframe} for all 9 csv files

    files = {
        'customers': 'olist_customers_dataset.csv',
        'orders': 'olist_orders_dataset.csv',
        'order_items': 'olist_order_items_dataset.csv',
        'order_payments': 'olist_order_payments_dataset.csv',
        'order_reviews': 'olist_order_reviews_dataset.csv',
        'products': 'olist_products_dataset.csv',
        'sellers': 'olist_sellers_dataset.csv',
        'geolocation': 'olist_geolocation_dataset.csv',
        'category_translation': 'product_category_name_translation.csv'
    }

    tables = {}
    for name, filename in files.items():
        path = os.path.join(raw_path, filename)
        tables[name] = pd.read_csv(path)
        print(f"loaded {name}: {tables[name].shape}")

    return tables


def parse_order_dates(orders_df):
    # converts the 5 date columns from string to datetime, returns a copy

    date_cols = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]

    df = orders_df.copy()
    for col in date_cols:
        df[col] = pd.to_datetime(df[col])

    return df
