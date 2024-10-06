from setuptools import setup, find_packages
import os  # Importing the os module

# Check if README.md exists before trying to read it
long_description = ""
if os.path.exists('README.md'):
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name="ai_audio_health_assistant",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.25.0",
        "speechrecognition==3.8.1",
        "gtts==2.2.3",
        "openai==0.27.4",
        "langdetect==1.0.9",
        "pyaudio==0.2.13",
        "pydub==0.25.1",
        "numpy==1.23.5"
    ],
    author="Your Name",  # Replace with your name
    description="AI Audio Health Assistant using Streamlit and OpenAI",
    long_description=long_description if long_description else "AI Audio Health Assistant",
    long_description_content_type='text/markdown',
    url="https://your-project-url",  # Replace with your project URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
