#This program  says hello word and ask for my name

print("Hello world")
print("What is your name?")
myName = input()
print("Your name is: " + myName)
print("The lenght of your name is: " + str(len(myName)))
print("What is your age?")
myAge=input()
print("Your age is: " + str(myAge))
print("You will be " + str( int(myAge) + 1) + " in a year.")