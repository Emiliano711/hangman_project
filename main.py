from game import HangmanGame
from utils import save_score


def choose_difficulty():
    options = {
        "1": ("facil", "Fácil (hasta 5 letras)"),
        "2": ("medio", "Medio (6 a 8 letras)"),
        "3": ("dificil", "Difícil (9 o más letras)"),
    }
    while True:
        print("Elige la dificultad:")
        for key, (_, label) in options.items():
            print(f"{key}. {label}")
        choice = input("Opción: ").strip()
        if choice in options:
            return options[choice][0]
        print("Opción no válida. Elige 1, 2 o 3.")


def play_game(player):
    difficulty = choose_difficulty()
    game = HangmanGame(difficulty=difficulty)
    print(f"\n¡Comienza una partida de dificultad {difficulty}!")
    print(game.display_hangman())

    while not game.is_won() and not game.is_lost():
        guess = input("Ingresa una letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Error: Debes ingresar únicamente una letra.")
            continue

        if guess in game.guessed_letters:
            print("Ya habías ingresado esa letra antes. Prueba con otra.")
            continue

        if game.process_guess(guess):
            print(f"¡Correcto! La letra '{guess}' está en la palabra.")
        else:
            print(f"La letra '{guess}' no está en la palabra.")

        print(game.display_hangman())
        print(f"Letras adivinadas: {', '.join(game.guessed_letters)}")
        print(f"Progreso: {game.display_progress()}")
        print(f"Intentos restantes: {game.max_errors - game.errors}")

    if game.is_won():
        result = "victoria"
        score = 100 + (game.max_errors - game.errors) * 10
        print(f"¡Ganaste! Puntuación: {score}")
    else:
        result = "derrota"
        score = 0
        print(f"Fin del juego. La palabra era: {game.word}")

    save_score(player, difficulty, result, score)


def main():
    print("¡Bienvenido al juego del ahorcado!")
    player = input("Ingresa tu nombre: ").strip() or "Jugador"

    while True:
        play_game(player)
        if input("¿Quieres volver a jugar? (s/n): ").strip().lower() not in ("s", "si", "sí"):
            print("¡Gracias por jugar!")
            break


if __name__ == "__main__":
    main()
