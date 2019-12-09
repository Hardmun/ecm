def projectdir(ctlg, usetempdir=False):
    """if executable file -  have to change the default path"""
    import os
    import sys
    if getattr(sys, 'frozen', False) and usetempdir:
        exe_path = os.path.dirname(sys.executable)
        dirPath = os.path.join(getattr(sys, "_MEIPASS", exe_path), ctlg)
    else:
        dirPath = ctlg
    return dirPath

def get_module_file(abs_path, filename=""):
    pass
    # """returns the full path to the file"""
    # import os
    # import sys
    # dirPath = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(
    #     os.path.abspath(abs_path))
    # return dirPath.replace("modules", "") + os.path.normpath(filename)


def df_to_excel(table, file="", template="", columns=None):
    from openpyxl import load_workbook
    from copy import copy

    if columns is None:
        columns = {}

    lw = load_workbook(template)
    lw_sheet = lw.active
    # for _ in range(10):
    cell = lw_sheet["M2"]
    new_cell = lw_sheet["N2"]

    # if cell.has_style:
        # new_cell._style = copy(cell._style)
    # new_cell.font = copy(cell.font)
    # new_cell.border = copy(cell.border)
    # new_cell.fill = copy(cell.fill)
    # new_cell.number_format = copy(cell.number_format)
    # new_cell.protection = copy(cell.protection)
    # new_cell.alignment = copy(cell.alignment)

    lw.save(file)

df_to_excel(123,file="reports//contracts//files//result.xlsx", template="reports//contracts//files//contract_sketch.xlsx")