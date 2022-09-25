import pyttsx3

import pdfplumber

import PyPDF2

file = 'c:/users/<user_name>/desktop/book.pdf'

path = open(file, 'rb')

pdf_reader = PyPDF2.PdfFileReader(path)

# pages = pdfreader.open(file) as pdf

speaker = pyttsx3.init()

for pages in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pages)
    text = page.extractText()
    print(text)
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()
