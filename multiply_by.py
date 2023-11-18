import openpyxl

def multiply_column_by_100(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    multiply_columns=[7,8,10,53,56]
    for mul_col in multiply_columns:
        for row in sheet.iter_rows(min_row=5, min_col=mul_col, max_col=mul_col):
            for cell in row:
                try:
                    # Multiply the cell value by 100
                    if cell.value=='-':
                        continue
                    else:
                        cell.value = round(cell.value * 100)
                except:
                    # print("Multiply issue at cell ",cell)
                    continue

    workbook.save(file_path)
    workbook.close()

