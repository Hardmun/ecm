# import pandas as pd
# from jupyter_mod.files.get_df import getDataFromExcel
# from numpy import sum
# from flask import Flask
# from jupyter_mod.export_xls import df_to_excel
# import datetime
# import re
#
# pd.set_option('display.max_rows', 500)

def get_contract_report():
    pass

# df_period = getDataFromExcel("periods.xlsx",
#                              ["Период", "ДоговорСсылка", "Филиал", "ОплатаЗаПериодПлан", "ОплатаЗаПериодФакт",
#                               "СуммаЗаПериодПлан", "ВыручкаЗаПериодФакт"])
# df_period = df_period.rename(
#     columns={"Период": "date", "ДоговорСсылка": "treat", "Филиал": "branch", "ОплатаЗаПериодПлан": "pay_plan",
#              "ОплатаЗаПериодФакт": "pay_fact", "СуммаЗаПериодПлан": "revenue_plan",
#              "ВыручкаЗаПериодФакт": "revenue_fact"})
# df_rev = getDataFromExcel("revenew.xlsx",
#                           ["ДоговорСсылка", "Дох_Договор", "Дох_НомерДоговора", "Дох_Контрагент", "СуммаДоговора",
#                            "Филиал"])
# df_rev = df_rev.rename(columns={"ДоговорСсылка": "treat", "Дох_Договор": "rev_treat", "Дох_НомерДоговора": "treat_num",
#                                 "Дох_Контрагент": "client", "СуммаДоговора": "treat_amount", "Филиал": "branch"})
# df_exp = getDataFromExcel("expense.xlsx",
#                           ["ДоговорСсылка", "Дох_Договор", "Дох_НомерДоговора", "Дох_Контрагент", "Расх_Договор",
#                            "Расх_Контрагент", "СуммаДоговора", "Филиал"])
# df_exp = df_exp.rename(columns={"ДоговорСсылка": "treat", "Дох_Договор": "rev_treat", "Дох_НомерДоговора": "treat_num",
#                                 "Дох_Контрагент": "client", "Расх_Договор": "exp_treat",
#                                 "Расх_Контрагент": "exp_client", "СуммаДоговора": "treat_amount", "Филиал": "branch"})
#
# result = pd.concat([df_rev, df_exp], ignore_index=True, sort=False)
# result = result.loc[result['rev_treat'] == '"Договор 00000000052 от 25.01.2012 13:03:37"']
# df_period_pivot = df_period.pivot_table(index=["treat", "branch"], columns="date",
#                                         values=["pay_plan", "pay_fact", "revenue_plan", "revenue_fact"], margins=True,
#                                         aggfunc=sum)
# # df_period_pivot = df_period_pivot.swaplevel(0, 1, axis=1).sort_index(axis=1)
#
# result = pd.merge(result, df_period, on=["treat", "branch"], how="left")
# result = result.fillna(
#     {"date": "01.01.2019 0:00:00", "pay_plan": 0, "pay_fact": 0, "revenue_plan": 0, "revenue_fact": 0}).fillna("null")
# result = result.pivot_table(index=["treat", "branch", "rev_treat", "exp_treat", "treat_amount"], columns="date",
#                             values=["pay_plan", "pay_fact", "revenue_plan", "revenue_fact"], fill_value=0, margins=True,
#                             aggfunc=sum)
# # result = result.swaplevel(0, 1, axis=1).sort_index(axis=1)
# result = result.reset_index()

# datestr = "23.08.2015 12:00:01"
# pat = re.compile("[0-9]")
# ismatch = re.match(re.compile("[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]"), datestr)



# columns = result.columns
# for col in columns:
#     print(col)

# df_to_excel(result,file="files//result.xlsx", template="files//contract_sketch.xlsx")

# app = Flask(__name__)
# if __name__ == "__main__":
#     app.run(port=9898)

a = get_contract_report()