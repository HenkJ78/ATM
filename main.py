# Starting menu
balance = 50000  # balance client
atm = 0

clients = {
    "Henk van Houten": "1978",
    "Jessica Reina": "1979",
    "Collin van Houten": "2012",
    "Ashly Pinzon": "1999"
}

choices = {
    'w': 'withdrawal',
    'd': 'deposit',
    'b': 'balance',
    'c': 'cancel',
}

denominations = {
    '€100': 200,
    '€50': 200,
    '€20': 200,
    '€10': 200,
    '€5': 200,
}

print("Good morning/Good afternoon/Good evening, welcome to the ATM.\n")
print("We accept the following cards: maestro, mastercard, debit card")

start = input("Enter your card and enter 'Go' to Start or 'Stop' to Quit: ").lower()
if start == "go":
    is_on = True
if start == "stop":
    is_on = False
    print("Have a nice day!")

# Choice
if is_on:
    # Enter pincode
    print("\nPlease enter your pincode")
    pincode = input("Pincode: ")
    if pincode in clients.values():
        print("\nHello", list(clients.keys())[list(clients.values()).index(pincode)] + "," + " Please Select Service.")
        choice = input("Enter ('W' for Withdrawal, 'D' for Deposit, 'B' for Balance, 'M' for Menu or 'E' for Exit): ").lower()
        if choice == "w":
            # Withdrawal (choice amount)
            withdrawal_amount = int(input("What amount do you want to withdrawal: "))
            if withdrawal_amount >= balance:
                print(f"Withdrawal is not possible, you have insufficient funds. Your current balance is {balance}")
            else:
                balance -= withdrawal_amount
                print(f"Your new balance is EUR {balance}")
        elif choice == "d":
            deposit_amount = int(input("What amount do you want to deposit: "))
            balance += deposit_amount
        elif choice == "b":
            print(f"Your balance: EUR {balance}")
        elif choice == "m":
            print("Please wait for main menu")
        elif choice == "e":
            print("Goodbye!")
            is_on = False
        else:
            print("Wrong choice, please try again!")
    else:
        print("Pincode not recognized!")

# print()
# # Wait
# print("Please wait")
#
# # Take out debit card
# print("Please take out your debit card.")
#
# # processing the money
# print("Please wait, your withdrawal is being processed.")
#
# # Take out money
# print("Please take out your money.")
#
# # receipt
# receipt = input("Do you want a receipt? Press 'Y' or 'N' ").lower()
# if receipt == "y":
#     print("Please wait for receipt.\n")
#
# # ready
# print("Have nice day! Till next time.")

# TODO: If pincode is wrong, ask to enter another time or 'Q' to quit
# TODO: After choice gif it the option to make another choice
# TODO: Amount of cash available in atm
# TODO: Print a greeting based on time a day
# TODO: Change withdrawal. Ask for bill choice and adjust amount in denominations
# TODO: Report - Ask for denominations
# TODO: Create clients and check for pincode and balance e.d.
# Error: show message and number of company which can be called
# Maintenance
# Keep track of the current amount of bills. If almost empty send message to fill
# TODO: Application with Flask or Django
