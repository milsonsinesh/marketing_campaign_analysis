import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/marketing_cleaned.csv")

sns.histplot(df['Age'], bins=30)
plt.title("Age Distribution")
plt.show()

sns.boxplot(x='Response', y='Income', data=df)
plt.title("Income vs Campaign Response")
plt.show()

sns.boxplot(x='Response', y='Total_Spend', data=df)
plt.title("Spending vs Response")
plt.show()
