import pandas as pd

xls = pd.ExcelFile('interview_assignment.xlsx')
df_m = pd.read_excel(xls, 'Messages')
df_s = pd.read_excel(xls, 'Subjects')
print('Messages: \n')
print(df_m.head())
print('\n Subjects: \n')
print(df_s.head())

print(df_m.loc[df_m['ticket_id']==2])
df_tick = df_m.loc[df_m['ticket_id']==2, ['body_text', 'id', ]]
print(df_tick.to_dict())

for row, columns in df_s.iterrows():
	print(row)
	print(columns)
	print('"Ticket_id" : ' + str(columns.ticket_id))
