# 8. Basic ATM Menu
balance = 1000
choice = 2

match choice:
    case 1:
        print("Balance:", balance)
    case 2:
        print("Withdraw selected")
    case 3:
        print("Deposit selected")
    case 4:
        print("Thank you!")
    case _:
        print("Invalid option")