
# [INCHES TO -- > _____]
def inchesToFeet():
    enter = int(input("Please enter the amount of inches you would like to convert to feet: "))
    foot = (enter / 12)
    foot = "{:.2f}".format(foot)
    print(foot, "feet")

def inchesToYards():
    enter = int(input("Please enter the amount of inches you would like to convert to yards: "))
    yards = (enter / 36)
    yards = "{:.2f}".format(yards)
    print(yards, "yards")

def inchesToMiles():
    enter = int(input("Please enter the amount of inches you would like to convert to miles: "))
    miles = (enter / 63360)
    miles = "{:.2f}".format(miles)
    print(miles, "miles")

def inchesToMilimeters():
    enter = int(input("Please enter the amount of inches you would like to convert to milimeters: "))
    milimeters = (enter * 25.4)
    milimeters = "{:.2f}".format(milimeters)
    print(milimeters, "milimeters")

def inchesToCentimeters():
    enter = int(input("Please enter the amount of inches you would like to convert to centimeters: "))
    centimeters = (enter * 2.54)
    centimeters = "{:.2f}".format(centimeters)
    print(centimeters, "centimeters")

def inchesToMeters():
    enter = int(input("Please enter the amount of inches you would like to convert to centimeters: "))
    meters = (enter / 39.37)
    meters = "{:.2f}".format(meters)
    print(meters, "centimeters")