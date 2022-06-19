import openpyxl
from openpyxl.chart import BarChart3D, Reference
wb = openpyxl.Workbook()
sheet = wb.active

for i in range(20):
    sheet.append([i])

values = Reference(sheet, min_col = 1, min_row = 1,max_col = 1, max_row = 20)
chart=BarChart3D()
chart.add_data(values)
chart.title= "Bar Chart 3D"
chart.x_axis.title="X-axis"
chart.y_axis.title= "Y-axis"
sheet.add_chart(chart,"D2")

wb.save("BarChart3D.xlsx")