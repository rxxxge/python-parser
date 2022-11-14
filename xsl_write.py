import xlsxwriter
from main import array


def writer(parameter):
    book = xlsxwriter.Workbook(r"/Users/tanya/Documents/Monty_Python/scraping/data.xlsx")
    page = book.add_worksheet("Items")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    for item in parameter():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        page.write(row, column + 3, item[3])
        row += 1

    book.close()

writer(array)   

