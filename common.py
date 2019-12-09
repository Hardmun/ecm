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

class test:
    pass