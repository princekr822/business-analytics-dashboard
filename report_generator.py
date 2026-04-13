import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def get_kpis(df):
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_orders = df.shape[0]
    return total_sales, total_profit, total_orders

def sales_by_region(df):
    return df.groupby('Region')['Sales'].sum().reset_index()

def profit_by_product(df):
    return df.groupby('Product')['Profit'].sum().reset_index()