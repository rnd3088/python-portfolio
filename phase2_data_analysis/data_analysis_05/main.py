from fpdf import FPDF

pdf = FPDF()
pdf.add_font('IPAexMincho', '', './fonts/ipaexm.ttf', uni=True)  
pdf.set_auto_page_break(auto=True, margin=15)

# タイトルページ
pdf.add_page()
pdf.set_font('IPAexMincho', '', 16)
pdf.set_y(148.5)
pdf.cell(0, 10, "売上分析レポート", ln=True, align='C')

# ① 日別売上推移
pdf.add_page()
pdf.set_font('IPAexMincho', '', 12)
pdf.cell(0, 10, "① 日別売上推移", ln=True)
pdf.image("../data_analysis_02/daily_sales.png", w=170)

# ② 曜日別平均売上
pdf.add_page()
pdf.cell(0, 10, "② 曜日別平均売上", ln=True)
pdf.image("../data_analysis_02/weekday_avg_sales.png", w=170)

# ③ カテゴリ別売上の割合
pdf.add_page()
pdf.cell(0, 10, "③ カテゴリ別売上の割合", ln=True)
pdf.image("../data_analysis_03/category_sales_pie.png", w=150)

# ④ 月別カテゴリ売上
pdf.add_page()
pdf.cell(0, 10, "④ 月別カテゴリ売上", ln=True)
pdf.image("../data_analysis_04/monthly_category_sales.png", w=170)

# 保存
pdf.output("sales_report.pdf")
