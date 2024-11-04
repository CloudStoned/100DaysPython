import pyttsx3
from gtts import gTTS
import PyPDF2

def pdf_t2s_pyttsx3(file_path):
    text_speech = pyttsx3.init()

    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            if text:
                print(f'Reading Page {page_num + 1} with pyttsx3...')
                text_speech.say(text)
        
    text_speech.runAndWait()
    print('Finished reading PDF w/ pyttsx3')

def pdf_t2s_gtts(file_path, mp3_save_path):
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Combine text from all pages
        full_txt = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            if text:
                full_txt += text
    
    tts = gTTS(text=full_txt, lang='en')
    tts.save(mp3_save_path)
    print(f'Audio has been saved as {mp3_save_path} using gTTs.')

pdf = r"C:\Users\Kraum\PROJECTS\100DaysPython\Text2Speech\test_pdf_for_audiobook.pdf"
mp3_save_path = r"C:\Users\Kraum\PROJECTS\100DaysPython\Text2Speech\audiobook.mp3"

# pdf_t2s_pyttsx3(pdf)  
pdf_t2s_gtts(pdf, mp3_save_path) 
