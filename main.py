
"""
Juego: Piedra, Papel o Tijera
Autor: (tu nombre)
Descripción:
Este programa permite al usuario jugar Piedra, Papel o Tijera contra la computadora.
Incluye:
- Estructuras lógicas (if, elif, else)
- Estructuras repetitivas (while)
- Comentarios en las partes más importantes del código
"""

import random  # Importamos la librería para generar elecciones aleatorias del PC


def obtener_opcion_usuario():
    """
    Muestra el menú al usuario y devuelve su elección como texto.
    Esta función incluye validación para evitar opciones incorrectas.
    """
    print("\n=== JUEGO: PIEDRA, PAPEL O TIJERA ===")
    print("Elige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir del juego")

    opcion = input("Ingresa el número de tu elección: ")

    # Estructura lógica para validar la entrada del usuario
    if opcion == "1":
        return "piedra"
    elif opcion == "2":
        return "papel"
    elif opcion == "3":
        return "tijera"
    elif opcion == "4":
        return "salir"
    else:
        # Si el usuario ingresa algo incorrecto, devolvemos None
        print("❌ Opción no válida. Intenta de nuevo.")
        return None


def obtener_opcion_pc():
    """
    Genera y devuelve aleatoriamente la elección de la computadora.
    """
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)


def determinar_resultado(usuario, pc):
    """
    Determina el resultado de la ronda según las reglas:
    - Piedra gana a Tijera
    - Tijera gana a Papel
    - Papel gana a Piedra
    Devuelve un texto: 'ganaste', 'perdiste' o 'empate'.
    """
    # Si ambas elecciones son iguales, es empate
    if usuario == pc:
        return "empate"

    # A continuación se utilizan estructuras lógicas para evaluar los casos de victoria
    if (
        (usuario == "piedra" and pc == "tijera") or
        (usuario == "tijera" and pc == "papel") or
        (usuario == "papel" and pc == "piedra")
    ):
        return "ganaste"
    else:
        return "perdiste"


def jugar():
    """
    Función principal del juego.
    Usa un bucle while (estructura repetitiva) para permitir jugar varias rondas.
    """
    print("Bienvenido al juego Piedra, Papel o Tijera.")

    # Estructura repetitiva: el juego continúa hasta que el usuario decida salir
    while True:
        opcion_usuario = obtener_opcion_usuario()

        # Si la opción es None, se repite el ciclo sin continuar el juego
        if opcion_usuario is None:
            continue

        # Si el usuario elige salir, se rompe el ciclo y termina el juego
        if opcion_usuario == "salir":
            print("👋 Gracias por jugar. ¡Hasta la próxima!")
            break

        # Elección de la computadora
        opcion_pc = obtener_opcion_pc()

        # Mostramos las elecciones
        print(f"\nTú elegiste: {opcion_usuario}")
        print(f"La computadora eligió: {opcion_pc}")

        # Determinar el resultado de la ronda
        resultado = determinar_resultado(opcion_usuario, opcion_pc)

        # Mostrar el resultado al usuario
        if resultado == "empate":
            print("🤝 Resultado: ¡Empate!")
        elif resultado == "ganaste":
            print("🏆 Resultado: ¡Ganaste la ronda!")
        else:
            print("😢 Resultado: Perdiste la ronda.")

        # El bucle while permite jugar de nuevo automáticamente


# Punto de entrada del programa
if __name__ == "__main__":
    jugar()
