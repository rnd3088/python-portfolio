import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

df = pd.read_csv("../data/category_sales.csv")

category_sales = df.groupby("カテゴリ")["売上"].sum()

plt.figure(figsize=(6, 6))
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=90)
plt.title("カテゴリ別売上の割合")
plt.tight_layout()

plt.savefig("category_sales_pie.png")