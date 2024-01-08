# create a function that takes a name as an argument
# returns a new string that says hello and then the name
# that was the arguement
# Then use this function and ask the user for their name
# and tell them greetings

print("Here at Himothy University")

name = "Oliver"
print("Hello", name)
print("Welcome to Himothy Unveristy" + " " + name )

def say_hello_print(users_name):
    print("Howdy " + users_name)

say_hello_print("Oliver")
print(say_hello_print("Oliver")) # has the value of none
def say_hello_return(users_name):
    return "Greetings to being him" + " " + users_name
say_hello_return("Neal") # "Greetings to being him Neal"
print(say_hello_return("Neal"))

#### THIS IS THE ANSWER TO PROBLEM
print("Here is the answer below")

users_name = input("Tell me your name: ")
# print("Welcome to Himothy Univeristy", users_name)
print(say_hello_return(users_name))