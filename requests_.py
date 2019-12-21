from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from requests import Session
from zeep import Client
from zeep.transports import Transport

session = Session()
session.auth = HTTPBasicAuth("Интеграция".encode("UTF-8"), "123")
client = Client('http://hq-s-1c-dev.hq.ecm.local/ps_dev/ws/exchangeCons?wsdl',
            transport=Transport(session=session))
t = client.service.getresult(paramsCode = "1")

