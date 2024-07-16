# Import Libraries and Dependencies
import pandas as pd
from pathlib import Path

sales_2020_path = Path('Resources/athletic_sales_2020.csv')
sales_2021_path = Path('Resources/athletic_sales_2021.csv')

sales_2020 = pd.read_csv(sales_2020_path)
sales_2021 = pd.read_csv(sales_2021_path)

sales_2020.info(True)
sales_2021.info(True)

combined_sales_df = pd.concat([sales_2020, sales_2021], axis=0, join='inner')
combined_sales_df

combined_sales_df.isnull().sum()

combined_sales_df.info()

combined_sales_df['invoice_date'] = pd.to_datetime(combined_sales_df['invoice_date'], format='%m/%d/%y')
combined_sales_df

combined_sales_df.info(['invoice_date'])

# Show the number products sold for region, state, and city.
# Rename the sum to "Total_Products_Sold".
total_products_sold_df = combined_sales_df.groupby(['region', 'state', 'city'])['units_sold'].agg(Total_Products_Sold=('sum'))

# Show the top 5 results.
total_products_sold_df.sort_values(by=(['Total_Products_Sold']), ascending=False).head()

# Show the number products sold for region, state, and city.


# Rename the "units_sold" column to "Total_Products_Sold"


# Show the top 5 results.