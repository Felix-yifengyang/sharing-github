Pet1 = {'name' : 'Bbaby', 'type' : 'cat', 'owner' : 'Kailin'}
Pet2 = {'name' : 'Chongyang', 'type' : 'crested gecko', 'owner' : 'Yifeng'}
Pet3 = {'name' : 'Change', 'type' : 'snake', 'owner' : 'Yifeng'}
pets = [Pet1,Pet2,Pet3]
i = 1
for pet in pets :
    print(f"\nPet{i}")
    for pet_name, pet_info in pet.items() :
        print(f"{pet_name}:\t{pet_info.title()}")
    i += 1