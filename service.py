import win32serviceutil
import win32service
import win32event
import servicemanager
# from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

from app import app

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = "ecmapiwin"
    _svc_display_name_ = "ecm api service for 1c"
    _svc_description_ = "External api for 1c"

    def __init__(self, *args):
        super().__init__(*args)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.process.terminate()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def main(self):
        app.run(host="0.0.0.0", debug=False, port=8181)

    def SvcDoRun(self):
        with ProcessPoolExecutor() as executor:
            executor.submit(self.main)
        # self.process = Process(target=self.main)
        # self.process.start()
        # self.process.run()

if __name__ == '__main__':
    # app.run(host="0.0.0.0", debug=False, port=5050)
    win32serviceutil.HandleCommandLine(Service)
