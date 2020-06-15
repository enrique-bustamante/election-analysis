voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

for dictionary in voting_data:
    print(f"{dictionary['county']} county has {dictionary['registered_voters']:,} registered voters")
