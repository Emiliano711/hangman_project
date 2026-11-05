# Juego del Ahorcado

## ¿De qué trata?
El objetivo es adivinar una palabra o frase oculta escribiendo letras una por una. 

## Reglas del juego
- Tenemos un límite de **6 intentos incorrectos**.
- Solo podemos ingresar letras (si ponemos números o símbolos, no vale).
- Los espacios o guiones de las palabras se descubren solos.
- Ganamos si adivinamos todas las letras de la palabra.
- Perdemos si se nos acaban los intentos.

## ¿Cómo organizamos los archivos?
Dividimos el código en varias partes para que sea más fácil de ordenar:
- `main.py`: Es el archivo principal, el que usamos para arrancar el juego.
- `game.py`: Acá guardamos las reglas y cómo funciona el juego por dentro.
- `utils.py`: Tiene funciones de ayuda (por ejemplo, la función que lee el archivo de texto y elige una palabra al azar).
- `wordlist.txt`: Es un archivito de texto donde anotamos las palabras que se van a usar (una por renglón).

## ¿Cómo se juega?
Para probarlo, abres la terminal en la carpeta del proyecto y escribes este comando:

```bash
python main.py
