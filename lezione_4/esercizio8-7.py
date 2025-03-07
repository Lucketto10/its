#esercizio8-7

def make_album(artist, title, num_songs=None):
    album = {
        'artist':artist,
        'title':title,
    } 

    if num_songs:
        album['num_songs'] = num_songs
    return album

print(make_album("Nayt", "Lettera q"))
print(make_album("Madman", "mm volume 5"))
print(make_album("Gemitaiz", "scatola nera"))
print(make_album("Kendrick Lamar", "dna", 14)) 