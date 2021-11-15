#Nathan
# practice using expresions and conditional statements

#an expresion is a problem that must be solved
# 5 + 5 is an arithmetic expression 
x = 5 + 5

#function/methods must be resolved as expresions as well
answer = input("What is your name?")

#comparison expressions resolve as true/false

print(7>8)
print(7>2)
print(x == 10)

#conditiona statement runs if its condition isnt false
if answer == "bob":
    print("Hello, bob! Welcome back!")
    print ("This line also prints if youre bob")
elif answer == "vadim":
    print("who let this guy in?")
    
else:
    print ("bob is gone")
    
print("This line isnt inside the if statement so it prints anyway.")

# ^ If checks a conditiom
# ^ Elif checks a condition of previous cpnditions werent true
# ^ you can have several elifs
#^ else runs if no prior conditions were true
