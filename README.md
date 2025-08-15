Gemini AI Chatbot with Tkinter

A simple desktop chatbot application built with Python's Tkinter library that connects to the Google Gemini AI model. This provides a clean graphical user interface (GUI) for real-time conversations with the AI.

✨ Features
Simple and Intuitive GUI: A straightforward chat window and input field for easy interaction.

Real-time AI Conversation: Connects directly to Google's powerful gemini-1.5-flash model.

Styled Chat Display: User prompts and AI responses are styled differently for better readability.

Follow-Up Functionality: Includes a dedicated button to ask the AI to elaborate on its most recent response.

Markdown Cleaning: A utility function removes basic Markdown formatting (like * or #) for a cleaner text display in the chat window.

📋 Prerequisites
Before you begin, ensure you have the following:

Python 3.8 or newer installed.

A Google Generative AI API Key. You can obtain one for free from the Google AI Studio.

🚀 Setup and Installation
Follow these steps to get the chatbot running on your local machine.

Clone the repository (or save the script to a local file).

Bash

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
(Recommended) Create and activate a virtual environment:

Bash

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
Install the required packages:

Bash

pip install google-generativeai
Add your API Key:
Open the main Python script in a text editor and find the following line:

Python

genai.configure(api_key="your_api_key")
Replace "your_api_key" with your actual Google Generative AI API key.

🏃‍♂️ How to Run
Once the setup is complete, run the application from your terminal with the following command:

Bash

python your_script_name.py
💬 How to Use
Type your question into the input box at the bottom of the window.

Click the "Prompt" button to send your question to the AI.

The conversation will appear in the main chat window.

Click the "Prompt Follow-Up" button at any time to ask the AI "Can you elaborate on that?" based on the current context.
