import speech_recognition as sr
import subprocess

def reconocer_porcentaje():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di el porcentaje de brillo (0-100)...")
        audio = recognizer.listen(source)

        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            print(f"Porcentaje escuchado: {texto}")
            # Asumimos que el texto es un número
            porcentaje = int(texto)
            if 0 <= porcentaje <= 100:
                return porcentaje
            else:
                print("El porcentaje debe estar entre 0 y 100.")
                return None
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print(f"No se pudo solicitar resultados; {e}")
        except ValueError:
            print("Por favor, di un número válido entre 0 y 100.")

    return None

def ajustar_brillo(porcentaje):
    # Usa nircmd para ajustar el brillo
    command = f'nircmd.exe setbrightness {porcentaje}'
    subprocess.run(command, shell=True)
    print(f"Brillo ajustado al {porcentaje}%")

def main():
    porcentaje = reconocer_porcentaje()
    if porcentaje is not None:
        ajustar_brillo(porcentaje)
    
    # Regresar a main.py después de ajustar el brillo
    subprocess.run(['python', 'main.py'])

if __name__ == "__main__":
    main()
