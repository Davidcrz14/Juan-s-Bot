import os
import google.generativeai as genai
from fpdf import FPDF
import speech_recognition as sr

# PRIMER CAMBIO, VE A https://aistudio.google.com/app/apikey GENERA TU KEY Y PEGALO ACA
os.environ['API_KEY'] = 'API_KEY_ACA'
genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')

def get_desktop_path():
    # PRIMER CAMBIO VE A TU ESCRITORIO COPIA LA URL Y PEGALO ACA:
    return r"C:\Users\david\OneDrive\Documentos\ondrive\OneDrive\Escritorio"

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Investigación sobre el Tema', 0, 1, 'C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, tema):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, f'Tema: {tema}', 0, 1, 'L')
        self.ln(5)
    
    def chapter_body(self, contenido):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, contenido)

def crear_pdf(tema, contenido):
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title(tema)
    pdf.chapter_body(contenido)
    
    escritorio = get_desktop_path()
    archivo_pdf = os.path.join(escritorio, f"{tema}.pdf")
    pdf.output(archivo_pdf)
    print(f"PDF creado: {archivo_pdf}")

def crear_txt(tema, contenido):
    escritorio = get_desktop_path()
    archivo_txt = os.path.join(escritorio, f"{tema}.txt")
    with open(archivo_txt, "w", encoding="utf-8") as file:
        file.write(contenido)
    print(f"TXT creado: {archivo_txt}")

def generar_contenido(tema):
    prompt = f"Genera una investigación sobre el siguiente tema {tema}"
    response = model.generate_content(prompt)
    return response.text

def ejecutar():
    print("¿Qué tipo de archivo quieres crear? Diga 'PDF' o 'TXT'.")
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            tipo_archivo = recognizer.recognize_google(audio, language="es-ES").strip().lower()
            if tipo_archivo not in ['pdf', 'txt']:
                print("Tipo de archivo no reconocido. Debe decir 'PDF' o 'TXT'.")
                return
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
            return
        except sr.RequestError as e:
            print(f"No se pudo solicitar resultados; {e}")
            return
    
    print(f"Tipo de archivo seleccionado: {tipo_archivo.upper()}")
    print("Di el tema sobre el que quieres crear el archivo.")
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            tema = recognizer.recognize_google(audio, language="es-ES").strip()
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
            return
        except sr.RequestError as e:
            print(f"No se pudo solicitar resultados; {e}")
            return

    contenido = generar_contenido(tema)
    
    if tipo_archivo == 'pdf':
        crear_pdf(tema, contenido)
    elif tipo_archivo == 'txt':
        crear_txt(tema, contenido)

if __name__ == "__main__":
    ejecutar()
