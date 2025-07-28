import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")

plt.rcParams['font.family'] = 'Hiragino Sans'   # 日本語フォントを指定（macOS向け：ヒラギノ）

df = pd.read_csv('../data_analysis_01/sample.csv')

# --- 日別売上推移 ---
daily_sales = df.groupby("日付")["売上"].sum()

plt.plot(daily_sales.index, daily_sales.values, marker ='o')
plt.title("日別売上推移")
plt.xlabel("日付")
plt.ylabel("売上")
plt.grid(True)
plt.tight_layout()

plt.savefig("daily_sales.png")

# --- 曜日別平均売上 ---
df["日付"] = pd.to_datetime(df["日付"])

df["曜日"] = df["日付"].dt.strftime("%A")

weekday_avg_sales = df.groupby("曜日")["売上"].mean()

weekday_order = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
weekday_avg_sales = weekday_avg_sales.reindex(weekday_order)

plt.figure(figsize=(8, 5))
plt.bar(weekday_avg_sales.index, weekday_avg_sales.values)
plt.title("曜日別の平均売上")
plt.xlabel("曜日")
plt.ylabel("平均売上")
plt.tight_layout()

plt.savefig("weekday_avg_sales.png")
