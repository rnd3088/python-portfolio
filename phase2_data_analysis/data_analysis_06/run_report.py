from generate_sales_report import generate_report

title = "売上分析レポート"
image_paths = [
    ("日別売上推移", "../data_analysis_02/daily_sales.png"),
    ("曜日別平均売上", "../data_analysis_02/weekday_avg_sales.png"),
    ("カテゴリ別売上の割合", "../data_analysis_03/category_sales_pie.png"),
    ("月別カテゴリ売上", "../data_analysis_04/monthly_category_sales.png"),
]
output_path = "sales_report.pdf"

generate_report(title, image_paths, output_path)
