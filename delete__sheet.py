import openpyxl

def delete_worksheet(file_path, sheet_name):
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)

    # Check if the worksheet exists
    if sheet_name in workbook.sheetnames:
        # Get the worksheet
        worksheet = workbook[sheet_name]

        # Delete the worksheet
        workbook.remove(worksheet)

        # Save the changes to the workbook
        workbook.save(file_path)
        print(f"The worksheet '{sheet_name}' has been deleted successfully.")
    else:
        print(f"The worksheet '{sheet_name}' does not exist in the workbook.")
