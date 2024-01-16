rivers = {'nile':'egypt','changjiang':'china','huanghe':'china'}
for river,country in rivers.items():
    print(f"The {river} runs through {country.title()}.")
for river in rivers.keys():
    print(f"The river is {river}.")
for country in rivers.values():
    print(f"The country is {country}.")