@main
To add additional files need to compile like this:
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py

To install windows service

1) Error
Error starting service: The service did not respond to the start or control request in a timely fashion.
Solution:
This specific problem was solved by copying this file - pywintypes36.dll
From -> Python36\Lib\site-packages\pywin32_system32
To -> Python36\Lib\site-packages\win32