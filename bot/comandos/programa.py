import os
import speech_recognition as sr

def reconocer_programa():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di el nombre del programa que quieres abrir. Opciones: navegador, editor_de_texto, explorador_de_archivos, calculadora, discord, valorant, operagx, etc.")
        audio = recognizer.listen(source)

        try:
            programa = recognizer.recognize_google(audio, language="es-ES")
            print(f"Programa escuchado: {programa}")
            return programa.strip().lower()
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print(f"No se pudo solicitar resultados; {e}")

    return ""

def ejecutar():
    programas = {
        "navegador": "start msedge",  # Para abrir Microsoft Edge en Windows
        "editor_de_texto": "notepad",  # Para abrir el Bloc de notas en Windows
        "explorador_de_archivos": "explorer",  # Para abrir el Explorador de archivos en Windows
        "calculadora": "calc",  # Para abrir la Calculadora en Windows
        "discord": "start discord",  # Para abrir Discord en Windows
        "valorant": "start valorant",  # Para abrir Valorant en Windows
        "operagx": "start operagx",  # Para abrir Opera GX en Windows
        "chrome": "start chrome",  # Para abrir Google Chrome en Windows
        "firefox": "start firefox",  # Para abrir Mozilla Firefox en Windows
        "vlc": "start vlc",  # Para abrir VLC Media Player en Windows
        "visual_studio_code": "start code",  # Para abrir Visual Studio Code en Windows
        "excel": "start excel",  # Para abrir Microsoft Excel en Windows
        "word": "start winword",  # Para abrir Microsoft Word en Windows
        "powerpoint": "start powerpnt",  # Para abrir Microsoft PowerPoint en Windows
        "steam": "start steam",  # Para abrir Steam en Windows
        "spotify": "start spotify",  # Para abrir Spotify en Windows
        "outlook": "start outlook",  # Para abrir Microsoft Outlook en Windows
        "notepad++": "start notepad++",  # Para abrir Notepad++ en Windows
        "skype": "start skype",  # Para abrir Skype en Windows
        "zoom": "start zoom"  # Para abrir Zoom en Windows
        # Agrega más programas según tus necesidades
    }

    programa = reconocer_programa()

    if programa in programas:
        print(f"Abriendo {programa}...")
        os.system(programas[programa])
    else:
        print(f"No se reconoce el programa: {programa}")

if __name__ == "__main__":
    ejecutar()
