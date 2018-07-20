# Define a set that contains tuples. Each tuple should contain two strings 1) The name of an artist 2) A song by that artist

songs = {
    ("Nickelback", "How You Remind Me"), 
    ("Will.i.am", "That Power"),
    ("Miles Davis", "Stella by Starlight"),
    ("Nickelback", "Animals")
}

# New variable to hold set. Start at index 0 and itterate over and evaluate which tuples include "Nickelback" and remove them. Print the new dictionary.
good_songs = {(song[0], song[1]) for song in songs if song[0] != 'Nickelback'}

print(good_songs)