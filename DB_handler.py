import pandas as pd
import pandasql as ps

dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project1\\project_db_test_publish.xlsx"
raz_path = "project_db_test_publish.xlsx"


def retrieve():
    DB = pd.read_excel(raz_path)
    DB = DB.query("First_name  == 'Eyal'")
    DB = DB.query("Last_name == 'Rothman'")
    DB = DB.query("Valid_start_time == '2018-05-17 13:11'")
    DB = DB.query("Transaction_time <= '2020-05-21 10:00'")

    q1 = "select * from DB ORDER BY Transaction_time DESC LIMIT 1; "
    answer = ps.sqldf(q1, locals())
    return answer


def retrieve_history():
    pass
    # DB = pd.read_excel(dvir_path)
    # DB=DB.query("First_name  == 'Eyal'")
    # DB=DB.query("Last_name == 'Rothman'")
    # DB=DB.query("LOINC_NUM == '11218-5'")
    # DB=DB.query("Valid_start_time >= '2018-05-17 13:11'")
    # DB=DB.query("Valid_start_time <= '2018-05-17 13:11'")
    #
    #
    # q1="select * from DB ORDER BY Transaction_time DESC ; "
    # answer=ps.sqldf(q1, locals())
    # return answer


def delete():
    DB = pd.read_excel(dvir_path)
    q1 = "update DB set deleted=1" \
         " where Valid_start_time=='2018-05-17 13:11' and Transaction_time == '2020-05-21 10:00'"
    answer = ps.sqldf(q1, locals())


def update():
    DB = pd.read_excel(dvir_path)
    q1 = "insert into BD (First_name,Last_name,LOINC_NUM,Value,Unit,Valid_start_time,Transaction_time,deleted)" \
         ""
    answer = ps.sqldf(q1, locals())
    return answer


# print(update())
# print(delete())
print(retrieve())
# print(retrieve_history())
