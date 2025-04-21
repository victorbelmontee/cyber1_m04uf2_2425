#!/usr/bin/pyhton3

version = 0.5
app_title = "Playlist v" + str(version)
print(app_title)
print("-" * len(app_title))

def saluda ():
	print("Hola!")


def suma (num1, num2):
	return num1+num2


def despide(quien="Jacinto"):
	print("Estas despedido", quien)


def retorna_multiple ():
	uno = 1
	dos = 3
	return uno, dos


if True:
	print("Cierto")
else:
	print("Falso")


primero = 5 
segundo = 5

if primero > segundo:
	print("El primero es mayor que el segundo")
elif primero < segundo:
	print("El segundo es mayor que el primero")
else:
	print("Son iguales")


contador = 10

while contador > 0:
	print(contador)
	contador-=1



for num in range (10):
	print(num)


personas = ["Jacinto", "Jaimito", "33", "Anselmito"]

for dato in personas:
	print(">", dato)


personaje = {

	"nombre": "Paquito",
	"edad": 33,
	"pelo": "marrón"
}

#print("Personaje:", personaje["nombre"])


for clave in personaje:
	print(">>", clave, personaje[clave])

for clave, valor in personaje.items():

	print(">>>", clave, valor)

saluda()

resultado = suma(3,5)

print(resultado)


despide()

despide("Ramiro")

valor1, valor2 = retorna_multiple()

print("Valores:", valor1, valor2)
