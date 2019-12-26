# from builtins import dict
#
# from numpy.ma import var
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from requests import Session
from zeep import Client
from zeep.transports import Transport
# import gzip
# import zipfile
# import io
# import sys
# import json

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

dict = {
    "home": " Это мой дом",
    "Адрес": varstr
}

t = client.service.getresult(args=varstr)

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

# utf = varstr.encode("utf-8")
#
#
#
# virtfile = io.BytesIO()
# compstring = gzip.compress(utf)

# with zipfile.ZipFile(virtfile, mode="w", compression=zipfile.ZIP_DEFLATED) as zpfile:
#     zpfile.writestr("tmp", utf)

# zpfile.write("c://1.zip")

# with zipfile.ZipFile("D://1/python.zip", mode="w", compression=zipfile.ZIP_DEFLATED) as zp:
#     zp.writestr("tmp", varstr)

#     asdf=0
# zp.writestr('tmp',data=utf)
#     asdf=0
#     zp.close()
#     sadf=0

# dict_utf = json.dumps(dict).encode("utf-8")
# dict_decode = json.loads(dict_utf)

# t = client.service.getresult(args=str(dict).encode("utf-8"))

# testIO = io.BytesIO(dict)

t = client.service.getresult(args=dict)

# with open("D://1/python.zip","wb") as enc:
#     enc.write(virtfile.getvalue())
