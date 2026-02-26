# Variables
name = "GSoC"
year = 27
is_ready = True

print(name)
print(year)
print(is_ready)

# Basic Math
a = 13
b = 3
print(a+b)
print(a-b)
print(a * b)
print(a / b)
print(a // b) # floor division
print(a % b) 
print(a ** b) # power

# Strings
full = "I will crack " + name + " " + str(year)
print(full)

# Taking Input
user = input("Enter your name: ")
print("Hello " + user)
print("The length of your name is: ")
print(len(user))

print("What is your age ?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")