#pip install xlwt
import xlwt

#create a blank spreadsheet file(or workbook)
wb=xlwt.Workbook()

#create a sheet within the file
#you can add sheets to your workbook by using add_sheet
ws=wb.add_sheet("its a test sheet")

#once you have created a sheet
#you can add values to particular cells in the sheet as follows:
ws.write(0,0,"Test Value")

#the last step saving the workbook
wb.save("writing.xls")
