from pyfiglet import figlet_format

import math as m

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

figlet_format("BODY MASS INDEX", font="small")

print(figlet_format("BODY MASS INDEX", font="small"))


print("            Welcome to the Body_Mass_Index!\n")
print("--------------------------------------------------------------- ")
print("As per the modern life style, and living in the world of technology")
print("every person needs to know what category of BMI he is in\n")

print("-------------***** Exceptions and Rare *****--------------------")
print("----------------------------------------------------------------")
print("Adult women and men weighing 100kg who are between 201.0cm and 219.0")
print("cm tall are considered to be of a healthy weight as measured by body")
print("  mass index (bmi)2, but this BMI is restricted to 200cm height ")
print("----------------------------------------------------------------")
print("This BMI calculator has limits i.e. it can take the age of the user")
print("from 5 years to 100 years and weight 5 kgs to 100 kgs plus the height")
print("restrictions upto 200cm, please consider them before entering your")
print(".                   details! Good Luck! \n")

start = input("To start please type yes:\n ")

while start.lower() != "yes":
    print(f"If you'd like to start please type 'yes'\n")
    start = input("To start please type yes:\n ")
    print(f"You said {start} to start")


def get_user_data():
    """
    Get the user data (name, age, body weight and height) from the
    user to calculate BMI. Run a while loop to collect the valid
    data appropriate to the required age, the loop will be keep
    requesting until the given data is valid.
    """

    while True:

        user1_name = input("Enter your name:\n")
        user1_age = input("Enter your age:\n")
        user1_weight = input("Enter your weight(in kgs only):\n")
        user1_height = input("Enter your height(in cms only):\n")

        class User:
            """
            Class User helps to manipulate and represent data in the form it
            has to be in the terminal, it correspond with the main function,
            takes the user input and segregate accordingly

            """

            def __init__(self, name, user_age, weight, height):
                self.name = name
                self.user_age = user_age
                self.weight = weight
                self.height = height

            def another(self):
                print(f"Your name is {self.name}\n")
                print(f"Your age is {self.user_age} years\n")
                print(f"Your weight is {self.weight}kgs\n")
                print(f"Your height is {self.height}cms\n")

        display_user = User(user1_name, user1_age, user1_weight, user1_height)
        display_user.another()
        weight = int(float(user1_weight))
        height = int(float(user1_height))
        user_age = int(float(user1_age))

        calculate_bmi(user1_name, weight, height)

        if validate_input(user1_name, weight, height, user_age):
            print("Given entries are valid!")
            break
    return user1_name, weight, height, user_age


def validate_input(user1_name, weight, height, user_age):
    """
    Inside the try, it converts all string values to integers,
    raises the ValueError if string cannot be converted to
    integers, or there aren't exact values as per requirement
    """
    try:
        

        if user1_name == " ":
            print('Blank space is not allowed, please enter a name')
            return False
        if (len(user1_name) <= 2):
            print("user name should be at least 3 characters long")
            return False
        if user_age < 5 or user_age > 100:
            raise ValueError(
                "Oops! Invalid age range")
            return False
        if weight < 10 or weight > 120:
            raise ValueError(
            f"Sorry weight should be a valid number you entered {weight}"
            )
            return False
        if height < 80 or height > 200:
            raise ValueError(
                f"Sorry Invalid height entered:{height}"
            ) 
    except ValueError as e:
        
        print(f"Invalid entry:{e}, please try again.\n ")
        return False

    return True


def calculate_bmi(name, weight, height):
    """
    It calculates the BMI of the data received from the user
    and generates the required result, it also tells
    the user if their wieght is good or high as per BMI
    calculations
    """

    height = height / 100
    bmi = weight / (height ** 2)
    result = round(bmi, 2)
    print('\033[32m'f"Hey " + name + " " + "your BMI is:", result)

    if result < 25:
        print('\033[32m' + name + " " + "Your weight is good as per BMI:)\n")
    else:
        print('\033[31m' + name + " " + "sorry your weight is a bit high\n")


def main():
    """
    Runs all the functions in the programme
    """

    name, user_age, weight, height = get_user_data()

    choice_to_restart = input('Press any key to restart or "q" to quit\n ')

    if choice_to_restart == "q":
        (quit)

    else:

        main()


main()
