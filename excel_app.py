from pandas import ExcelFile as pd_ExcelFile
from openpyxl import load_workbook
from copy import copy

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


