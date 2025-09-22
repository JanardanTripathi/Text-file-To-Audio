import pypdf
import pyttsx3
from pypdf import PdfReader
from tkinter.filedialog import askopenfilename

book=askopenfilename()
pdfReader=pypdf.PdfReader(book)
pages=pdfReader.get_num_pages()
for num in range(0,pages):
    page=pdfReader.get_page(num)
    text=page.extract_text()
    player=pyttsx3.init()
    player.say(text)
    player.runAndWait()