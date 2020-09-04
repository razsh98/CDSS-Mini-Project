import pandas as pd
import pandasql as ps
from UI_Elements import *
from datetime import datetime

dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project1\\project_db_test_publish.xlsx"
raz_path = "project_db_test_publish_1.xlsx"


def retrieve(first_name, last_name, valid_start_time, transaction_time,
             valid_start_time_end=None, limit=None, loinc_num=None):
    DB = pd.read_excel(raz_path)
    # DB = DB.query("First_name  == 'Eyal'")
    # DB = DB.query("Last_name == 'Rothman'")
    # DB = DB.query("Valid_start_time == '2018-05-17 13:11'")
    # DB = DB.query("Transaction_time <= '2020-05-21 10:00'")

    DB = DB.query("First_name == '" + first_name + "'")
    DB = DB.query("Last_name == '" + last_name + "'")
    filter_mask = DB['Transaction_time'] >= transaction_time
    DB = DB[filter_mask]

    if limit is None:
        try:
            filter_mask = DB['LOINC-NUM'] >= loinc_num
            DB = DB[filter_mask]

            filter_mask = DB['Valid_start_time'] >= valid_start_time
            DB = DB[filter_mask]

            filter_mask = DB['Valid_start_time'] <= valid_start_time_end
            DB = DB[filter_mask]
        except:
            DB = DB
        limit_clause = " ;"
    else:
        filter_mask = DB['Valid_start_time'] == valid_start_time
        DB = DB[filter_mask]
        limit_clause = "LIMIT " + str(limit) + " ;"

    q1 = "SELECT * FROM DB ORDER BY Transaction_time DESC " + limit_clause
    answer = ps.sqldf(q1, locals())
    return answer


def retrieve_history(first_name, last_name, valid_start_time, transaction_time):
    return retrieve(first_name, last_name, valid_start_time, transaction_time)


def delete(first_name="f", last_name="l", valid_start_time=None, transaction_time=None,
           valid_start_time_end=None, limit=None, loinc_num=None):
    before_update = retrieve(first_name, last_name, valid_start_time, transaction_time,
                             valid_start_time_end, limit, loinc_num)
    DB = pd.read_excel(raz_path)
    union_part_1 = pd.concat([DB, before_update, before_update]).drop_duplicates(keep=False)
    union_part_2 = before_update.replace(0, 1)
    union = pd.concat([union_part_1, union_part_2])
    union.to_excel('project_db_test_publish_1.xlsx', index=False)
    return union_part_2


def update(loinc_num, first_name="f", last_name="l", value="v", unit="none",
           valid_start_time="svt", transaction_time=datetime.now()):
    DB = pd.read_excel(raz_path)
    LOINC_NUM_DB = pd.read_csv('LoincTableCore.csv')
    component = LOINC_NUM_DB.query("LOINC_NUM == '" + loinc_num + "'")
    x = len(component)
    if not x == 1:
        show_alert(title="bad loinc num", info="the given loinc number didnt typed well ")
        return ""
    component = component['COMPONENT'].to_list()[0]
    new_row = [loinc_num, first_name, last_name, value, unit, valid_start_time, transaction_time, 0, component]
    DB.loc[len(DB)] = new_row
    DB.to_excel('project_db_test_publish_1.xlsx', index=False)
    return new_row
