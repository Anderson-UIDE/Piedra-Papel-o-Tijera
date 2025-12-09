import random  # Se usa para que la computadora elija piedra, papel o tijera

print("Bienvenido al juego Piedra, Papel o Tijera.")
print("Elige una opción:")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

opcion = input("Ingresa el número de tu elección: ")

# Conversión del número a texto (lógica básica)
if opcion == "1":
    usuario = "piedra"
elif opcion == "2":
    usuario = "papel"
elif opcion == "3":
    usuario = "tijera"
else:
    print("Opción no válida. El programa terminará.")
    exit()  # Termina el programa si la opción no es correcta

# Elección aleatoria del PC
opciones = ["piedra", "papel", "tijera"]
pc = random.choice(opciones)

print("\nTú elegiste:", usuario)
print("La computadora eligió:", pc)

# Lógica básica para determinar el resultado
if usuario == pc:
    print("Resultado: Empate.")
elif (usuario == "piedra" and pc == "tijera") or \
     (usuario == "tijera" and pc == "papel") or \
     (usuario == "papel" and pc == "piedra"):
    print("Resultado: Ganaste.")
else:
    print("Resultado: Perdiste.")


