import pandas as pd
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

df = pd.read_csv("../data/category_sales.csv")

df["日付"] = pd.to_datetime(df["日付"])
df["月"] = df["日付"].dt.strftime("%Y-%m")

pivot = df.pivot_table(index="月", columns="カテゴリ", values="売上", aggfunc="sum", fill_value=0)

pivot.plot(kind="bar", stacked=True, figsize=(10, 6))

plt.title("月別カテゴリ売上")
plt.xlabel("月")
plt.ylabel("売上")
plt.tight_layout()

plt.savefig("monthly_category_sales.png")