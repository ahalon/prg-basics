class Song:
   def __init___(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
   def __str__(self):
      return f"Performer: {self.artist}\nTitle:     {self.title}\nAlbum:     {self.album}\nYear:      {self.year}\n"

# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017 )
song2 = Song("Queen", "Bohemian Rhapsody", "A Night a the Opera", 1975)

## object usage
print(song1)
print(song2)