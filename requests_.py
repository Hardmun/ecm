from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from requests import Session
from zeep import Client
from zeep.transports import Transport
import gzip

session = Session()
session.auth = HTTPBasicAuth("Интеграция".encode("UTF-8"), "123")
client = Client('http://hq-s-1c-dev.hq.ecm.local/ps_dev/ws/exchangeCons?wsdl',
                transport=Transport(session=session))
# t = client.service.getresult(args = "sadfasdf")

varstr = "Строка для преобразования Строка для преобразованияСтрока для преобразованияСтрока для преобразованияСтрока для преобразования\
        Строка для преобразования Строка для преобразованияСтрока для преобразованияСтрока для преобразованияСтрока для преобразования\
Строка для преобразования Строка для преобразованияСтрока для преобразованияСтрока для преобразованияСтрока для преобразования\
Строка для преобразования Строка для преобразованияСтрока для преобразованияСтрока для преобразованияСтрока для преобразования\
Строка для преобразования Строка для преобразованияСтрока для преобразованияСтрока для преобразованияСтрока для преобразования\
Строка для преобразования Строка для преобразованияСтрока для преобразованияСтрока для преобразованияСтрока для преобразования\
Строка для преобразования Строка для преобразованияСтрока для преобразованияСтрока для преобразованияСтрока для преобразования\
Строка для преобразования Строка для преобразованияСтрока для преобразованияСтрока для преобразованияСтрока для преобразования"

# varstr = "String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!\
# String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!String to decode !!!!"

utf = varstr.encode("utf-8")

compstring = gzip.compress(utf)
t = client.service.getresult(args=compstring)
