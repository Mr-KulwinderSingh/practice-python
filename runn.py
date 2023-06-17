from pyfiglet import figlet_format

import math

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
        user1_age = int(input("Enter your age:\n"))
        user1_weight = int(input("Enter your weight(in kgs only):\n"))
        user1_height = int(input("Enter your height(in cms only):\n"))

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
        weight = user1_weight
        height = user1_height
        user_age = user1_age

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
            raise ValueError(
                f"Please enter a name {user1_name}"
            )
        elif (len(user1_name) <= 2):
                raise ValueError(
                    f"user name should be more than 3 characters"
                )
        elif user_age == " ":
            raise ValueError(
                f"Please enter a age {user_age}"
            )
        elif user_age < 5:
            raise ValueError(
                f"Sorry age should be above 5 years you provided {user_age}"
            )
        elif user_age > 100:
            raise ValueError(
                f"Sorry max age to calculate BMI is 100 your age {user_age}"
            )
        elif weight < 5:
            raise ValueError(
                f"Sorry weight should be a valid number you provided {weight}"
            )
        elif weight > 120:
            raise ValueError(
                f"Sorry weight should be a valid number you provided {weight}"
            )
        while height > 200:
            raise ValueError(
                f"Sorry above 200cm is invalid height, you entered: {height}"
                " " "Please read Exception and Rare statement or "
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again.\n ")
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
        print('\033[31m' + name + " " + "sorry but your weight is a bit high\n")


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
