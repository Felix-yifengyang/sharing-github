people = ['admin','yyf','ckl','zdz','shit']
for person in people :
    if person == 'admin' :
        print("Hello admin, would you like to see a status report?")
    else :
        print(f"Hello {person}, thank you for logging in again.")
current_users = people[:]
new_users = ['YYF','ckl','sb','qs','nc']
current_users_lower = [person.lower() for person in people]
for new_user in new_users :
    if new_user.lower() in current_users_lower :
        print(f"{new_user}, input other!")
    else :
        print("OK!")
del(people[:])
if not people :
    print("We need to find some users!")
