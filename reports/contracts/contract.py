from excel_app import getDataFromExcel
from pandas import concat as pd_concat
from pandas import merge as pd_merge
from openpyxl import load_workbook
from openpyxl.comments import Comment
from copy import copy

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
        "Дох_Контрагент": "treat_client",
        "Дох_ИНН": "treat_inn",
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
        "Расх_Тип": "treat_type",
        "Расх_Контрагент": "exp_client",
        "Расх_ИНН": "treat_inn",
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

def mapping_df_xls():
    dct = {
        'A': ('branch', ''),
        'B': ('treat_client', ''),
        'J': ('treat_inn', ''),
        'D': ('treat_num', ''),
        'E': ('treat_date', ''),
        'F': ('treat_end_date', ''),
        'G': ('treat_object', ''),
        'H': ('treat_type', ''),
        'I': ('exp_client', ''),
        'K': ('exp_num', ''),
        'L': ('exp_date', ''),
        'M': ('treat_amount', ''),
        'N': ('amount_done_on_begin', ''),
        'O': ('amount_on_begin', ''),
        'P': ('pay_on_begin', '')
        # ,
        # ('amount_done_on_begin', ''): '',
        # ('amount_on_begin', ''): '',
        # ('pay_on_begin', ''): '',
        # ('amount_done_on_end', ''): '',
        # ('amount_on_end', ''): '',

    }
    return dct

def df_to_excel(table, file="", template="", columns=None):
    lw = load_workbook(template)
    lw_sheet = lw.active
    """header style"""
    header_style = copy(lw_sheet["M2"]._style)
    header_num_style = copy(lw_sheet["M3"]._style)
    header_need = True
    """resources """
    resources = {
        "revenue_plan": "Выручка\nплан.",
        "revenue_fact": "Выручка\nфакт",
        "pay_plan": "Оплата\nфакт",
        "pay_fact": "Оплата\nфакт"
    }
    resource_column = 17
    row_start = 4
    for df_row in table.iterrows():
        """static fields"""
        for key, value in columns.items():
            new_row = lw_sheet[f"{key}{row_start}"]
            df_curr_row = df_row[1]
            new_row.value = df_curr_row[value]
        lw_sheet[f"A{row_start}"].comment = Comment(f"{df_row[0][0]}\n{df_row[0][1]}", "user", height=50, width=350)

        """pivot and the end"""
        """header"""

        if header_need:
            for key, value in resources.items():
                for idx in df_row[1][key].items():
                    """header"""
                    new_header_cell = lw_sheet.cell(2, resource_column)
                    new_header_cell.value = f"{value}\n{idx[0]}"
                    new_header_cell._style = header_style
                    """header number"""
                    new_num_header_cell = lw_sheet.cell(3, resource_column)
                    new_num_header_cell.value = resource_column
                    new_num_header_cell._style = header_num_style
                    resource_column += 1
                    """values"""
        """rows"""

        header_need = False

        row_start += 1
    lw.save(file)

def get_contract_report():
    xls_struct = get_xls_struct()
    df_period = getDataFromExcel("files//periods.xlsx", list(xls_struct[0]))
    df_period = df_period.rename(columns=xls_struct[0])
    df_rev = getDataFromExcel("files//revenew.xlsx", list(xls_struct[1]))
    df_rev = df_rev.rename(columns=xls_struct[1])
    df_exp = getDataFromExcel("files//expense.xlsx", list(xls_struct[2]))
    df_exp = df_exp.rename(columns=xls_struct[2])

    """union and merge table"""
    df_result = pd_concat([df_rev, df_exp], ignore_index=True, sort=False)
    # df_result = df_result.loc[result['rev_treat'] == '"Договор 00000000052 от 25.01.2012 13:03:37"']
    df_result = pd_merge(df_result, df_period, on=["treat", "branch"], how="left")
    df_result = df_result.fillna(
        {"date": "01.01.2019 0:00:00", "pay_plan": 0, "pay_fact": 0, "revenue_plan": 0, "revenue_fact": 0}).fillna(
        '')
    """building pivot table"""
    df_result = df_result.pivot_table(index=xls_struct[3], columns="date",
                                      values=["pay_plan", "pay_fact", "revenue_plan", "revenue_fact"], fill_value=0,
                                      margins=True,
                                      aggfunc=sum)
    """removing the last row with totals"""
    df_result = df_result[:-1]
    """to swipe columns"""
    # result = result.swaplevel(0, 1, axis=1).sort_index(axis=1)
    """reseting and building a new hierarchy indexes"""
    df_result = df_result.reset_index()
    df_result = df_result.set_index(['rev_treat', 'exp_treat']).sort_index()

    df_to_excel(df_result, "files//result.xlsx", "files//contract_sketch.xlsx", mapping_df_xls())

    return df_result

result = get_contract_report()

# df_to_excel(result, "files//result.xlsx", "files//contract_sketch.xlsx")

# datestr = "23.08.2015 12:00:01"
# pat = re.compile("[0-9]")
# ismatch = re.match(re.compile("[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]"), datestr)

# df_to_excel(result,file="files//result.xlsx", template="files//contract_sketch.xlsx")

#
# app = Flask(__name__)
# if __name__ == "__main__":
#     app.run()
