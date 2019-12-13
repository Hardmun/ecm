from unittest import result
from excel_app import getDataFromExcel
from pandas import concat as pd_concat
from pandas import merge as pd_merge
from openpyxl import load_workbook
from openpyxl.comments import Comment
from openpyxl.styles import PatternFill
from io import BytesIO
from copy import copy
import re



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
        'C': (),
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
    }
    return dct

def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def get_quarter(month):
    return (int(month) - 1) // 3 + 1

def user_format(frm_value):
    pattern = re.compile("[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]")
    ismatch = re.match(pattern, frm_value)
    if ismatch != None:
        date_str = frm_value[0:10].split(".");
        result_frm = f"{get_quarter(date_str[1])} кв. {date_str[2]} г."
    elif frm_value == "All":
        result_frm = "Всего"
    else:
        result_frm = frm_value
    return result_frm

def df_to_excel(table, file="", template="", columns=None):
    lw = load_workbook(template)
    lw_sheet: Worksheet = lw.active
    """dynamic column starts"""
    dyn_col = 17
    """header style"""
    header_style = copy(lw_sheet["M2"]._style)
    header_num_style = copy(lw_sheet["M3"]._style)
    fill_pattern_blue = PatternFill(start_color='CCFFFF', end_color='CCFFFF', fill_type='solid')
    header_need = True
    """resources """
    resources = {
        "revenue_plan": "Выручка\nплан.",
        "revenue_fact": "Выручка\nфакт",
        "pay_plan": "Оплата\nплан",
        "pay_fact": "Оплата\nфакт"
    }
    """end"""
    end_colm = {
        ('amount_done_on_end', ''): 'Выполнено на конец',
        ('amount_on_end', ''): 'Остаток не сданных работ на конец'
    }

    resource_column = dyn_col
    grouping_clm = dyn_col
    grouping_list = []
    row_start = 4
    last_row = len(table.index) - row_start
    grouping_row = row_start + 1;
    for df_row in table.iterrows():
        """define revenue contract"""
        is_rev = df_row[0][1] == ""
        """static fields"""
        for key, value in columns.items():
            new_row = lw_sheet[f"{key}{row_start}"]
            df_curr_row = df_row[1]
            if is_rev:
                new_row.fill = fill_pattern_blue
            new_row.number_format = 'General'
            if value != ():
                new_row.value = df_curr_row[value]

        lw_sheet[f"A{row_start}"].comment = Comment(f"{df_row[0][0]}\n{df_row[0][1]}", "user", height=50, width=350)

        """pivot and the end"""
        """header"""
        if header_need:
            for key, value in resources.items():
                for idx in df_row[1][key].items():
                    """header"""
                    new_header_cell = lw_sheet.cell(2, resource_column)
                    new_header_cell.value = f"{value}\n{user_format(idx[0])}"
                    new_header_cell._style = header_style
                    """header number"""
                    new_num_header_cell = lw_sheet.cell(3, resource_column)
                    new_num_header_cell.value = resource_column
                    new_num_header_cell._style = header_num_style
                    resource_column += 1
                    # grouping_clm += 1
                """grouping totals"""
                num_added_clm = (resource_column - grouping_clm)
                if num_added_clm > 1:
                    # lw_sheet.column_dimensions.group(colnum_string(grouping_clm),
                    #                                  colnum_string(grouping_clm + num_added_clm - 2))
                    grouping_list.append((colnum_string(grouping_clm), colnum_string(grouping_clm + num_added_clm - 2)))
                    grouping_clm = grouping_clm + num_added_clm
        """rows"""
        column_for_rows = dyn_col
        for key in resources:
            for idx in df_row[1][key].items():
                new_row_cell = lw_sheet.cell(row_start, column_for_rows)
                new_row_cell.value = idx[1]
                new_row_cell.number_format = 'General'
                if is_rev:
                    new_row_cell.fill = fill_pattern_blue
                column_for_rows += 1

        """end"""
        """header"""
        if header_need:
            column_for_rows_end = resource_column
            for key, value in end_colm.items():
                new_header_cell = lw_sheet.cell(2, resource_column)
                new_header_cell.value = value
                new_header_cell._style = header_style
                """header number"""
                new_num_header_cell = lw_sheet.cell(3, resource_column)
                new_num_header_cell.value = resource_column
                new_num_header_cell._style = header_num_style
                resource_column += 1
        """rows"""
        column_for_rows = column_for_rows_end
        for key in list(end_colm.keys()):
            new_row_cell = lw_sheet.cell(row_start, column_for_rows)
            df_curr_row = df_row[1]
            new_row_cell.value = df_curr_row[key]
            new_row_cell.number_format = 'General'
            if is_rev:
                new_row_cell.fill = fill_pattern_blue
            column_for_rows += 1

        header_need = False
        row_start += 1
        """grouping row"""
        if is_rev:
            lw_sheet.row_dimensions.group(grouping_row, row_start - 1)
            grouping_row = row_start
    """other styles"""
    """column size"""
    lw_sheet.auto_filter.ref = lw_sheet.dimensions
    for col_num in range(dyn_col, resource_column):
        lw_sheet.column_dimensions[colnum_string(col_num)].width = 14
    """fix A2"""
    lw_sheet.freeze_panes = lw_sheet.cell(3, 1)
    """grouping"""
    for grpcol in grouping_list:
        lw_sheet.column_dimensions.group(grpcol[0], grpcol[1])
    """grouping rows"""
    


    # bt = BytesIO()
    lw.save(file)
    # lw.save(bt)

    # with open("233.xlsx","wb") as binarysave:
    #     binarysave.write(bt.getvalue())


    # with NamedTemporaryFile(mode='wb',delete=False) as tmp:
    #     lw.save(tmp.name)
    #     sadf=0;
    #     tmp.close()

    # with open("files//result.xlsx","rb") as tmp:
    #     asdf=0
        # with open("1.xlsx", "wb") as ex:
        #     for line in tmp:
        #         ex.write(line)

    # return bt

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
    # df_result = df_result.loc[df_result['rev_treat'] == '"Договор 00000003129 от 29.05.2015 12:00:00"']
    df_result = pd_merge(df_result, df_period, on=["treat", "branch"], how="left")
    df_result = df_result.fillna(
        {"date": "01.01.2019 0:00:00", "pay_plan": 0, "pay_fact": 0, "revenue_plan": 0, "revenue_fact": 0}).fillna(
        '')
    """building pivot table"""
    df_result = df_result.pivot_table(index=xls_struct[3], columns="date",
                                      values=["pay_plan", "pay_fact", "revenue_plan", "revenue_fact"], fill_value='',
                                      margins=True,
                                      aggfunc=sum).replace(0, '')
    """removing the last row with totals"""
    df_result = df_result[:-1]
    """to swipe columns"""
    # result = result.swaplevel(0, 1, axis=1).sort_index(axis=1)
    """reseting and building a new hierarchy indexes"""
    df_result = df_result.reset_index()
    df_result = df_result.set_index(['rev_treat', 'exp_treat']).sort_index()

    """format values(need to rebuild later)"""
    df_result['treat_date'] = df_result['treat_date'].apply(lambda x: "{:.10}".format(x))
    df_result['treat_end_date'] = df_result['treat_end_date'].apply(lambda x: "{:.10}".format(x))
    df_result['exp_date'] = df_result['exp_date'].apply(lambda x: "{:.10}".format(x))

    """creating excel file"""
    # df_to_excel(df_result, "files//result.xlsx", "files//contract_sketch.xlsx", mapping_df_xls())

    # return df_result
    """testing"""
    return df_to_excel(df_result, "files//result.xlsx", "files//contract_sketch.xlsx", mapping_df_xls())

rslt = get_contract_report()
asdf=0
# with open("files//result.xlsx","rb") as bn:
#     bn.write()

# df_to_excel(result, "files//result.xlsx", "files//contract_sketch.xlsx")

# datestr = "23.08.2015 12:00:01"
# pat = re.compile("[0-9]")
# ismatch = re.match(re.compile("[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]"), datestr)

# df_to_excel(result,file="files//result.xlsx", template="files//contract_sketch.xlsx")

#
# app = Flask(__name__)
# if __name__ == "__main__":
#     app.run()
