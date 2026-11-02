class Playlist:
     def __init__(self,name,genre):
        self.name = name
        self.genre = genre
        self.song = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")
     def add_song(self,song):
        self.song.append(song)
        print(f"'{song}' has been added to the playlist '{self.name}.'")
     def remove_song(self,song):
        if song in self.song:
            self.song.remove(song)
            print(f"'{song}' has been removed from the playlist '{self.name}.'")
        else:
            print(f"'{song}' is not in the playlist '{self.name}.'")
     def display(self):
        print(f"\n----{self.name} ({self.genre})----")
        if self.song:
            for  i, song in enumerate(self.song, 1):
             print(f"{i}. {song}")
        else:
            print("No songs in the playlist.")
     def __del__ (self):
        print(f"Playlist '{self.name}' has been deleted.")
my_playlist = Playlist("My Favorites", "Pop")
while True:
    print("\nOptions: 1.Add Songs 2.Remove Songs 3.Show playlist 4.Delete and quit")
    choice = input("enter your choice: ")
    if choice == "1":
        song = input("Enter the song name to add:")
        my_playlist.add_song(song)
    elif choice == "2":
        song = input("Enter the song name to remove: ")
        my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        del my_playlist
        break
    else:
        print("Invalid Entry!")