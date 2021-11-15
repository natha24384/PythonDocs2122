# Nathan Green 
import basics
app = basics.newProgram()
user = basics.newUser()
app.balance = 1000

while app.running:
    print(app.balance)
    user.choice = input("1. deposit, 2. withdraw, 3. exit")
    if user.choice == "1":
        user.deposit = input("Enter however much you want to deposit.")
        user.deposit = int(user.deposit)
        app.balance += user.deposit
    elif user.choice == "2":
        user.withdraw = input("withdrawal as much as you want, or more accurately, as much as you have deposited already.")
        user.withdraw = int(user.withdraw)
        if user.withdraw > app.balance:
            print("That's way too much for somebody like you")
        else: app.balance -= user.withdraw
    elif user.choice == "3":
        print("leave then.")
        app.running = False
    else:
        print("That isn't an option, why'd you think that it would give you a serious response?")

