packing_list_1 = []

#importing python math package in order to calculate rounding up/down etc
import math                                             
from General_Data import Beach_Trip, Skiing_Trip
#importing deepcopy so when creating packing lists the original version isnt changed
from copy import deepcopy

#Festlegen des Current trips (trip der durhc selection kreeirt wird, ist immer der current trip, so können wir später evtl. erweitern falls wir mehrere trips haben wollen)
Function_1= None #Function_1 = unser aktueller trip, wir müssen Variable schon hier definieren, damit man zb Funktion 2 nicht aufrufen kann, ohne das Function_1 etwas enthält (Würde sonst abstürzen weil trip leer = Show Items funktioniert nicht)

def selection():
    print("1   Generate Trip")
    print("2 Show Items")
    print("3 Show unpacked Items")

    Choice = int(input("Choose Function "))
    if Choice == 1:
        Function_1 = Generate_Trip()
        print(Function_1)       #Use loop with f string instead of print so every item gets own line.
    else:
        print("not definded")
        return None

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
        return"No Predefined Trip exists! / Check your spelling!"
    duration = int(input("How many days is your Trip? "))
    filled_trip = fill_packing_list(chosen_trip, duration)
    return filled_trip
#Is it possible it runs into an error if you first type in a wrong input so ex. misspelled "Skiing" and then try again? 

def get_status_text(item) : #Hilfsfunktion, damit wir packing status nicht einfach True oder False haben sondern False = Unpacked True = Packed (Schönere klarere Darstellung)
    if item ["Packing Status"] == True : 
        return "packed"
    else : 
        return "unpacked"

def show_items(trip) : 

    if len(trip["packing_list"]) == 0:
       print("Packing list is empty.")

    else :
       
       print("-----------------------------------------------------------------")
       print(f"{'Name':<20} | {'Quantity':<10} | {'Category':<15} | {'Status':<10}|")
       print("-----------------------------------------------------------------")
       for item in trip["packing_list"] :

           status = get_status_text(item)

           print(
            f"{item['Name']:<20} | "
            f"{item['Quantity']:<10} | "
            f"{item['Category']:<15} | "
            f"{status:<10}|"
            )
    print("-----------------------------------------------------------------")

               
def show_unpacked_items(trip):

    if len(trip["packing_list"]) == 0:
        print("Packing list is empty.")

    else:

        unpacked_found = False

        for item in trip["packing_list"]:

            if item["Packing Status"] == False:
                unpacked_found = True

        if unpacked_found == False:
            print("All items are packed.")
            return

        print("-----------------------------------------------------------------")
        print(f"{'Name':<20} | {'Quantity':<10} | {'Category':<15} | {'Status':<10}|")
        print("-----------------------------------------------------------------")

        for item in trip["packing_list"]:

            if item["Packing Status"] == False:

                status = get_status_text(item)

                print(
                    f"{item['Name']:<20} | "
                    f"{item['Quantity']:<10} | "
                    f"{item['Category']:<15} | "
                    f"{status:<10}|"
                )

        print("-----------------------------------------------------------------")

def search_item(trip):

    search_name = input("Enter item name: ")

    for item in trip["packing_list"]:

        item_name = item["Name"].lower()
        search_name_lower = search_name.lower()

        if item_name == search_name_lower:

            status = get_status_text(item)

            print("-----------------------------------------------------------------")
            print(f"{'Name':<20} | {'Quantity':<10} | {'Category':<15} | {'Status':<10}|")
            print("-----------------------------------------------------------------")

            print(
                f"{item['Name']:<20} | "
                f"{item['Quantity']:<10} | "
                f"{item['Category']:<15} | "
                f"{status:<10}|"
            )

            print("-----------------------------------------------------------------")

            return

    print("Item not found.")
    


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
 
def add_item():
    new_item = input("What new item would you like to add? ")
    new_item_amount = input("How much/many would you like to add? ")
    if new_item == "" or new_item_amount == "":
        return("No item definded/no amount specified")
    else:
        packing_list_1.append({"Name" : new_item, "Quantity" : int(new_item_amount), "Category" : "undefined", "Packing Status" : False})
        return(packing_list_1)
       
def edit_item():
    item_choice = input("Choose Item to edit: ")    
    for items in packing_list_1:
        if items["Name"].lower().strip() == item_choice.lower().strip():
            items["Quantity"] = str(input("How much/many do you want/need? "))
            items["Category"] = input("what is the Item's Category? ")
            return(packing_list_1)
    return("Item is not in the packing List")

#Function_1 = selection() #Function 1 = Aktueller Trip, könnten wir umbennennen (Zugriffspunkt für alle Funktionen)
#function only runs if started in this file
if __name__ == "__main__":
    selection()