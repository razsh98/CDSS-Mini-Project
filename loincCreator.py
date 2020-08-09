import pandas as pd


df1 = pd.read_csv("C://Users//Dvir Levi//Desktop//MDSS//Mini-Project//LoincTableCore.csv")
df2 = pd.read_excel("C://Users//Dvir Levi//PycharmProjects//CDSS-Mini-Project//project_db_test_publish.xlsx")
# print(df2.columns)
result = df2.set_index('LOINC_NUM').join(df1.set_index('LOINC_NUM'))
#print(result)
result.to_excel("project_db_test_publish_1.xlsx")