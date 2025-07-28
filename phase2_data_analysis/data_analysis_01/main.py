import pandas as pd

df = pd.read_csv("sample.csv")

print("📌 データの先頭５行目:")
print(df.head())

print("\n📌 列名一覧:")
print(df.columns)

print("\n📌 データの形状(行数、 列名):")
print(df.shape)

print("\n📌 要約統計情報：")
print(df.describe())

print("\n📌 売上が1300を超える行:")
print(df[df["売上"] > 1300])

print("\n📌 売上が高い順に並べる:")
print(df.sort_values("売上", ascending=False))

print("\n📌 店舗ごとの売上合計")
print(df.groupby("店舗")["売上"].sum())