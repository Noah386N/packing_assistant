packing_list_1 = []

from General_Data import Beach_Trip, Skiing_Trip

def selection():
    print("1   Generate Trip")
    Choice = int(input("Choose Function "))
    if Choice == 1:
        Function_1 = Generate_Trip()
        print(Function_1)
    else:
        print("not definded")


def Generate_Trip():
    location = input("Chose your Trip: Beach or Skiing? ")
    if location.lower().strip() == "beach":
        Beach_Trip["Duration"] = int(input("How many days is your Trip? "))
        return Beach_Trip
    elif location.lower().strip() == "skiing":
        Skiing_Trip["Duration"] = int(input("How many days is your Trip? "))
        return Skiing_Trip
    else:
        return"No Predefined Trip exists! / Check your spelling!"


selection()


