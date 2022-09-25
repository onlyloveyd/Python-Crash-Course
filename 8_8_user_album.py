def make_album(name, singer, number_of_songs=None):
    return {
        'name': name,
        'singer': singer,
        'number_of_songs': number_of_songs
    }


QUIT = 'quit'
while True:
    album_name = input("Album name: ")
    if QUIT == album_name:
        break
    singer = input("Singer: ")
    if QUIT == singer:
        break
    print(make_album(album_name, singer))
