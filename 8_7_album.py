def make_album(name, singer, number_of_songs=None):
    return {
        'name': name,
        'singer': singer,
        'number_of_songs': number_of_songs
    }


print(make_album('name1', 'singer1'))
print(make_album('name2', 'singer2'))
print(make_album('name3', 'singer3', 9))
