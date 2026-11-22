item = {"Name" : "name", "Quantity" : 0, "Category" : "Category", "Packing Status" : False}
item_1= {"Name" : "Wallet", "Quantity" : 1, "Category" : "Essential", "Packing Status" : False}
item_2= {"Name" : "Beach Towel", "Quantity" : 1, "Category" : "Beach", "Packing Status" : False}
item_3= {"Name" : "ski-goggles", "Quantity" : 1, "Category" : "Skiing", "Packing Status" : False}

packing_list = [item_1,item_2,item_3]
packing_list_beach = [item_1,item_2]
packing_list_skiing = [item_1,item_3]

Beach_Trip = {"Location" : "Beach", 
        "Duration" : 0, 
        "packing_list" :packing_list_beach}

Skiing_Trip = {"Location" : "Skiing", 
        "Duration" : 0, 
        "packing_list" :packing_list_skiing}


#List_of_Trips = {"Trip_1" : 
   #              {"Location" : "Beach", 
    #              "Duration" : 7 ,
     #             "Packing_list_1" : [Packing_List_1]}
      #            }

