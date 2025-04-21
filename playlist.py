#!/usr/bin/pyhton3

from bs4 import BeautifulSoup


version = 0.5

app_title = "Playlist v" + str(version)

print(app_title)

print("-" * len(app_title))


song_xml = open("songs/song_1.xml", "r").read()

#print(song_xml)

song = BeautifulSoup(song_xml, 'xml')

print(song.title.text)
print(int(song.duration["seconds"])/60)

for artist in song.artists.find("artist"):
	print(str(artist.attr.id), artist.text)
