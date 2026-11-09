# Juego del Ahorcado

## ¿De qué trata?
El objetivo es adivinar una palabra o frase oculta escribiendo letras una por una. 

## Reglas del juego
- Tenemos un límite de **6 intentos incorrectos**.
- Solo podemos ingresar letras (si ponemos números o símbolos, no vale).
- Los espacios o guiones de las palabras se descubren solos.
- Ganamos si adivinamos todas las letras de la palabra.
- Perdemos si se nos acaban los intentos.
- La dificultad depende de la cantidad de letras: fácil (hasta 5), medio (6 a 8) y difícil (9 o más).
- Al terminar cada partida, se guarda el jugador, el resultado y su puntuación en `scores.csv`.
- Puedes elegir si quieres volver a jugar después de cada partida.

## ¿Cómo organizamos los archivos?
Dividimos el código en varias partes para que sea más fácil de ordenar:
- `main.py`: Es el archivo principal, el que usamos para arrancar el juego.
- `game.py`: Acá guardamos las reglas y cómo funciona el juego por dentro (gestiona los intentos y el estado del juego).
             Contiene la clase HangmanGame que gestiona el estado central de la partida (palabra, letras adivinadas, límite de 6 errores) e incluye el método display_progress() para mostrar el progreso actual del tablero con guiones bajos.
- `utils.py`: Tiene funciones de ayuda (por ejemplo, la función que lee el archivo de texto y elige una palabra al azar). Incluye `get_random_word()`, encargada de leer el archivo de texto, limpiar los espacios en blanco de forma segura y seleccionar una palabra aleatoria mediante el módulo `random`.
- `wordlist.txt`: Es un archivo de texto donde anotamos las palabras que se van a usar (una por renglón).
- `scores.csv`: Se crea automáticamente para guardar las puntuaciones de las partidas.

## ¿Cómo se juega?

