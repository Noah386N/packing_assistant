# packing_assistant
This is our Programming foundations project. 
Project by Martin Merzaie, Balthasar Weber, Aleksandar Filipovic and Noah Kleiner

Defintions:
Item: Dictionary with 4 key value pairs which are name, quantity, category, packing status. Default item status is unpacked.
Packing list: A Packing List is a list of dictionaries. It Consists of a certain number of items which are dictionaries. 
Item Selection: An Item is Selected by Name. 
Trip: A trip is a combination out of preselected themes (Skiing, beach etc.) and the duration of the trip. The List is preconfigured for every destination, the duration changes the quantity of single items listed. 

Rules for input validation:
There cant be a negative number of a certain item.
Duration cant be negative and is the unit is in days.



User stories with acceptance criteria – Group H;
 Balthasar Weber, Aleksandar Filipovic, Martin Merzaie, Noah Kleiner

Balz
 
1. Add an item
As a user, I want to add an item to my packing list so that I remember what I need to bring.
Acceptance Criteria
Definition of an Item: Dictionary with 4 key value pairs which are name, quantity, category, packing status.
-The user can enter the name and the quantity of a new item and the item is then added to the packing list.
- An empty item name returns an error
- There will be a confirming message once the item has been added successfully.
 
 
2. Edit an item
As a user, I want to edit an item so that I can correct information.
Acceptance Criteria
 
•	The user is able to change the name or the quantity of the item, the updated information replaces the old information in the selected trip
•	The program shows an specific error if the selected item does not exist.
 
 
3. Remove an item
As a user, I want to remove an item so that I can delete things I no longer need.
Acceptance Criteria
 
- The user can select an existing item and remove it from the list.
- Other items are not affected.
- The program shows an specific error if the item does not exist.
 
 
Noah
 
4. Show all items
As a user, I want to see all items so that I know what is on my packing list.
Acceptance Criteria
 
- Quantity, category and packing status and name are always displayed.
- The same rule as the criteria above is for custom items.
- If the list is empty, the program informs the user.
 
 
5. Show unpacked items
As a user, I want to see only unpacked items so that I know what I still need to pack.
Acceptance Criteria
 
-On User request, only items with the status "unpacked" are displayed.
- If everything is packed, the program informs the user.
- The original packing list is not changed by displaying the non-packed items. 
 
6. Search for an item
As a user, I want to search for an item so that I can quickly find it.
Acceptance Criteria
 
- When the user enters the name of an item, the matching item is displayed. 
- If no item is found, the user receives a specific message.
 
 
Martin
 
7. Mark an item as packed
As a user, I want to mark an item as packed so that I know it is already in my luggage.
Acceptance Criteria
 
- The user can select an existing item so that item status changes from unpacked to packed. 
- The user receives a confirmation once the status has successfully changed 
- The program shows an error if the item does not exist.
- Other items are not changed.
 
8. Mark an item as unpacked
As a user, I want to mark an item as unpacked so that I can correct the packing status.
Acceptance Criteria
 
- The user can select a packed item so that the item status changes from packed to unpacked.
- The user receives a confirmation once the status has successfully changed 
- The program shows an error if the item does not exist.
- Other items are not changed.
 
9. Show packing progress
As a user, I want to see my packing progress so that I know how much I have already packed.
Acceptance Criteria
 
- The program counts the total number of item and the total number of items already packed and then calculates a percentage of items already packed.  
- The result is displayed clearly, for example: "7 of 10 items packed - 70%".
-If the list is empty it returns an specific error
 
 
Aleks
 
10. Create a trip
As a user, I want to be able to choose a trip with different Locations and Durations so that I can create a packing list for my journey. 
Acceptance Criteria
 
- The user can create a trip by entering a destination and a trip duration.
- The duration must be a positive number.
- Empty destinations are not accepted and returns an error. 
 
 
11. Save data
As a user, I want to save my packing list so that my data is not lost.
Acceptance Criteria
 
- The packing list can be saved as a file. 
- All item information is saved (Packing status, item name, packing amount).
- Existing data in the specific file can be updated when the user saves again.
- The program confirms that the data was saved successfully.
 
 
12. Load data
As a user, I want to load my packing list so that I can continue where I stopped.
Acceptance Criteria
 
- The program can read previously saved data from a file.
- All saved items and their respective packing statuses are loaded correctly.
- If the file does not exist, the program shows a message.

