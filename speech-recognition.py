from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import playmp3

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        phrase = recognizer.recognize_google(audio)
        print(f"Recognized phrase: {phrase}")

        # Welcome home sir, (Should I stay or Should I go)
        if phrase.lower() in ["wake up", "wake up daddy's", "wake up daddy's home"]:
            jarvis = gTTS(text="welcome home sir, it's good to have you back", lang='en')
            jarvis.save("./responses/output.mp3")
            playsound("./responses/output.mp3")
            playmp3.play_mp3s_from_directory("../tonyStark")

        # At your service, sir
        elif phrase.lower() in ["jarvis you there"]:
            jarvis = gTTS(text="at your service sir", lang='en')
            jarvis.save("./responses/output.mp3")
            playsound("./responses/output.mp3")
            playsound("./mp3s/jarvisStartupSound.mp3")

        # Start up Jarvis
        elif phrase.lower() in ["boot up jarvis"]:
            playsound("./mp3s/jarvisStartupSound.mp3")
        
        # End program
        elif phrase.lower() in ["shut down"]:
            jarvis = gTTS(text="Of course sir. Booting down all systems.", lang='en')
            jarvis.save("./responses/output.mp3")
            playsound("./responses/output.mp3")
            exit()

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    while True:
        listen()
