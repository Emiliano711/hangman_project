# main.py - Tarea 3: Manejar la entrada del usuario
guessed_letters = []

while True:
    # 1. Pedir la letra al usuario y pasarla a minúsculas
    guess = input("Ingresa una letra: ").lower()
    
    # 2. Validar que sea una sola letra y que sea alfabética
    if len(guess) != 1 or not guess.isalpha():
        print("Error: Debes ingresar únicamente una letra.")
        continue
        
    # 3. Validar que no se haya adivinado antes
    if guess in guessed_letters:
        print("Ya habías ingresado esa letra antes. Prueba con otra.")
        continue
        
    # Si pasa las validaciones, la agregamos a la lista y salimos
    guessed_letters.append(guess)
    print(f"¡Letra válida aceptada: {guess}!")
    break
