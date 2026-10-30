packing_list_1 = []

import General_Data

Beach_Trip = {"Location" : "Beach", 
        "Duration" : 0, 
        "packing_list" : [1, 2, 3, 4]}

Skiing_Trip = {"Location" : "Skiing", 
        "Duration" : 0, 
        "packing_list" : [1, 2, 3, 4]}

def Generate_Trip():
    location = input("Chose your Trip: Beach or Skiing")
    if location.lower().strip() == "beach":
        Beach_Trip["Duration"] = int(input("How many days is your Trip?"))
        return Beach_Trip
    elif location.lower().strip() == "skiing":
        Skiing_Trip["Duration"] = int(input("How many days is your Trip?"))
        return Skiing_Trip
    else:
        return"No Predefined Trip exists! / Check your spelling!"



def selection():
    Choice = int(input("Choose Function "))
    if Choice == 1:
        Function_1 = Generate_Trip()
        print(Function_1)
    else:
        print("not definded")

selection()


