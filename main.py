import datetime
import sqlite3
import pytz

db = sqlite3.connect('accounts.db')
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, account_number TEXT NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE TABLE IF NOT EXISTS security (account_number TEXT PRIMARY KEY NOT NULL, pincode TEXT NOT NULL)")
# create security

class Account:

    def current_time(self):
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name, account_number, pincode, balance=0):
        cursor = db.execute("SELECT name, account_number, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()
        if row:
            self.name, self.account_number, self.balance = row
        else:
            self.name = name
            self.account_number = account_number
            self.pincode = pincode
            self.balance = balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?, ?)", (name, account_number, balance))
            cursor.execute("INSERT INTO security VALUES(?, ?)", (account_number, pincode))
            cursor.connection.commit()

    def deposit(self, amount):
        if amount % 5 == 0:
            new_balance = self.balance + amount
            deposit_time = self.current_time()
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO transactions VALUES(?,?,?)", (deposit_time, self.name, amount))
            db.commit()
            self.balance = new_balance
        else:
            print("You entered a wrong amount.")
        return amount

    def withdrawal(self, amount):
        if amount % 5 == 0:
            if (self.balance - amount) >= 0:
                new_balance = self.balance - amount
                withdrawal_time = Account.current_time(self)
                db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
                db.execute("INSERT INTO transactions VALUES(?,?,?)", (withdrawal_time, self.name, -amount))
                db.commit()
                self.balance = new_balance
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
        change = input("Do you really want to change your pincode? Type 'Y' for yes or 'N' for no: ").lower()
        if change == "y":
            self.pincode = input("Enter a 4 digit number: ")
            db.execute("UPDATE security SET pincode = ? WHERE (account_number = ?)", (self.pincode, self.account_number))
            db.commit()
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

if __name__ == '__main__':

    #create accounts
    client1 = Account("Henk van Houten", "123456", "1978", 0)
    client2 = Account("Jessica Reina", "123457", "1979", 0)
    client3 = Account("Collin van Houten", "123458", "2012", 0)
    client4 = Account("Ashly Pinzon", "123459", "1999", 0)
    client5 = Account("Geert de Vries", "1234563", "1978", 0)

    # Check if a deposit gets stored? and if we get an error message if the wrong denominations are given
    client1.deposit(2500)
    client2.deposit(100)
    client3.deposit(23.45)

    # Check if a withdrawal is being processed and gets stored? and if we get an error message if we try to withdraw
    # more than we have
    client1.withdrawal(1000)
    client2.withdrawal(150)

    # Can a client change the pincode and does the new one gets stored?
    client1.change_pin()





    db.close()


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
