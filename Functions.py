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

selection()


