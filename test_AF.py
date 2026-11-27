from Functions import fill_packing_list

test_trip = {
    "Location": "Test",
    "Duration": 7,
    "packing_list": [
        {"Name": "Wallet", "Quantity": 0, "Per Day": None},
        {"Name": "Pants", "Quantity": 0, "Per Day": 0.5},
    ]
}

result = fill_packing_list(test_trip)
print(result["packing_list"])      # expect Quantity 1 and 4
print(test_trip["packing_list"])   # expect Quantity 0 and 0 (original untouched)

