import xlrd
workbook = xlrd.open_workbook('C:\\Users\\MVS AKHIL KUMAR\\Documents\\Book2.xlsx')
sheet = workbook.sheets("Sheet1")
row_count = sheet.nrows
col_count = sheet.ncols
print(row_count)
print(col_count)

