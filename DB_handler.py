import pandas as pd
import pandasql as ps

dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project1\\project_db_test_publish.xlsx"
raz_path = "project_db_test_publish.xlsx"


def retrieve(first_name, last_name, valid_start_time, transaction_time, limit=None):
    DB = pd.read_excel(raz_path)
    # DB = DB.query("First_name  == 'Eyal'")
    # DB = DB.query("Last_name == 'Rothman'")
    # DB = DB.query("Valid_start_time == '2018-05-17 13:11'")
    # DB = DB.query("Transaction_time <= '2020-05-21 10:00'")

    DB = DB.query("First_name == '" + first_name + "'")
    DB = DB.query("Last_name == '" + last_name + "'")
    DB = DB.query("Valid_start_time >= '" + valid_start_time + "'")
    DB = DB.query("Transaction_time >= '" + transaction_time + "'")

    if limit is None:
        limit_clause = " ;"
    else:
        limit_clause = "LIMIT " + limit + " ;"

    q1 = "SELECT * FROM DB ORDER BY Transaction_time DESC " + limit_clause
    answer = ps.sqldf(q1, locals())
    return answer


def retrieve_history(first_name, last_name, valid_start_time, transaction_time):
    return retrieve(first_name, last_name, valid_start_time, transaction_time)


def delete():
    DB = pd.read_excel(dvir_path)
    q1 = "UPDATE DB SET deleted=1" \
         " WHERE Valid_start_time=='2018-05-17 13:11' AND Transaction_time == '2020-05-21 10:00'"
    answer = ps.sqldf(q1, locals())


def update():
    DB = pd.read_excel(dvir_path)
    q1 = "insert into DB (First_name,Last_name,LOINC_NUM,Value,Unit,Valid_start_time,Transaction_time,deleted)" \
         ""
    answer = ps.sqldf(q1, locals())
    return answer
