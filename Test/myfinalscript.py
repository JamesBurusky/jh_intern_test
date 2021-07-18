import pandas as pd

#Access the excel document
xls = pd.ExcelFile('interview_assignment.xlsx')
#Read data from either of the sheets
df_m = pd.read_excel(xls, 'Messages')
df_s = pd.read_excel(xls, 'Subjects')


unique_tickets_list = []
#iterate the data for rows and columns
for s_row, s_columns in df_s.iterrows():
	#Reser the unique_tickets to empty to avoid reassigning of keys
	unique_tickets = {}
	s_ticket_id = s_columns.ticket_id
	#print('"@@@@Ticket_id" : ' + str(s_columns.ticket_id))
	#Store the ticket id, Subject, Phone number, Intents, incoming and outgoing messages in the unique_tickets dictionary
	unique_tickets["Ticket_id"] = (s_columns.ticket_id)
	#print('"Subject" : "' + str(s_columns.subject)[16:] + '"')
	unique_tickets["Subject"] =  str(s_columns.subject)[16:] 
	#print('"Phone Number" : "' + str(s_columns.subject)[4:14] + '"')
	unique_tickets["Phone Number"] = str(s_columns.subject)[4:14]
	intents = []
	unique_tickets["Intents"] = intents
	incoming_messages = []
	outgoing_messages = []
	
	for m_row, m_columns in df_m.iterrows():
		m_ticket_id = m_columns.ticket_id

		#print('********Checking for each row in mesages usig unique tickets')
		if (m_ticket_id == s_ticket_id):
			if "Detected intent" in (m_columns.body_text):
				#print('"Intent" : "' + str(m_columns.body_text)[16:].split('(')[0] + '"')
				intents.append(str(m_columns.body_text)[16:].split('(')[0])
			else:
				#print("No intent detected!")
				#unique_tickets["Detected intent"] = 'No intent detected!'
				intents.append("No intent detected!")

			##Reset the message_details dictionary to empty to avoid reassigning of keys
			message_details = {}
			#print(m_columns.incoming)
			#print(m_columns.id)
			if str(m_columns.incoming) == "True":
				#print(str(m_columns.id))
				#Assign the folloeing keys to message_details dictionary
				message_details["Message Content"] = str(m_columns.body_text).split(')')[-1]
				message_details["Id"] = m_columns.id
				message_details["User ID"] = m_columns.user_id
				message_details["Date Time"] = str(m_columns.created_at)
				#print(message_details)

				#Add the dictionary to incoming_messages list before iterating next row to avoid dictionary being overwritten
				incoming_messages.append(message_details)

			else:
				message_details["Message Content"] = str(m_columns.body_text).split(')')[-1]
				message_details["Id"] = m_columns.id
				message_details["User ID"] = m_columns.user_id
				message_details["Date Time"] = str(m_columns.created_at)

				outgoing_messages.append(message_details)

			#Store the incoming and outgoing messages in the unique_tickets dictionary
			unique_tickets["Incoming Messages"] = incoming_messages
			unique_tickets["Outgoing Messages"] = outgoing_messages

	#Before checking next row, add the dictionary in the unique_tickets_list
	unique_tickets_list.append(unique_tickets)
print("*\n****Here is the output for task Number 1 ******\n**")
print(unique_tickets_list)
print("*\n****END of output for task Number 1 ******\n**")
ticketslist_output = unique_tickets_list
		


	