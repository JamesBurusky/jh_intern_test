import mongoengine as db

import myfinalscript as mfs

database_name = "jhtest"
password = "kaburusky"

DB_URI = "mongodb+srv://kaburusky:{}@cluster0.y8u7a.mongodb.net/{}?retryWrites=true&w=majority".format(password, database_name)

db.connect(host = DB_URI)

#By default the name of the class is the name of the collection converted to lowercase
class Tickets(db.Document):
	ticket_id = db.IntField()
	subject = db.StringField()
	phone_number = db.StringField()
	intents = db.ListField()
	incoming_messages = db.ListField()
	outgoing_messages = db.ListField()

	def to_json(self):
		return {
			"ticket_id": self.ticket_id,
			"subject": self.subject,
			"phone_number": self.phone_number,
			"intents": self.intents,
			"incoming_messages": self.incoming_messages,
			"outgoing_messages": self.outgoing_messages
		}

tickets = mfs.ticketslist_output
#print(tickets[0])
#ticket_detail = tickets[0]


def commit_to_mongodb():
	for ticket_detail in tickets:
		ticket = Tickets(
			ticket_id = ticket_detail["Ticket_id"],
			subject = ticket_detail["Subject"],
			phone_number = ticket_detail["Phone Number"],
			intents = ticket_detail["Intents"],
			incoming_messages = ticket_detail["Incoming Messages"],
			outgoing_messages = ticket_detail["Outgoing Messages"]
		)
		print("*\n Ticket Created \n*")
		print("Commit the Ticket")
		ticket.save()
		print("*\n Ticket Committed \n*")

def read_from_mongodb():
	all_ticket = Tickets.objects().all()
	print(all_ticket.to_json())
	return all_ticket

def read_from_mongodb_by_id(id: int):
	ticket = Tickets.objects(ticket_id=id).all()
	#print(ticket.to_json())
	return ticket

def update_ticket_in_mongodb(id: int, phone: str):
	print("*\n Update Ticket \n*")
	ticket = Tickets.objects(ticket_id=id).first()
	ticket.update(phone_number = phone)

#commit_to_mongodb()
#read_from_mongodb()
#update_ticket_in_mongodb(9, "0705052243")
#read_from_mongodb_by_id(9)


"""for i in tickets:
	print(i)
	print("*\n*")
	print("*\n Create a Ticket \n*")
	ticket = Tickets(
		ticket_id=1,
		name = "A Game of Thrones",
		author = "James Mwenda"
		)
	print("*\n Ticket Created \n*")"""

"""print("Commit the Ticket")
ticket.save()
print("*\n Ticket Committed \n*")

print("*\n Fetch a Ticket \n*")
#Fetch all
all_ticket = Tickets.objects(ticket_id=1).all()
#In the objects filter the objects based on that parameter ie the first match in this case
ticket = Tickets.objects().first()
print("*\n Ticket Fetched \n*")
print(all_ticket.to_json())

print("*\n Update Ticket \n*")
ticket.update(name = "My new Book", author = "Me Myself and I")
print(ticket.to_json())"""
