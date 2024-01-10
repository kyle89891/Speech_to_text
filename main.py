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


def main():
    while True:
        choice = input("Choose an option:\n1. Transcribe real-time audio\n2.Upload a voice message \n3. Exit\nEnter your choice: ")
        if choice == "1":
            Speech_to_text()
        elif choice == "2":
            Audio_to_text()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

main()





