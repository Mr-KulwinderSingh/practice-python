# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def greet(name):
    print("Hey there!")
    print("welcome, " + name)




greet("Sonu")

def say_heloo(sam):
    print("Hello!, " + sam)
    print("Welcome to the coding school")

sam = "Kulwinder Singh"
say_heloo(sam)


def not_welcome(name):
    if name == "Sham":
        print("You are not welcome in my house")
        return 

not_welcome("Sham")


# shorter code, return and print

def short_code(name):
    if name == "Mimi":
        return "Welcome to Dun Darrach"
    return "You are very welcome to county Longford"

print(short_code("Mimi"))