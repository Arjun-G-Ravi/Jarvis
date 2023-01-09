import pyttsx3
import datetime
import speech_recognition as sr 
engine = pyttsx3.init('sapi5') 
def write(audio):        #also prints the words
     print('JARVIS: ' + audio) 
     engine.say(audio) 
     engine.runAndWait()

def speak(audio):            #just voice
     engine.say(audio) 
     engine.runAndWait()                                                             

 
def greet(): 
    currentH = int(datetime.datetime.now().hour) 
    if currentH >= 5 and currentH < 12: 
         speak('Good Morning!') 
    elif currentH >= 12 and currentH < 16: 
        speak('Good Afternoon!') 
    else: 
         speak('Good Evening!') 


def myCommand(): 
    r = sr.Recognizer()                                                                                    
    with sr.Microphone() as source:                                                                        
     print("Listening...") 
     r.pause_thresholdld =  1 
     audio = r.listen(source) 
    try: 
     query = r.recognize_google(audio, language='en-in') 
     print('USER:' + query + '\n') 
      
    except sr.UnknownValueError: 
     speak('Sorry sir! I didn\'t get that! Try typing the command!') 
     query = str(input('Command: ')) 
    return query 
