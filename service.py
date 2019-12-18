import win32serviceutil
import win32service
import win32event
import servicemanager
from multiprocessing import Process

# from app import app

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

    def SvcDoRun(self):
        self.process = Process(target=self.main)
        self.process.start()
        self.process.run()

    # def main(self):
    #     app.run(host="0.0.0.0", debug=False, port=8181)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(Service)
