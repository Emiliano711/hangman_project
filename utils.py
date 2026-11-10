import random
import csv
from pathlib import Path

DIFFICULTY_RANGES = {
    "facil": (1, 5),
    "medio": (6, 8),
    "dificil": (9, None),
}

def get_random_word(filepath="wordlist.txt", difficulty=None):
    """
    Lee las palabras del archivo y devuelve una al azar, opcionalmente
    filtrada por dificultad según la cantidad de letras.
    """
    wordlist_path = Path(filepath)
    if not wordlist_path.is_absolute():
        wordlist_path = Path(__file__).parent / wordlist_path

    with wordlist_path.open("r", encoding="utf-8") as file:
        words = [
            line.strip()
            for line in file
            if line.strip().isalpha()
        ]

    if not words:
        raise ValueError(
            f"No hay palabras compuestas solo por letras en '{wordlist_path}'."
        )

    if difficulty is not None:
        if difficulty not in DIFFICULTY_RANGES:
            raise ValueError(f"Dificultad no válida: '{difficulty}'.")

        min_length, max_length = DIFFICULTY_RANGES[difficulty]
        words = [
            word for word in words
            if min_length <= len(word)
            and (max_length is None or len(word) <= max_length)
        ]

        if not words:
            raise ValueError(
                f"No hay palabras válidas para la dificultad '{difficulty}' "
                f"en '{wordlist_path}'."
            )

    return random.choice(words)


def save_score(player, difficulty, result, score, filepath="scores.csv"):
    """Guarda el resultado de una partida en un archivo CSV."""
    scores_path = Path(filepath)
    if not scores_path.is_absolute():
        scores_path = Path(__file__).parent / scores_path

    file_exists = scores_path.exists() and scores_path.stat().st_size > 0
    with scores_path.open("a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["jugador", "dificultad", "resultado", "puntuacion"])
        writer.writerow([player, difficulty, result, score])
