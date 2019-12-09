from excel_app import getDataFromExcel
from pandas import concat as pd_concat
from pandas import merge as pd_merge

def get_xls_struct():
    dates_pivot = {
        "Период": "date",
        "ДоговорСсылка": "treat",
        "Филиал": "branch",
        "ОплатаЗаПериодПлан": "pay_plan",
        "ОплатаЗаПериодФакт": "pay_fact",
        "СуммаЗаПериодПлан": "revenue_plan",
        "ВыручкаЗаПериодФакт": "revenue_fact"}

    revenue = {
        "Филиал": "branch",
        "ДоговорСсылка": "treat",
        "Дох_Договор": "rev_treat",
        "Дох_Контрагент": "client",
        "Дох_ИНН": "inn",
        "Дох_НомерДоговора": "treat_num",
        "Дох_Дата": "treat_date",
        "Дох_ДатаОкончания": "treat_end_date",
        "Дох_ОбъектДоговора": "treat_object",
        "Дох_Тип": "treat_type",
        "СуммаДоговора": "treat_amount",
        "СуммаНачало": "amount_done_on_begin",
        "ОстатокНачало": "amount_on_begin",
        "ОплатаНаНачало": "pay_on_begin",
        "СуммаКонец": "amount_done_on_end",
        "ОстатокКонец": "amount_on_end"}

    expense = {
        "Филиал": "branch",
        "ДоговорСсылка": "treat",
        "Дох_Договор": "rev_treat",
        "Расх_Договор": "exp_treat",
        "Расх_Тип": "exp_type",
        "Расх_Контрагент": "exp_client",
        "Расх_ИНН": "exp_inn",
        "Расх_НомерДоговора": "exp_num",
        "Расх_Дата": "exp_date",
        "СуммаДоговора": "treat_amount",
        "СуммаНачало": "amount_done_on_begin",
        "ОстатокНачало": "amount_on_begin",
        "СуммаКонец": "amount_done_on_end",
        "ОстатокКонец": "amount_on_end"}

    list_rev = list(revenue.values())
    for exp_var in list(expense.values()):
        if exp_var not in list_rev:
            list_rev.append(exp_var)

    return [dates_pivot, revenue, expense, list_rev]

def get_contract_report():
    xls_struct = get_xls_struct()
    df_period = getDataFromExcel("files//periods.xlsx", list(xls_struct[0]))
    df_period = df_period.rename(columns=xls_struct[0])
    df_rev = getDataFromExcel("files//revenew.xlsx", list(xls_struct[1]))
    df_rev = df_rev.rename(columns=xls_struct[1])
    df_exp = getDataFromExcel("files//expense.xlsx", list(xls_struct[2]))
    df_exp = df_exp.rename(columns=xls_struct[2])

    result = pd_concat([df_rev, df_exp], ignore_index=True, sort=False)
    result = result.loc[result['rev_treat'] == '"Договор 00000000052 от 25.01.2012 13:03:37"']
    result = pd_merge(result, df_period, on=["treat", "branch"], how="left")
    result = result.fillna(
        {"date": "01.01.2019 0:00:00", "pay_plan": 0, "pay_fact": 0, "revenue_plan": 0, "revenue_fact": 0}).fillna(
        "null")
    result = result.pivot_table(index=xls_struct[3], columns="date",
                                values=["pay_plan", "pay_fact", "revenue_plan", "revenue_fact"], fill_value=0,
                                margins=True,
                                aggfunc=sum)
    # result = result.swaplevel(0, 1, axis=1).sort_index(axis=1)
    result = result.reset_index()
    return result

# datestr = "23.08.2015 12:00:01"
# pat = re.compile("[0-9]")
# ismatch = re.match(re.compile("[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]"), datestr)


# columns = result.columns
# for col in columns:
#     print(col)

# df_to_excel(result,file="files//result.xlsx", template="files//contract_sketch.xlsx")


a = get_contract_report()
print(a)
