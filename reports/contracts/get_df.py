import pandas as pd
import os

def getDataFromExcel(filename, cols=None):
    abspath = os.path.dirname(os.path.abspath(__file__))
    path_xls = os.path.join(abspath, filename)
    with pd.ExcelFile(path_xls) as file_xls:
        for curr_sheet in file_xls.sheet_names:
            sheet_df = file_xls.parse(curr_sheet, index=True).fillna('')
            break
    if cols is not None:
        for i in range(len(cols)):
            if type(cols[i]) == int:
                cols[i] = sheet_df.columns[cols[i]]
        return sheet_df[cols]

    return sheet_df

# getxls = getDataFromExcel("periods.xlsx", [2,3,"ВыручкаЗаПериодФакт"])
