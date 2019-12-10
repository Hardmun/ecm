from flask import Flask
from reports.contracts import contract

if __name__ == "__main__":
    result = contract.get_contract_report()


    # indx = result.index
    # for ind in indx:
    #     # result = rusult[ind]
    # #     sdf=0
    #
    # for i in result.iterrows():
    #     print(i)