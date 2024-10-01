#initializer
import speech_recognition as sr
from googlesearch import search
import gtts #For generating audio from text, see tests.py

def speechRecog (r, mic):
    with mic as source: #Setup
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    response = { #Response dict, refreshes each time
        "error": None,
        "transcription": None
    }

    print("Processing, please wait...")

    try:
        response["transcription"] = r.recognize_google(audio) #Google module because it works
    except sr.RequestError: #Basic request error
        raise Exception("API Error")
    except sr.UnknownValueError: #For some reason VR decides to throw error at this
        response["error"] = "Unable to recognize speech"

    return response

#Main
r = sr.Recognizer()
mic = sr.Microphone() #Dependent on pyaudio

while True: #Full loop
    print("Now Listening...")

    response = speechRecog(r, mic) #Page for a response

    if response["error"] == "Unable to recognize speech":
        print("I didn't catch that. Please try again.")

    elif response["transcription"] == "exit":
        break

    print(response["transcription"])

''' # Voice asssistant, leave for later
    else:
        print(response["transcription"])
        if "search" in response["transcription"]:
            print("Searching...")
            
            query = response["transcription"].replace("search","") #remove the word search
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j) #Print all results
            time.sleep(1.3) #User friendly

        
    '''