from flask import Flask
from reports.contracts import contract

if __name__ == "__main__":
    result = contract.get_contract_report_proc()
    result = result.set_index(['rev_treat', 'exp_treat']).sort_index()

    # indx = result.index
    # for ind in indx:
    #     # result = rusult[ind]
    #     sdf=0

    for i in result.iterrows():
        print(i)