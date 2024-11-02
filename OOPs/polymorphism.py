class notification:

	def sendmessage(self,message):

		pass

class Email(notification):

	def sendmessage(self,message):

		print(f"Hi, buddy there is notification:{message}")

class whatsapp(notification):

	def sendmessage(self,message):

		print(f"Hi, this is whatsapp:{message}")

def notify(lang,message):

	lang.sendmessage(message)

em=Email()

wh=whatsapp()

notify(wh,"Whatsapp Update!!")

notify(em,"This is from Organization")
