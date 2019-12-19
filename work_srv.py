import win32serviceutil
import win32service
import win32event
import servicemanager
import socket

from flask_app import app


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"
    _svc_description_ = "Test Service for 1c"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)


    def SvcDoRun(self):
        f = open('test.dat', 'w+')
        rc = None
        # if the stop event hasn't been fired keep looping
        while rc != win32event.WAIT_OBJECT_0:
            # f.write('TEST DATA\n')
            # f.flush()
            # block for 5 seconds and listen for a stop event

            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)

        f.write('SHUTTING DOWN\n')
        f.close()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        # self.main()

    def main(self):
        flask_app.app.run(host="0.0.0.0", debug=False, port=5050)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)