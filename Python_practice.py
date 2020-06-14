voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

print(voting_data[0]["county"],voting_data[0]["registered_voters"])

for dictionary in voting_data:
    print(f"{dictionary['county']} county has {dictionary['registered_voters']:,} registered voters")
