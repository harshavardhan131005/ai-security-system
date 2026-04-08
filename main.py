from utils.speech import speak
from face.face_recognition import detect_face
from voice.audio_utils import record_audio

def main():
    speak("System Started")

    print("1. Face Detection")
    print("2. Record Voice")

    choice = input("Enter your choice: ")

    if choice == "1":
        detect_face()
    elif choice == "2":
        record_audio()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
