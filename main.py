class Account:
    def __init__(self, name, account_number, pincode):
        self.name = name
        self.account_number = account_number
        self.pincode = pincode
        self.balance = 0

    def deposit(self, amount):
        if amount % 5 == 0:
            self.balance += amount
        else:
            print("You entered a wrong amount.")
        return amount

    def withdrawal(self, amount):
        if amount % 5 == 0:
            if (self.balance - amount) >= 0:
                self.balance -= amount
            else:
                print(f"Your balance is not sufficient")
        else:
            print("You entered a wrong amount.")
        return amount

    def check_balance(self):
        print(f"The balance is: {self.balance}")

    def receipt(self):
        receipt = input("Do want a receipt of your transaction? Type 'Y' for yes or 'N' for no! ").lower()
        if receipt == "y":
            pass

    def change_pin(self):
        change = input("Do you really want to change your pincode? Type 'Y' for yes or 'N' for no! ").lower()
        if change == "y":
            self.pincode = input("Enter a 4 digit number: ")
        else:
            print("You are being redirected to the main menu")


# choices = {
#     'w': 'withdrawal',
#     'd': 'deposit',
#     'b': 'balance',
#     'c': 'cancel',
# }
#
# denominations = {
#     '€100': 200,
#     '€50': 200,
#     '€20': 200,
#     '€10': 200,
#     '€5': 200,
# }

client1 = Account("Henk van Houten", "123456", "1978")
client2 = Account("Jessica Reina", "123457", "1979")
client3 = Account("Collin van Houten", "123458", "2012")
client4 = Account("Ashly Pinzon", "123459", "1999")

client1.deposit(2525.00)
client1.withdrawal(32.00)
client1.check_balance()


    # print("Good morning/Good afternoon/Good evening, welcome to the ATM.\n")
    # print("We accept the following cards: maestro, mastercard, debit card")
    #
    # start = input("Enter your card and enter 'Go' to Start or 'Stop' to Quit: ").lower()
    # if start == "go":
    #     is_on = True
    # if start == "stop":
    #     is_on = False
    #     print("Have a nice day!")
    #
    # # Choice
    # if is_on:
    #     # Enter pincode
    #     print("\nPlease enter your pincode.")
    #     pincode = input("Pincode: ")
    #     if pincode in clients.values():
    #         print("\nHello", list(clients.keys())[list(clients.values()).index(pincode)] + "," + " Please Select Service.")
    #         choice = input("Enter ('W' for Withdrawal, 'D' for Deposit, 'B' for Balance, 'M' for Menu or 'E' for Exit): ").lower()
    #         if choice == "w":
    #             # Withdrawal (choice amount)
    #             withdrawal_amount = int(input("What amount do you want to withdrawal: "))
    #             if withdrawal_amount >= balance:
    #                 print(f"Withdrawal is not possible, you have insufficient funds. Your current balance is {balance}")
    #             else:
    #                 balance -= withdrawal_amount
    #                 print(f"Your new balance is EUR {balance}")
    #         elif choice == "d":
    #             deposit_amount = int(input("What amount do you want to deposit: "))
    #             balance += deposit_amount
    #         elif choice == "b":
    #             print(f"Your balance: EUR {balance}")
    #         elif choice == "m":
    #             print("Please wait for main menu")
    #         elif choice == "e":
    #             print("Goodbye!")
    #             is_on = False
    #         else:
    #             print("Wrong choice, please try again!")
    #     else:
    #         print("Pincode not recognized!")


    # Added the TODOs to Jira as requirements (User Stories) and tasks
