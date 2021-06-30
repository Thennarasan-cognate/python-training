import xlrd

loc=("C:\\Users\\User\\AppData\\Local\\Programs\\Python\Python39\\TEST_READ.xls")
#after writing in excel file to read save excel file as Excel 97-2003 workbook 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(0, 0))
