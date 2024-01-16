favorite_languages = {
     'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',
}
close = ['ckl','zdz','jen']
for jiyou in close :
    if jiyou in favorite_languages :
        print(f"{jiyou}, Thank you!")
    else:
        print(f"{jiyou}, Please take the toll!")
