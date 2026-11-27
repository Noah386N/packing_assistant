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


# User_story_7
def Mark_Item_As_Packed(trip):
    packing_list = trip["packing_list"]
    item_name = input("Which item do you want to mark as packed? ")

    found = False

    for item in packing_list:
        if item["Name"].lower().strip() == item_name.lower().strip():
            item["Packing Status"] = True
            found = True
            print(item["Name"], "has been marked as packed.")
            break

    if found == False:
        print("Error: Item does not exist.")

# User_story_8
def Mark_Item_As_Unpacked(trip):
    packing_list = trip["packing_list"]
    item_name = input("Which item do you want to mark as unpacked? ")
    found = False

    for item in packing_list:
        if item["Name"].lower().strip() == item_name.lower().strip():
            found = True
            if item["Packing Status"] == True:
                item["Packing Status"] = False
                print(item["Name"], "has been marked as unpacked.")
            else:
                print(item["Name"], "is already unpacked.")

            break

    if found == False:
        print("Error: Item does not exist.")

#User_story_9
def Show_Packing_Progress(trip):
    packing_list = trip["packing_list"]

    if len(packing_list) == 0:
        print("Error: Packing list is empty.")
        return

    total_items = len(packing_list)
    packed_items = 0

    for item in packing_list:
        if item["Packing Status"] == True:
            packed_items = packed_items + 1

    percentage = packed_items / total_items * 100
    percentage = round(percentage)

    print(packed_items, "of", total_items, "items packed -", str(percentage) + "%")
 

#function only runs if started in this file
if __name__ == "__main__":
    selection()


