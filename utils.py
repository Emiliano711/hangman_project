import random

def get_random_word(filepath="wordlist.txt"):
    """
    Lee las palabras del archivo y devuelve una al azar.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            # Lee cada línea y le quita los espacios o saltos de línea vacíos
            words = [line.strip() for line in file if line.strip()]
            
        if words:
            return random.choice(words)
        else:
            return "python"
    except FileNotFoundError:
        return "ahorcado"
