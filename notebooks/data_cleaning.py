import pandas as pd
import numpy as np

df = pd.read_csv("data/marketing_data.csv")

df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])

df['Income'] = df['Income'].fillna(df['Income'].median())

df['Age'] = 2024 - df['Year_Birth']
df = df[(df['Age'] >= 18) & (df['Age'] <= 90)]

df['Children'] = df['Kidhome'] + df['Teenhome']

df['Total_Spend'] = (
    df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] +
    df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
)

df['Total_Purchases'] = (
    df['NumWebPurchases'] + df['NumCatalogPurchases'] +
    df['NumStorePurchases'] + df['NumDealsPurchases']
)

df['Customer_Tenure_Days'] = (pd.Timestamp.today() - df['Dt_Customer']).dt.days

df.to_csv("data/marketing_cleaned.csv", index=False)

print("✅ Data Cleaning Completed")
