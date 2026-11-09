from utils import get_random_word

class HangmanGame:
    def __init__(self, word=None, difficulty=None):
        # Si no se pasa una palabra, usamos get_random_word() por defecto
        self.word = word if word else get_random_word(difficulty=difficulty)
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_hangman(self):
        """Devuelve el dibujo del ahorcado correspondiente a los errores."""
        stages = [
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
        ]
        return stages[min(self.errors, self.max_errors)]

    def display_progress(self):
        """
        Muestra el estado actual de la palabra (por ejemplo, "_ _ e _ _ a _ _")
        revelando las letras adivinadas y ocultando las demás con guiones bajos.
        """
        progress = []
        for char in self.word:
            # Si el caracter es un espacio u otro símbolo, o si ya fue adivinado:
            if char.lower() in self.guessed_letters or not char.isalpha():
                progress.append(char)
            else:
                progress.append("_")
        
        # Unimos todo con espacios para que se vea prolijo
        return " ".join(progress)

    def is_won(self):
        """Indica si todas las letras de la palabra fueron adivinadas."""
        return all(
            not char.isalpha() or char.lower() in self.guessed_letters
            for char in self.word
        )

    def is_lost(self):
        """Indica si se alcanzó el máximo de errores permitidos."""
        return self.errors >= self.max_errors

    def process_guess(self, letter): 
        """
        Procesa la letra adivinada por el jugador.
        Si la letra ya fue adivinada, no hace nada.
        Si la letra está en la palabra, se agrega a guessed_letters.
        Si no está, se incrementa el contador de errores.
        """
        letter = letter.lower()
        is_correct = letter in self.word.lower()

        if letter in self.guessed_letters:
            return is_correct  # Ya fue adivinada, no hacemos nada

        self.guessed_letters.append(letter)

        if not is_correct:
            self.errors += 1  # Incrementamos errores si la letra no está en la palabra 

        return is_correct
    