packing_list_1 = []

from General_Data import Beach_Trip, Skiing_Trip

#Festlegen des Current trips (trip der durhc selection kreeirt wird, ist immer der current trip, so können wir später evtl. erweitern falls wir mehrere trips haben wollen)
Function_1= None #Function_1 = unser aktueller trip, wir müssen Variable schon hier definieren, damit man zb Funktion 2 nicht aufrufen kann, ohne das Function_1 etwas enthält (Würde sonst abstürzen weil trip leer = Show Items funktioniert nicht)

def selection():
    print("1   Generate Trip")
    print("2 Show Items")
    print ("3 Show unpacked Items")

    Choice = int(input("Choose Function "))
    if Choice == 1:
        Function_1 = Generate_Trip()
        print(Function_1)
        return Function_1 #Damit wir mit Trip weiter arbeiten können
    elif Choice == 2:
        if Function_1 is None:
            print("Please create a trip first")
        else:
            show_items(Function_1)
    elif Choice == 3 :
        if Function_1 is None:
            print("Please create a trip first")
        else : 
            show_unpacked_items(Function_1)    
    else:
        print("not definded")
        return None


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
    


#Function_1 = selection() #Function 1 = Aktueller Trip, könnten wir umbennennen (Zugriffspunkt für alle Funktionen)

Function_1 = Generate_Trip()

search_item(Function_1)