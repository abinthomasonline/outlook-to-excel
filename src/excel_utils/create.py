import openpyxl


def create_excel_file(config):
    output_path = config['output_path']
    workbook = openpyxl.Workbook()
    workbook.save(output_path)
    workbook.close()
