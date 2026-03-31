# property ----> variable
# methods  ----> functions

# INHERITANCE
class netflixPakage:
    def __init__(self, pakage_id, plan, total_payment):
        self.id = pakage_id
        self.plan = plan
        self.payment = total_payment

    def subscribe(self):
        print(f"User with {self.id} id subscribe to {self.plan} plan")
    def unsubscribe(self):
        print(f"User with {self.id} unsubscribe the {self.plan} plan")

        # netflix = netflixPakage(13545, "monthly", 100)
        # netflix.plan
        # netflix.subscribe()

class premium_netflix(netflixPakage):
    def __init__(self, pakage_id, plan, total_payment, screens):
        super().__init__(pakage_id, plan, total_payment)
        self.screen = screens

    def max_screen(self, screens):
        self.screen = screens
        print(f"Maximum screen set to {self.screen} screens in premium plan")

        # netflix = premium_netflix(667677, "weekly", 100, 90)
        # netflix.subscribe()
        # netflix.max_screen(5)