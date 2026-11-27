#to try out functions:

packing_list_1 = []

from General_Data import item, packing_list, Skiing_Trip, Beach_Trip

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
    elif Choice == 2:
            Function_2 = add_item()
            print(Function_2)
    else:
        print("not definded")

def add_item():
    new_item = input("What new item would you like to add? ")
    new_item_amount = input("How much/many would you like to add? ")
    if new_item == "" or new_item_amount == "":
        print("No item definded/no amount specified")
    else:
        packing_list_1.append({"Name" : new_item, "Quantity" : int(new_item_amount), "Category" : "Category", "Packing Status" : False})

selection()