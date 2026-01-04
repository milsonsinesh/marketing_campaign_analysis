import pandas as pd
import numpy as np

df = pd.read_csv("data/marketing_cleaned.csv")

df['High_Income'] = np.where(df['Income'] > 75000, 1, 0)
df['Young_Customer'] = np.where(df['Age'] < 30, 1, 0)
df['High_Web_Engagement'] = np.where(df['NumWebVisitsMonth'] > 5, 1, 0)
df['Family_Customer'] = np.where(df['Children'] > 0, 1, 0)

threshold = df['Total_Spend'].quantile(0.90)
df['High_Spender'] = np.where(df['Total_Spend'] > threshold, 1, 0)

df.to_csv("data/marketing_final.csv", index=False)

print("✅ Segmentation Completed")
