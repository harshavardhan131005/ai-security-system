# AI Security System (Face, Voice, and Email Integration)

## Overview
This project is a multi-modal AI-based security system that integrates face recognition, voice authentication, and email automation into a single platform. The system is designed to enhance security by combining multiple layers of user verification.

## Features
- Face detection using OpenCV
- Voice recording and processing using PyAudio
- Email sending and inbox access
- Modular and scalable code structure
- Easy to extend for additional features

## Technologies Used
- Python
- OpenCV
- TensorFlow / Keras
- PyAudio
- SpeechRecognition
- Scikit-learn

## Project Structure
The project follows a modular architecture for better maintainability and scalability:

- `face/` – Handles face detection and encoding
- `voice/` – Manages voice recording, feature extraction, and recognition
- `email_module/` – Contains email sending and inbox functionalities
- `utils/` – Utility functions such as speech output and logging
- `models/` – Pre-trained models and trained data
- `data/` – Stores user-related data (face and voice)
- `main.py` – Entry point of the application

## How to Run
1. Install the required dependencies:

2. Run the main application:

## Notes
- Ensure that your system has a working webcam and microphone.
- Place the required machine learning models in the `models/` directory.
- For email functionality, use valid credentials and configure access permissions if required.

## Future Improvements
- Graphical user interface (GUI)
- Real-time authentication dashboard
- Mobile application integration
- Enhanced security mechanisms

## Author
Harsha Vardhan
