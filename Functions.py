packing_list_1 = []

#importing python math package in order to calculate rounding up/down etc
import math                                             
from General_Data import Beach_Trip, Skiing_Trip
#importing deepcopy so when creating packing lists the original version isnt changed
from copy import deepcopy

def selection():
    print("1   Generate Trip")
    Choice = int(input("Choose Function "))
    if Choice == 1:
        Function_1 = Generate_Trip()
        print(Function_1)       #Use loop with f string instead of print so every item gets own line.
    else:
        print("not definded")

#Calculating the amount of items needed for duration
def calculate_quantity(item, duration):
    if item["Per Day"] is None:
        return 1
    else:
        return math.ceil(item["Per Day"] * duration)

#Creating copy of trip and assigning previously calculated quantity
def fill_packing_list(trip, duration):
    custom_trip = deepcopy(trip)
    custom_trip["Duration"] = duration
    for item in custom_trip["packing_list"]:
        item["Quantity"] = calculate_quantity(item, duration) 
    return custom_trip
        
#Generate the trip calling user input and putting it through predefined functions
def Generate_Trip():
    location = input("Chose your Trip: Beach or Skiing? ")
    if location.lower().strip() == "beach":
        chosen_trip = Beach_Trip        
    elif location.lower().strip() == "skiing":
        chosen_trip = Skiing_Trip       
    else:
        return "No Predefined Trip exists! / Check your spelling!"

    duration = int(input("How many days is your Trip? "))
    filled_trip = fill_packing_list(chosen_trip, duration)
    return filled_trip

#function only runs if started in this file
if __name__ == "__main__":
    selection()


