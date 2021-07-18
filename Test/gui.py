from tkinter import *
import mongodb_jhtest as mdbjht

def display_data():
	all_tickets_list = mdbjht.read_from_mongodb()
	
	scrollbar = Scrollbar(window)
	scrollbar.pack( side = RIGHT, fill = Y )

	scrollbar1 = Scrollbar(window, orient = HORIZONTAL)
	scrollbar1.pack( side = BOTTOM, fill = X )

	mylist = Listbox(window, yscrollcommand = scrollbar.set, xscrollcommand = scrollbar1.set )
	mylist.config(width=500, height=10, font = 50)

	#mystring = ""
	counter = 0#To help style the gui list
	print("*\n****List of intents fetched from mongoDB ******\n**")
	for ticket in all_tickets_list:
		print("*\n****Intent ******\n**" + str(counter))
		print(ticket.to_json())
		
		#mystring += "*\n*"
		#mystring += str(ticket.to_json())
		mylist.insert(END, ticket.to_json())
		#Create alternating colours for each ticket in the gui
		if (counter%2 == 0):
			mylist.itemconfig(counter, bg='lightblue')
		counter+=1 



	mylist.pack( side = LEFT, fill = BOTH )
	scrollbar.config( command = mylist.yview )
	scrollbar1.config( command = mylist.xview )

	print("*\n**** END of fetch from mongoDB ******\n**")

	#text = Label(window, width = 200, wraplength = 800, text = mystring)
	#text.pack()

#Get user input
'''def submit():
	entered_id = entry.get()
	return entered_id'''

#To display ticket by id passed
def display_single_ticket():
	ticket = mdbjht.read_from_mongodb_by_id(entry.get())#Pass the user input as id
	scrollbar1 = Scrollbar(window, orient = HORIZONTAL)
	scrollbar1.pack( side = BOTTOM, fill = X )

	mylist = Listbox(window, xscrollcommand = scrollbar1.set )
	mylist.config(width=500, height=10)

	mylist.insert(END, ticket.to_json())

	mylist.pack( side = LEFT, fill = BOTH )
	scrollbar1.config( command = mylist.xview )


window = Tk()
window.geometry('800x500')
window.title("JH Interview Assignment")

#Create a button to display the data
button = Button(window, text = 'Display All Data')
#Call the function on button click command
button.config(command=display_data)
button.pack()

text = Label(window, text = "Enter ID of the ticket to display below")
text.pack()
entry = Entry(window)
entry.pack()

button2 = Button(window, text = 'Display Data for Ticket Id')
button2.config(command=display_single_ticket)
button2.pack()

text = Label(window, text = "On clicking a button, rows representing the details per each ticket display below. Please restart the app for each button operation")
text.pack()

mylist = Listbox(window)

#Display the window
window.mainloop()