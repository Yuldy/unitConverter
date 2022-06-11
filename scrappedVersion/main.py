#Unit Conversion Program
#Created by Christian Phan 6/7/22
from lenAndDistConversion import *

def menu():
    print("Welcome to the Unit Conversion Program!")
    print("Here are the list of types of conversions: \n 1. Length/Distance \n 2. Weight/Size \n 3. Temperature \n 4. Speed  ")
    print() #spacer


def lengthAndDistance():
    print(" 1. Inches \n 2. Feet \n 3. Yards \n 4. Miles \n 5. Milimeters \n 6. Centimeters \n 7. Meters")
    option = input("Please select a unit:" )

    if option == '1':
        print("Inches to... : \n 1. Feet \n 2. Yards \n 3. Miles \n 4. Milimeters \n 5. Centimeters \n 6. Meters ")
        option1 = input("And what would you like to convert it to? ")
        option1.lower()

        if option1 == '1' or option1 == 'feet' or option1 == 'ft':
            inchesToFeet()

    elif option == '2':
        print("Feet to... : \n 1. Inches \n 2. Yards \n 3. Miles \n 4. Milimeters \n 5. Centimeters \n 6. Meters ")
        option1 = input("And what would you like to convert it to?")
        option1.lower()

    elif option == '3':
        print("Yards to... : \n 1. Inches \n 2. Feet \n 3. Miles \n 4. Milimeters \n 5. Centimeters \n 6. Meters ")
        option1 = input("And what would you like to convert it to?")

    elif option == 4:
        print("Miles to... : \n 1. Inches \n 2. Feet \n 3. Yards \n 4. Milimeters \n 5. Centimeters \n 6. Meters ")
        option1 = input("And what would you like to convert it to?")

    elif option == 5:
        print("Milimeters to... : \n 1. Inches \n 2. Feet \n 3. Yards \n 4. Miles \n 5. Centimeters \n 6. Meters ")
        option1 = input("And what would you like to convert it to?")

    elif option == 6:
        print("Centimeters to... : \n 1. Inches \n 2. Feet \n 3. Yards \n 4. Miles \n 5. Milimeters \n 6. Meters ")
        option1 = input("And what would you like to convert it to?")
 
    elif option == 7:
        print("Meters to... : \n 1. Feet \n 2. Yard \n 3. Miles \n 4. Milimeters \n 5. Centimeters \n 6. Meters ")
        option1 = input("And what would you like to convert it to?")
    
    else:
        print("Invalid entry! Please try again: ")
        lengthAndDistance()


def weightAndSize():
    print("hello")

def weather():
    print("hello")

def speed():
    print("hello")

menu()


choice = input("Which conversion would you like to do?: ")

if choice == '1':
    lengthAndDistance()

if choice == '2':
    weightAndSize()




