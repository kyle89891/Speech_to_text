import whisper
import speech_recognition as sr

def Speech_to_text():
    r1 = sr.Recognizer()

    mic = sr.Microphone()

    print('Hey! You can speak now')
    print('Tell me How is your day?')
    with mic as source:
        audio = r1.listen(source)
    print('Thank You! for Speaking')
    print('This is your text')
    print(r1.recognize_google(audio))

def Audio_to_text():
    audio="audio.mp3"
    model = whisper.load_model("base")
    result = model.transcribe(audio,fp16=False)
    print(result["text"])


option=int(input("Press 1 for Speaking or Press 2 for Audio File: "))
if(option==1):
    Speech_to_text()
elif(option==2):
    Audio_to_text()
else:
    print("please enter valid option")





