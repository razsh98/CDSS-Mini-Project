import pandas as pd
import pandasql as ps

dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project1\\project_db_test_publish.xlsx"
raz_path = "C:/_Information Systems Engineering/_Senior Year/Semester H/Decision Support Systems in Medicine/" \
           "Assignments/Mini Project/project_db_test_publish.xlsx"


def retrive():
    DB = pd.read_excel(dvir_path)
    DB=DB.query("First_name  == 'Eyal'")
    DB=DB.query("Last_name == 'Rothman'")
    DB=DB.query("Valid_start_time == '2018-05-17 13:11'")
    DB=DB.query("Transaction_time <= '2020-05-21 10:00'")

    q1="select * from DB ORDER BY Transaction_time DESC LIMIT 1; "
    answer=ps.sqldf(q1, locals())
    return answer

def retrive_history():
    DB = pd.read_excel(dvir_path)
    DB=DB.query("First_name  == 'Eyal'")
    DB=DB.query("Last_name == 'Rothman'")
    DB=DB.query("Valid_start_time == '2018-05-17 13:11'")
    DB=DB.query("Transaction_time <= '2020-05-21 10:00'")

    q1="select * from DB ORDER BY Transaction_time DESC LIMIT 1; "
    answer=ps.sqldf(q1, locals())
    return answer


retrive()