#esercizio8-8

def make_album(artist, title, num_songs=None):
    album={'artist':artist,'title':title} 
    if num_songs:
        album['num_songs']=num_songs
    return album

while True:
    artist=input("Enter the artist's name (or 'q'to quit):")
    if artist in ['q', 'quit']:
        break

    title=input ("Enter the album title:")

    if title in['q', 'quit']:
        break

    num_songs= input("Enter the numbers of songs (or press Enter to skip): ")
    
    if num_songs in ['q', 'quit']:
        break

    if num_songs:
        album=make_album(artist, title, int(num_songs))

    else:
        album=make_album(artist, title)
        print(album)