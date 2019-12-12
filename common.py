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

# def get_contract_report_proc():
#     with ProcessPoolExecutor(1) as executor:
#         prc = executor.submit(get_contract_report).result()
#         return prc
