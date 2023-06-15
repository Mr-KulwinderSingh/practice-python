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


def get_user_data():
    """
    Get the user data (name, age, body weight and height) from the
    user to calculate BMI. Run a while loop to collect the valid 
    data appropriate to the required age, the loop will be keep 
    requesting until the given data is valid.
    """

    while True:
    
        print("Great !")
        name = input("Please enter your name:\n")
        
        age = int(input("Please enter your age:\n"))
        
        print("Please provide your body weight(in kgs)")
        data1 = int(input("Enter your weight here:\n "))

        print("now enter your height(only in cms)")
        data2 = int(input("Enter the height here:\n "))
        print(f"Your weight is : {data1}kgs and height is :{data2}cms\n")


        weight = data1 
        height = data2
        user_age = age
        
        
        if validate_input(weight, height, user_age):
            print("Given entries are valid!")
            break

    return name, weight, height, user_age

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
    calculate_bmi(name, wight, height) 

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

    

class User:
    def __init__(self, name, user_age, weight, height):
        self.name = name
        self.user_age = user_age
        self.weight = weight
        self.height = height

    def another(self):
        print(f"User's name is {self.name}")
        print(f"User's age is {self.user_age}")
        print(f"User's weight is {self.weight}")
        print(f"User's height is {self.height}")


user_one_name = input("Enter your name:\n")
user_one_age = input("Enter your age:\n")
user_one_weight = input("Enter your weight")
user_one_height = input("Enter your height")


object_of_user = User(user_one_name, user_one_age, user_one_weight, user_one_height)
object_of_user.another()





name, user_age, weight, height = get_user_data()
calculate_bmi(name, weight, height)
