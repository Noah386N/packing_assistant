#item = {"Name" : "name", "Quantity" : 0, "Category" : "Category", "Packing Status" : False}
# Generall Items
item_1= {"Name" : "Wallet", "Quantity" : 0, "Per Day" : None, "Category" : "Essential", "Packing Status" : False}
item_2= {"Name" : "Charger", "Quantity" : 0, "Per Day" : None, "Category" : "Essential", "Packing Status" : False}
item_3= {"Name" : "Underpants", "Quantity" : 0, "Per Day" : 1.5, "Category" : "Essential", "Packing Status" : False}
item_4= {"Name" : "Socks", "Quantity" : 0, "Per Day" : 2, "Category" : "Essential", "Packing Status" : False}
# Skiing Specific
item_5= {"Name" : "Pants", "Quantity" : 0, "Per Day" : 0.5, "Category" : "Skiing", "Packing Status" : False}
item_6= {"Name" : "Thermal-Clothing", "Quantity" : 0, "Per Day" : 0.5, "Category" : "Skiing", "Packing Status" : False}
item_7= {"Name" : "Sweater", "Quantity" : 0, "Per Day" : 0.5, "Category" : "Skiing", "Packing Status" : False}
item_8= {"Name" : "Ski-Goggles", "Quantity" : 0, "Per Day" : None, "Category" : "Skiing", "Packing Status" : False}
# Beach Specific
item_9= {"Name" : "Swimming-Trunks", "Quantity" : 0, "Per Day" : 1, "Category" : "Beach", "Packing Status" : False}
item_10= {"Name" : "T-Shirt", "Quantity" : 0, "Per Day" : 1, "Category" : "Beach", "Packing Status" : False}
item_11= {"Name" : "Shorts", "Quantity" : 0, "Per Day" : 0.5, "Category" : "Beach", "Packing Status" : False}
item_12= {"Name" : "Flipflops", "Quantity" : 0, "Per Day" : None, "Category" : "Beach", "Packing Status" : False}

#packing_list = [item_1,item_2,item_3, ...]
packing_list_beach = [item_1,item_2,item_3,item_4,item_9,item_10,item_11,item_12]
packing_list_skiing = [item_1,item_2, item_3, item_4,item_5,item_6,item_7,item_8]

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
        #         }

