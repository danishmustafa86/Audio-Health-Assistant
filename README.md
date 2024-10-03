# Real-time Multilingual Audio Health Assistant

## Introduction

The **Real-time Multilingual Audio Health Assistant** is an intelligent voice-based application designed to assist users in managing their health. It integrates speech recognition, language detection, medical condition assessment, and real-time text-to-speech generation, providing a seamless, conversational experience for users.

This project is designed to detect symptoms based on user voice input and provide tailored advice in different languages. The assistant can also check common medical conditions and generate responses using the **AIML API** with an embedded AI model.

## Key Features
- **Voice-to-Text Conversion**: Translates user speech into text using Google SpeechRecognition.
- **Multilingual Support**: Detects the language of the input text and provides responses in the detected language or the user's preferred language.
- **Medical Condition Checker**: Checks user-reported symptoms against a mock medical database for common conditions (e.g., fever, headache).
- **AI-Powered Responses**: Utilizes the **AIML API** to generate AI responses based on the user's symptoms and health conditions.
- **Text-to-Speech**: Converts AI-generated text responses back into audio and plays it for the user in real-time.
- **Audio Control**: Allows users to control audio playback, stop, repeat responses, and seek backward in the audio.
- **User Profile Management**: Customizes responses based on the user's age, weight, and language preferences.
  
## Technologies Used
1. **SpeechRecognition**: Used for converting audio to text.
2. **gTTS (Google Text-to-Speech)**: Converts text responses to speech.
3. **OpenAI AIML API**: Provides AI-based responses based on user queries and health conditions.
4. **Langdetect**: Automatically detects the language of the input text.
5. **Sounddevice & Pydub**: For playing back audio responses.
6. **Streamlit**: Used to create an interactive web-based user interface.

## Industry Impact
- **Healthcare Support**: The project acts as a virtual assistant for users to get basic health information and guidance in multiple languages. It can be a valuable tool for first-line support and monitoring.
- **Multilingual Capability**: By supporting a wide range of languages, it can assist non-English-speaking users, which is vital in areas with linguistic diversity.
- **Telemedicine Integration**: This assistant has the potential to integrate with telemedicine services, providing preliminary analysis and advice.

### Competitors
- **Google Health Assistant**: Offers symptom checking and advice but lacks multilingual and voice-driven symptom detection.
- **Babylon Health**: Provides AI-based healthcare services, including symptom checking, but lacks extensive voice integration.
- **Ada Health**: A symptom checker that uses an AI-powered chatbot but does not support the same level of real-time audio interaction.

## Operations
This assistant performs the following operations:
1. **Real-time Symptom Checking**: Users can describe their symptoms using their voice, and the assistant will offer basic advice.
2. **Multilingual Interaction**: Automatically detects the language of the user and responds in that language.
3. **AI-Powered Conversation**: Provides AI-generated responses based on user inputs and health conditions.
4. **Text-to-Speech Playback**: Plays the AI's responses as audio, allowing users to engage with the assistant hands-free.

## Project Qualities
- **Real-time Audio Processing**: Provides instant responses to user voice inputs.
- **Multilingual Support**: Detects and adapts to the user's language preference.
- **User-Friendly Interface**: Uses **Streamlit** to deliver a simple, easy-to-use interface.
- **Medical Condition Advice**: Offers basic health advice based on recognized symptoms.

## How to Install and Run on Your PC

### Install the Required Libraries
```bash
pip install SpeechRecognition gtts streamlit openai langdetect sounddevice numpy pydub
### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname
