import os
import google.generativeai as genai
from gtts import gTTS
import speech_recognition as sr
import io
import pygame

# PRIMER CAMBIO, VE A https://aistudio.google.com/app/apikey GENERA TU KEY Y PEGALO ACA
os.environ['API_KEY'] = 'API_KEY_ACA'
genai.configure(api_key=os.environ['API_KEY'])

# Configura el modelo de IA
model = genai.GenerativeModel(
    'gemini-1.5-flash',
    generation_config=genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=0.2,
    )
)

pygame.init()
pygame.mixer.init()

def text_to_speech(text):
    tts = gTTS(text=text, lang='es')
    with io.BytesIO() as audio_file:
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  
            pygame.time.Clock().tick(10)

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        return text
    except sr.UnknownValueError:
        print("No se entendió el audio")
        return None
    except sr.RequestError:
        print("Error con el servicio de reconocimiento de voz")
        return None

def ejecutar():
    while True:
        texto = speech_to_text()
        
        if texto and texto.lower() == "dejemos de platicar":
            print("Terminando conversación.")
            break
        
        if texto:
            print(f"Tú dijiste: {texto}")
            prompt = f"Responde a la siguiente conversación: {texto}"
            respuesta = model.generate_content(prompt).text
            
            print(f"Respuesta: {respuesta}")
            text_to_speech(respuesta)

    import subprocess
    subprocess.run(['python', 'main.py'])

if __name__ == "__main__":
    ejecutar()
