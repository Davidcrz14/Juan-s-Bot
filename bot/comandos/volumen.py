import subprocess
import speech_recognition as sr

def set_volume(percent):
    volume_percent = max(0, min(percent, 100))
    
    command = f'nircmd.exe setsysvolume {int(volume_percent * 65535 / 100)}'
    subprocess.run(command, shell=True)
    print(f"Volumen ajustado al {volume_percent}%")

def get_volume_from_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Por favor, diga el porcentaje de volumen (0-100):")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print(f"Usted dijo: {text}")

        percent = int(text.split()[0])
        if percent < 0 or percent > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100.")
        
        return percent
    except sr.UnknownValueError:
        print("No se entendió el audio. Intente nuevamente.")
        return None
    except sr.RequestError:
        print("Error con el servicio de reconocimiento de voz. Intente nuevamente.")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    while True:
        percent = get_volume_from_speech()
        if percent is not None:
            set_volume(percent)
            break

if __name__ == "__main__":
    main()
