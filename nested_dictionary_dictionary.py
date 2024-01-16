users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}
for user_name, user_info in users.items():
    print(f"\n Username: {user_name}")
    fullname = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]

    print(f"\t Full name : {fullname.title()}")
    print(f"\t Location : {location.title()}")