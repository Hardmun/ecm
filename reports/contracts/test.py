from flask import Flask
from reports.contracts import contract

if __name__ == "__main__":
    result = contract.get_contract_report_proc()
    result = result.set_index(['rev_treat', 'exp_treat'])

    for i in result.itertuples():
        print(i)