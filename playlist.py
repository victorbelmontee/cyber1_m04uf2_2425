#!/usr/bin/env python3

from bs4 import BeautifulSoup
import os

def show_main_menu():
    # Muestra el menú principal y retorna la opción seleccionada por el usuario
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
            if option in (0, 1, 2, 3, 4):
                return option
        print("Opción no válida. Por favor, ingrese un número entre 0 y 4.")

def show_menu_albums():
    # Muestra el menú de álbumes y retorna la opción seleccionada
    while True:
        print("\nMenú Álbumes:")
        print("1. Listar todos los álbumes")
        print("2. Buscar álbum por nombre")
        print("0. Volver")
        option = input("Ingrese una opción: ")
        if option.isdigit() and int(option) in (0,1,2):
            return int(option)
        print("Opción no válida. Por favor, ingrese un número entre 0 y 2.")

def show_menu_artists():
    # Muestra el menú de artistas y retorna la opción seleccionada
    while True:
        print("\nMenú Artistas:")
        print("1. Listar todos los artistas")
        print("2. Buscar artista por nombre")
        print("0. Volver")
        option = input("Ingrese una opción: ")
        if option.isdigit() and int(option) in (0,1,2):
            return int(option)
        print("Opción no válida. Por favor, ingrese un número entre 0 y 2.")

def show_menu_songs():
    # Muestra el menú de canciones y retorna la opción seleccionada
    while True:
        print("\nMenú Canciones:")
        print("1. Listar todas las canciones")
        print("2. Buscar canción por título")
        print("0. Volver")
        option = input("Ingrese una opción: ")
        if option.isdigit() and int(option) in (0,1,2):
            return int(option)
        print("Opción no válida. Por favor, ingrese un número entre 0 y 2.")

def show_menu_genres():
    # Muestra el menú de géneros y retorna la opción seleccionada
    while True:
        print("\nMenú Géneros:")
        print("1. Listar todos los géneros")
        print("2. Buscar género por nombre")
        print("0. Volver")
        option = input("Ingrese una opción: ")
        if option.isdigit() and int(option) in (0,1,2):
            return int(option)
        print("Opción no válida. Por favor, ingrese un número entre 0 y 2.")

def list_all_albums():
    # Lista todos los álbumes encontrados en los archivos XML del directorio 'albums'
    print("\n--- Álbumes ---")
    files = os.listdir("albums")
    for file in files:
        if file.endswith(".xml"):
            with open("albums/" + file, "r") as f:
                soup = BeautifulSoup(f, "xml")
                title = soup.find("title")
                if title:
                    print("-", title.text)

def search_album():
    # Busca álbumes que contengan el texto ingresado por el usuario
    name = input("Nombre del álbum a buscar: ").lower()
    found = False
    files = os.listdir("albums")
    for file in files:
        if file.endswith(".xml"):
            with open("albums/" + file, "r") as f:
                soup = BeautifulSoup(f, "xml")
                title = soup.find("title")
                if title and name in title.text.lower():
                    print("Encontrado:", title.text)
                    found = True
    if not found:
        print("No se encontraron álbumes con ese nombre.")

def list_all_artists():
    # Lista todos los artistas encontrados en los archivos XML del directorio 'artists'
    print("\n--- Artistas ---")
    files = os.listdir("artists")
    for file in files:
        if file.endswith(".xml"):
            with open("artists/" + file, "r") as f:
                soup = BeautifulSoup(f, "xml")
                name = soup.find("name")
                if name:
                    print("-", name.text)

def search_artist():
    # Busca artistas que contengan el texto ingresado por el usuario
    name = input("Nombre del artista a buscar: ").lower()
    found = False
    files = os.listdir("artists")
    for file in files:
        if file.endswith(".xml"):
            with open("artists/" + file, "r") as f:
                soup = BeautifulSoup(f, "xml")
                artist_name = soup.find("name")
                if artist_name and name in artist_name.text.lower():
                    print("Encontrado:", artist_name.text)
                    found = True
    if not found:
        print("No se encontraron artistas con ese nombre.")

def list_all_songs():
    # Lista todas las canciones encontradas en los archivos XML del directorio 'songs'
    print("\n--- Canciones ---")
    files = os.listdir("songs")
    for file in files:
        if file.endswith(".xml"):
            with open("songs/" + file, "r") as f:
                soup = BeautifulSoup(f, "xml")
                title = soup.find("title")
                if title:
                    print("-", title.text)

def search_song():
    # Busca canciones que contengan el texto ingresado por el usuario
    title = input("Título de la canción a buscar: ").lower()
    found = False
    files = os.listdir("songs")
    for file in files:
        if file.endswith(".xml"):
            with open("songs/" + file, "r") as f:
                soup = BeautifulSoup(f, "xml")
                song_title = soup.find("title")
                if song_title and title in song_title.text.lower():
                    print("Encontrado:", song_title.text)
                    found = True
    if not found:
        print("No se encontraron canciones con ese título.")

def list_all_genres():
    # Lista todos los géneros encontrados en los archivos XML del directorio 'genres'
    print("\n--- Géneros ---")
    files = os.listdir("genres")
    for file in files:
        if file.endswith(".xml"):
            with open("genres/" + file, "r") as f:
                soup = BeautifulSoup(f, "xml")
                name = soup.find("name")
                if name:
                    print("-", name.text)

def search_genre():
    # Busca géneros que contengan el texto ingresado por el usuario
    name = input("Nombre del género a buscar: ").lower()
    found = False
    files = os.listdir("genres")
    for file in files:
        if file.endswith(".xml"):
            with open("genres/" + file, "r") as f:
                soup = BeautifulSoup(f, "xml")
                genre_name = soup.find("name")
                if genre_name and name in genre_name.text.lower():
                    print("Encontrado:", genre_name.text)
                    found = True
    if not found:
        print("No se encontraron géneros con ese nombre.")

def main():
    # Función principal que controla el flujo del programa
    # Configuración inicial del programa
    version = 0.5
    app_title = "Playlist v" + str(version)
    print(app_title)
    print("-" * len(app_title))

    # Bucle principal del programa
    while True:
        option = show_main_menu()
        if option == 0:
            print("¡Hasta luego!")
            break
        elif option == 1:
            # Gestión del menú de álbumes
            submenu = show_menu_albums()
            if submenu == 1:
                list_all_albums()
            elif submenu == 2:
                search_album()
            # Si submenu==0, vuelve automáticamente al menú principal
        elif option == 2:
            # Gestión del menú de artistas
            submenu = show_menu_artists()
            if submenu == 1:
                list_all_artists()
            elif submenu == 2:
                search_artist()
        elif option == 3:
            # Gestión del menú de canciones
            submenu = show_menu_songs()
            if submenu == 1:
                list_all_songs()
            elif submenu == 2:
                search_song()
        elif option == 4:
            # Gestión del menú de géneros
            submenu = show_menu_genres()
            if submenu == 1:
                list_all_genres()
            elif submenu == 2:
                search_genre()

# Punto de entrada del programa
if __name__ == "__main__":
    main()


