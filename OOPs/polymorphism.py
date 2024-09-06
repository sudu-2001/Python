class notification:
    def send(self,meaasge):
        pass

class email(notification):
    def send(self,message):
        print(f"message:{self.message}")

class whatsapp(notification):
    def send(self,message):
        count=0
        while count<4:

            print(f"message:{self.message}")
            count+=1

def send_notification(notification,message):
    notification.send(message)

em=email()
wa=whatsapp()

send_notification(em,"hi")
send_notification(wa,"hit")