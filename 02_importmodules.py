# import modules to use the modules codes
import basics

# make new application object from basics
app = basics.newProgram()
# use method of new application object
app.print('yeah')

# print property of new application object
app.print( app.debugging )

# this line wont print if app.debugging is false
app.debug("hello")

# enable debbuging for application

app.debugging = True
app.debug('That should work')

# import a default python module
import random

# use a random module method 
randomNumber = random.randint(1, 10)
app.print(randomNumber)
