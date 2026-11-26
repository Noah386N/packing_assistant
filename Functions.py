packing_list_1 = []

from General_Data import Beach_Trip, Skiing_Trip

def selection():
    print("1   Generate Trip")
    print("2   Add Item")
    print("3   Edit Item")
    Choice = int(input("Choose Function "))
    if Choice == 1:
        Function_1 = Generate_Trip()
        print(Function_1)
    elif Choice == 2:
        Function_2 = add_item()
        print(Function_2)
    elif Choice == 3:
        Function_3 = edit_item()
        print(Function_3)
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


selection()


