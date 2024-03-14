import PyPDF2
from gtts import gTTS

# Abre el archivo PDF
with open('gaming2.pdf', 'rb') as pdf_file:
    # Crea un objeto PDFFileReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Inicializa una cadena vacía para almacenar el texto
    texto = ""

    # Extrae el texto de cada página
    for page_number in range(len(pdf_reader.pages)):
        pagina = pdf_reader.pages[page_number]
        texto += pagina.extract_text()

# Convierte el texto a audio
audio = gTTS(text=texto, lang='es')

# Guarda el audio en un archivo
audio.save("gaming2.mp3")
