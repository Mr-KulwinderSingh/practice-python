from pyfiglet import figlet_format

import math

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

figlet_format("BODY MASS INDEX", font="small")

print(figlet_format("BODY MASS INDEX", font="small"))


def get_user_data():
    """
    This function starts the whole process of the BMI app with the  
    welcome message & info about exception and rare statement for the  
    user. It appeals the user to follow the prompts. Get user data
    (name, age, body weight and height) from the user to calculate
    BMI. Runs a while loop to collect the valid data appropriate
    to the required age, the loop will be keep requesting until the
    given data is valid.
    """
    
    print("            Welcome to the Body_Mass_Index!\n")
    print("--------------------------------------------------------------- ")
    print("Our modern eat-out style, and living in the world of technology")
    print("every person needs to know what category of BMI he/she is in\n")

    print("-------------***** Exceptions and Rare *****--------------------")
    print("----------------------------------------------------------------")
    print("Adult women and men weighing 100kg who are between 201.0cm and")
    print("219.0 cm tall are considered to be of a healthy weight as measured")
    print("by body mass index (bmi)2,but our BMI is restricted to 200cm height")
    print("----------------------------------------------------------------")
    print("This BMI calculator has limits i.e. it can take the age of the ")
    print("user 5 years to 100 years and weight 5kgs to 100kgs plus the height")
    print("restrictions upto 200cm, please consider them before entering your")
    print(".                   details! Good Luck! \n")

    start = input("To start please type yes:\n ")

    while start.lower() != "yes":
        print(f"BMI app needs your permission, please type yes to start!\n")
        start = input("To start please type yes:\n ")
        print(f"You said {start} to start")



    while True:

        user1_name = input("Enter your Name:\n")
        user1_age = input("Enter your Age:\n")
        user1_weight = input("Enter your Weight(in kgs only):\n")
        user1_height = input("Enter your Height(in cms only):\n")

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
                print(f"You are {self.user_age} years old\n")
                print(f"Your weight is {self.weight}kgs\n")
                print(f"Your height is {self.height}cms\n")

        display_user = User(user1_name, user1_age, user1_weight, user1_height)
        display_user.another()
        weight = int(float(user1_weight))
        height = int(float(user1_height))
        user_age = int(float(user1_age))

        calculate_bmi(user1_name, weight, height)

        validate_username(user1_name)
        validate_user_weight(weight)
        validate_user_height(height)

        if validate_user_age(user_age):
            print("Given entries are valid!")
            break
    return user1_name, weight, height, user_age


def validate_username(user1_name):
    """
    Inside the try, it converts all string values to integers,
    raises the ValueError if string cannot be converted to
    integers, or there aren't exact values as per requirement
    """
    try:
        
        if user1_name == " ":
            raise ValueError(
                f"'Blank space error!', Please enter a name {user1_name}"
            )
        elif (len(user1_name) <= 2) or (len(user1_name) >= 10):
                raise ValueError(
                    f"User name should be min 3 or max 10 characters long"
                )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again.\n ")
        return False
        print("Due to the error program ended")
    return True

def validate_user_age(user_age):
    """
    Inside this function checks if the user enters an integer or
    not, plus it also checks an error if the provided age range is 
    valid and if it's not valid as per the BMI age range, value error 
    will be triggered, empty or blank space can also be detected here
    in this validation function
    """
    try:
        if user_age < 5 or user_age > 100:
            raise ValueError(
                f"Please correct user age range in order to calculate BMI"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again.\n ")
        return False
        print("program ended!")
    return True

def validate_user_weight(weight):
    """
    Inside the try, this function checks if the user enters an integer
    or not, plus it also checks an error if the provided weight range is 
    valid & if it's not valid as per the BMI valid weight range,value error 
    will be triggered, empty or blank space can also be detected here
    in this validation function
    """
    try:

        if weight < 10 or weight > 120:
            raise ValueError(
            f"Sorry Invalid weight range entered: {weight}"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again.\n ")
        return False
        print("program ended!")
    return True

def validate_user_height(height):
    """
    Inside the try, this function checks if the user enters an integer
    or not, plus it also gives an error if the provided height range is 
    valid and if it's not valid as per the BMI valid height range error 
    will be triggered, empty or blank space can also be detected here
    in in this validation function
    """

    try:

        if height < 80 or height > 200:
            raise ValueError(
                f"Sorry Invalid height range entered:{height}"
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
