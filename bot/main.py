import speech_recognition as sr
import subprocess  # Para ejecutar comandos de sistema
import os

def reconocer_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di el comando....")
        audio = recognizer.listen(source)

        try:
            comando = recognizer.recognize_google(audio, language="es-ES")
            print(f"Comando escuchado: {comando}")
            return comando
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print(f"No se pudo solicitar resultados; {e}")

    return ""

def ejecutar_comando(comando):
    if comando.lower().startswith("Juan abre"):
        print("Llamando a comandos/programa.py...")
        subprocess.run(["python", "comandos/programa.py"])
    elif comando.lower().startswith("juan crea"):
        print("Llamando a comandos/crea.py...")
        subprocess.run(["python", "comandos/crea.py"])
    elif comando.lower().startswith("Juan platiquemos"):
        print("Llamando a comandos/platica.py...")
        subprocess.run(["python", "comandos/chat.py"])
    elif comando.lower().startswith("Juan volumen"):
        print("Llamando a comandos/volumen.py...")
        subprocess.run(["python", "comandos/volumen.py"])
    elif comando.lower().startswith("Juan brillo"):
        print("Llamando a comandos/brillo.py...")
        subprocess.run(["python", "comandos/brillo.py"])            
    else:
        print(f"Comando no reconocido: {comando}")

if __name__ == "__main__":
    while True:
        comando = reconocer_comando()
        if comando:
            ejecutar_comando(comando)
