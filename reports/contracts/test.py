from flask import Flask
from reports.contracts import contract

if __name__ == "__main__":
    f = contract.get_contract_report_proc()
    print(f)

app = Flask(__name__)
if __name__ == "__main__":
    app.run()
