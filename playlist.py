#!/usr/bin/pyhton3

from bs4 import BeautifulSoup

def show_main_menu():
    while True:
        print("\nMenú Principal:")
        print("1. Álbumes")
        print("2. Artistas")
        print("3. Canciones")
        print("4. Géneros")
        print("0. Salir")
        option = input("Ingrese una opción: ")
        if option.isdigit():
            option = int(option)
            if option in [0, 1, 2, 3, 4]:
                return option
            else:
                print("Opción no válida. Por favor, ingrese un número entre 0 y 4.")
        else:
            print("Entrada no válida. Por favor, ingrese un número.")


def show_menu_songs():
    while True:
        print("\nMenú Canciones:")
        print("1. Listar todas las canciones")
        print("2. Buscar canción por título")
        print("0. Volver")
        option = input("Ingrese una opción: ")
        if option.isdigit():
        	option = int(option)
            if option == 0:
                return option
            elif option == 1:
            	return option
			elif option == 2:
            	return option
			else:
                print("Opción no válida. Por favor, ingrese un número entre 0 y 2.")
        else:
            print("Entrada no válida. Por favor, ingrese un número.")



def show_menu_albums():
    while True:
        print("\nMenú Álbumes:")
        print("1. Listar todos los álbumes")
        print("2. Buscar álbum por nombre")
        print("0. Volver")
        option = input("Ingrese una opción: ")
        if option.isdigit():
            option = int(option)
            if option == 0:
                return option
            elif option == 1:
            	return option
			elif option == 2:
            	return option
			else:
                print("Opción no válida. Por favor, ingrese un número entre 0 y 2.")
        else:
            print("Entrada no válida. Por favor, ingrese un número.")


def show_menu_artists():
    while True:
        print("\nMenú Artistas:")
        print("1. Listar todos los artistas")
        print("2. Buscar artista por nombre")
        print("0. Volver")
        option = input("Ingrese una opción: ")
        if option.isdigit():
            option = int(option)
            if option == 0:
             	return option
			elif option == 1:
             	return option
			elif option == 2:
             	return option
			else:
                print("Opción no válida. Por favor, ingrese un número entre 0 y 2.")
        else:
            print("Entrada no válida. Por favor, ingrese un número.")

def show_menu_genres():
    while True:
        print("\nMenú Géneros:")
        print("1. Listar todos los géneros")
        print("2. Buscar género por nombre")
        print("0. Volver")
        option = input("Ingrese una opción: ")
        if option.isdigit():
            option = int(option)
            if option == 0:
                return option
            elif option == 1:
                 return option
            elif option == 2:
				return option
            else:
                print("Opción no válida. Por favor, ingrese un número entre 0 y 2.")
        else:
            print("Entrada no válida. Por favor, ingrese un número.")




version = 0.5

app_title = "Playlist v" + str(version)

print(app_title)

print("-" * len(app_title))


show_main_menu()
show_menu_albums()
show_menu_artists()
show_menu_genres()
song_xml = open("songs/song_1.xml", "r").read()

#print(song_xml)

song = BeautifulSoup(song_xml, 'xml')

print(song.title.text)
print(int(song.duration["seconds"])/60)

#for artist in song.artists.find("artist"):
#	print(str(artist.attr.id), artist.text)
