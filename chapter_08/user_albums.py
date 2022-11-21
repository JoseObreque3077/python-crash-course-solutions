# Exercise 8-8
# Start with your program from Exercise 8-7. Write a while loop that
# allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist, title, tracks=None):
    album = {
        'artist': artist.title(),
        'album': title.title()
        }
    
    if tracks:
        album['tracks'] = tracks
    
    return album


if __name__ == "__main__":
    print("Enter 'exit' to stop program")
    while True:
        artist_name = input("\nArtist name: ")
        if artist_name.lower() == "exit":
            break
        
        album_title = input("Album title: ")
        if album_title.lower() == "exit":
            break
        
        album = make_album(artist_name, album_title)
        print(album)
