@second
To add additional files need to compile like this:
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py