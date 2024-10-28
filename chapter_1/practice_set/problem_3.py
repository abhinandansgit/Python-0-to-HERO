# Install an external module and use it to perform an operation of your interest.
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. o for male 1 for female 
engine.say("Hii Abhinandan, I am your virtual assistant!")
voices = engine.getProperty('voices')   
engine.runAndWait()
engine.stop()
