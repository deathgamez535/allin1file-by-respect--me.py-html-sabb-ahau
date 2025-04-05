import openai
import speech_recognition as sr
from gtts import gTTS
from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch
import os
from PIL import Image
import requests
from io import BytesIO
import time

# Set up OpenAI API Key (replace with your own API key)
openai.api_key = 'your-openai-api-key'

# Initialize the NLP pipeline (Huggingface GPT-2 for text generation)
nlp = pipeline("text-generation", model="gpt2")

# Stable Diffusion model for image generation
def generate_image(prompt):
    try:
        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4-original", torch_dtype=torch.float16)
        pipe.to("cuda")  # Use GPU if available

        image = pipe(prompt).images[0]
        image.show()  # Show image
        image.save("generated_image.png")
        print("Image saved as 'generated_image.png'")
    except Exception as e:
        print(f"Error generating image: {e}")

# Text-to-Speech Function
def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("start output.mp3")  # For Windows, adjust for other systems if needed
        print("Speech saved and playing.")
    except Exception as e:
        print(f"Error converting text to speech: {e}")

# Speech-to-Text Function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for speech...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized Speech: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the speech.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
        return ""

# Chat and Question Answering using GPT-3
def chat_with_ai(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # GPT-3 model
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating AI response: {e}")
        return "Sorry, I couldn't process that request."

# Code Generation using GPT-3
def generate_code(prompt):
    return chat_with_ai(f"Generate code: {prompt}")

# Task-oriented answers (like weather, facts, etc.)
def task_answering(task):
    # Example for weather (you can expand more tasks here)
    if 'weather' in task.lower():
        return "The weather is sunny with a temperature of 25°C."
    else:
        return chat_with_ai(f"Answer this task: {task}")

# Main Function
def main():
    print("AI Assistant is Ready!")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Chat with AI")
        print("2. Generate code")
        print("3. Generate Image")
        print("4. Text to Speech")
        print("5. Speech to Text")
        print("6. Task-oriented Answer (e.g., weather)")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            prompt = input("Enter your question or conversation prompt: ")
            response = chat_with_ai(prompt)
            print("AI Response:", response)
            text_to_speech(response)
        elif choice == "2":
            prompt = input("Enter the task or problem you want code for: ")
            response = generate_code(prompt)
            print("Generated Code:", response)
            text_to_speech(response)
        elif choice == "3":
            prompt = input("Enter the text for image generation: ")
            generate_image(prompt)
        elif choice == "4":
            text = input("Enter the text to convert to speech: ")
            text_to_speech(text)
        elif choice == "5":
            speech_text = speech_to_text()
            if speech_text:
                print("You said:", speech_text)
                response = chat_with_ai(speech_text)
                print("AI Response:", response)
                text_to_speech(response)
        elif choice == "6":
            task = input("Enter the task you want assistance with: ")
            response = task_answering(task)
            print("Task Response:", response)
            text_to_speech(response)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the main program
if __name__ == "__main__":
    main()
