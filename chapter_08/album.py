# Exercise 8-7
# Write a function called make_album() that builds a dictionary describing a
# music album. The function should take in an artist name and an album title,
# and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album
# information correctly.
# Use None to add an optional parameter to make_album() that allows you to store
# the number of songs on an album. If the calling line includes a value for the
# number of songs, add that value to the album’s dictionary. Make at least one
# new function call that includes the number of songs on an album.

def make_album(artist, title, tracks=None):
    # * Album dictionary
    album = {
        'artist': artist.title(),
        'album': title.title()
        }
    # * Tracks data are added if available.
    if tracks:
        album['tracks'] = tracks
    return album


if __name__ == "__main__":
    print(make_album("Elton John", "The Lockdown Sessions"))
    print(make_album("Warren Zevon", "Excitable Boy"))
    print(make_album("Elvis Presley", "Good Times"))
    print(make_album("The Police", "Synchronicity", 10))
