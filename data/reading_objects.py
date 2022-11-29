from library_.config import Config
import xlrd
# path= Config.DATA_PATH

def read_test_data():
    workbook = xlrd.open_workbook(Config.DATA_PATH)
    worksheet = workbook.sheet_by_name("TC_Data")
    # print(columns)
    rows = worksheet.get_rows()
    columns = worksheet.ncols
    header = next(rows)
    data = []

    for row in rows:
        values = ()
        for j in range(columns):
            values += (row[j].value,)
        data.append(values)
    return data


print(read_test_data())

def read_locators():
    workbook = xlrd.open_workbook(Config.DATA_PATH)
    worksheet = workbook.sheet_by_name("SearchPage")
    rows = worksheet.nrows
    # print(rows)
    d={}

    for i in range(1,rows):
        row = worksheet.row_values(i)
        d[row[0]] = (row[1],row[2])
    return d
print(read_locators())










# rd = ReadExcel()
# print(rd.read_test_data("TC_Data"))



    # row = worksheet.row_values(i)
    # print(row)
    # d[row[0]] = (row[1], row[2])
