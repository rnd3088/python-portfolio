from fpdf import FPDF
import os

def generate_report(title, image_paths, output_path, font_path='./fonts/ipaexm.ttf'):
    pdf = FPDF()
    pdf.add_font('IPAexMincho', '', font_path, uni=True)
    pdf.set_auto_page_break(auto=True, margin=15)

    #タイトルページ
    pdf.add_page()
    pdf.set_font('IPAexMincho', '', 16)
    pdf.set_y(148.5)
    pdf.cell(0, 10, title, ln=True, align='C')

    #各画像ページ
    pdf.set_font('IPAexMincho', '', 12)
    for idx, (label, path) in enumerate(image_paths, start=1):
        if not os.path.exists(path):
            continue
        pdf.add_page()
        pdf.cell(0, 10, f"({idx}) {label}", ln=True)
        pdf.image(path, w=170)

    #保存
    pdf.output(output_path)


#使い方(呼び出し例)
# title = "売上分析レポート"
# image_paths = [
#     ("日別売上推移", "../data_analysis_02/daily_sales.png"),
#     ("曜日別平均売上", "../data_analysis_02/weekday_avg_sales.png"),
#     ("カテゴリ別売上の割合", "../data_analysis_03/category_sales_pie.png"),
#     ("月別カテゴリ売上", "../data_analysis_04/monthly_category_sales.png"),
# ]
# output_path = "sales_report.pdf"

# generate_report(title, image_paths, output_path)

