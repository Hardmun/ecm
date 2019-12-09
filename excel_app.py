from pandas import ExcelFile as pd_ExcelFile

def getDataFromExcel(filename, cols=None):
    with pd_ExcelFile(filename) as file_xls:
        for curr_sheet in file_xls.sheet_names:
            sheet_df = file_xls.parse(curr_sheet, index=True).fillna('')
            break

    if cols is not None:
        for i in range(len(cols)):
            if type(cols[i]) == int:
                cols[i] = sheet_df.columns[cols[i]]
        return sheet_df[cols]

    return sheet_df

#
# def df_to_excel(table, file="", template="", columns=None):
#     from openpyxl import load_workbook
#     from copy import copy
#
#     if columns is None:
#         columns = {}
#
#     lw = load_workbook(template)
#     lw_sheet = lw.active
#     # for _ in range(10):
#     cell = lw_sheet["M2"]
#     new_cell = lw_sheet["N2"]
#
#     # if cell.has_style:
#         # new_cell._style = copy(cell._style)
#     # new_cell.font = copy(cell.font)
#     # new_cell.border = copy(cell.border)
#     # new_cell.fill = copy(cell.fill)
#     # new_cell.number_format = copy(cell.number_format)
#     # new_cell.protection = copy(cell.protection)
#     # new_cell.alignment = copy(cell.alignment)
#
#     lw.save(file)
#
# df_to_excel(123,file="reports//contracts//files//result.xlsx", template="reports//contracts//files//contract_sketch.xlsx")
