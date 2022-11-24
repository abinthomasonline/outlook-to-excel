from excel_utils.create import create_excel_file

import os
import openpyxl


def append_to_excel_file(config, records):
    output_path = config['output_path']
    if not os.path.exists(output_path):
        create_excel_file(config)
    workbook = openpyxl.load_workbook(output_path)
    sheet = workbook.active
    for record in records:
        sheet.append(record)
    workbook.save(output_path)
    workbook.close()
