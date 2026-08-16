class Notification:

    def send(self, message):
        print("Sending notification:", message)


class EmailNotification(Notification):

    def send(self, message):
        print("Email:", message)


class SMSNotification(Notification):

    def send(self, message):
        print("SMS:", message)


class PushNotification(Notification):

    def send(self, message):
        print("Push Notification:", message)


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

message = "Your order has been delivered."

for notification in notifications:

    notification.send(message)