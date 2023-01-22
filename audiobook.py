import PyPDF2
import pyttsx3
book = open('poems.pdf', 'rb')
pdfRead = PyPDF2.PdfReader(book)
pages = len(pdfRead.pages)
print("total number of pages:",pages)
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 140)
for num in range(0,pages):
    page = pdfRead.pages[num]
    text = page.extract_text()
    speaker.say(text)
    print("\n",text)
    speaker.runAndWait()
    num=num+1
