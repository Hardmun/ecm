import win32serviceutil
import win32service
import win32event
import servicemanager
from concurrent.futures import ProcessPoolExecutor

from flask_app import app
import os

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = "ecmapp"
    _svc_display_name_ = "ECM application"
    _svc_description_ = "ECM application"

    def __init__(self, *args):
        super().__init__(*args)
        self.pid_1 = None

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def SvcDoRun(self):
        with ProcessPoolExecutor(1) as executor:
            executor.submit(self.main)

    def main(self):
        app.run(host="0.0.0.0", debug=False, port=8181)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(Service)
