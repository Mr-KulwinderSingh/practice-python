

import colorama 
from colorama import Fore, Back, Style 
colorama.init(autoreset= True)
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


import math

print("Welcome to the Body_Mass_Index!\n")
print("As per the modern life style, and living in the world of technology")
print("every person needs to know what category of BMI he is in\n")

start = input("To start please type yes\n ")

if start.lower() != "yes":
    quit()


def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = '-' * int(percent) + '-' * (100 - int(percent) )
    print(color + f"\r | {bar}| {percent:.25f}%", end="\r ")
    if progress == 'total':
        print(colorama.Fore.GREEN + f"\r | {bar}| {percent:.25f}%", end="\r ")



numbers = [x * 5 for x in range (2000, 3000)]
output = ['25%']

progress_bar(0, len(numbers))

for i, x in enumerate(numbers):
    output.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

print(colorama.Fore.RESET)



def get_user_data():
    """
    Get the user data (name, age, body weight and height) from the
    user to calculate BMI. Run a while loop to collect the valid 
    data appropriate to the required age, the loop will be keep 
    requesting until the given data is valid.
    """

    while True:


        user_one_name = input("Enter your name:\n")
        user_one_age = int(input("Enter your age:\n"))
        user_one_weight = int(input("Enter your weight:\n"))
        user_one_height = int(input("Enter your height:\n"))

    
        class User:
            def __init__(self, name, user_age, weight, height):
                self.name = name
                self.user_age = user_age
                self.weight = weight
                self.height = height

            def another(self):
                print(f"Your name is {self.name}")
                print(f"Your age is {self.user_age}")
                print(f"Your weight is {self.weight}")
                print(f"Your height is {self.height}")


        object_of_user = User(user_one_name, user_one_age, user_one_weight, user_one_height)
        object_of_user.another()





        weight = user_one_weight
        height = user_one_height
        user_age = user_one_age
        
        calculate_bmi(user_one_name, weight, height) 
        
        if validate_input(weight, height, user_age):
            print("Given entries are valid!")
            break

    return user_one_name, weight, height, user_age

def validate_input(weight, height, user_age):
    """
    Inside the try, it converts all string values to integers,
    raises the ValueError if string cannot be converted to
    integers, or there aren't exact values as per requirement 
    """
    try:
        if user_age < 5:
            raise ValueError(
                f"Sorry age should be above 2 years you provided {user_age}"
            )
        elif user_age > 100:
            raise ValueError(
                f"Sorry max age to calculate BMI is 100 your age {user_age}"
            )
    except ValueError as e:
            print(f"Invalid entry: {e}, please try again.\n ")
            return False

    return True

    name, weight, height = calculate_bmi
    

def calculate_bmi(name, weight, height):
    """
    It calculate the BMI from data received from get user data
    function and produce the required result, it also tells
    the user if their wieght is good or hight as per BMI
    calculations
    """ 
    high = height / 100
    bmi = weight / (high ** 2) 
    result = round(bmi,2)
    print(f"Hey " + name +" "+ "your BMI is:", result)

    if result < 25:
        print( name + " " + "You have a good weight according to BMI:)\n")
    else:
        print(name + " " + "sorry but your weight is a bit high\n")







name, user_age, weight, height = get_user_data()

