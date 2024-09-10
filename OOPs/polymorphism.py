class notification:
    def send(self,message):
        pass

class email(notification):
    def send(self, message):
        print(f"message is :{message}")

class whatsapp(notification):
    def send(self,message):
        print(f"messgae is:{message}")

def notify(lang,message):
    lang.send(message)

em=email()
what=whatsapp()

notify(em,"hi")
notify(what,"ji")