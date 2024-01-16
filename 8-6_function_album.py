def make_album(singer, album_name, song_count = None) :
    album = {'singer' : singer, "album's name" : album_name,}
    if song_count :
        album["album's number"] = song_count
    return album
while True :
    print("""Please tell me the infomation,
if you want to quit, please enter 'q'.""")
    singer = input("Please tell me the singer name :")
    if singer == 'q' :
        break
    album_name = input("Please tell me the album's name :")
    if album_name == 'q' :
        break
    song_count = input("""Please tell me how many songs in the album :""")
    if album_name == 'q' :
        continue
    else :
        int(song_count)
    print(make_album(singer, album_name, song_count))