import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext
import re

# Configure Google Generative AI
genai.configure(api_key="your_api_key")
model = genai.GenerativeModel("gemini-1.5-flash")


def clean_markdown(response_text):
    """Function to remove Markdown formatting (like * for bold, _ for italics)."""
    cleaned_text = re.sub(
        r"(\{1,2}|_{1,2})(.?)\1", r"\2", response_text
    )  # Remove bold/italic
    cleaned_text = re.sub(
        r"[\[`*_#]+", "", cleaned_text
    )  # Remove other Markdown characters
    return cleaned_text


def ask_question():
    """Send the user input to the Generative AI model and display the response."""
    user_input = user_entry.get()
    if not user_input.strip():
        return

    chat_window.insert(tk.END, f"You: {user_input}\n", "user_text")
    user_entry.delete(0, tk.END)

    try:
        response = model.generate_content(user_input)
        ai_response = clean_markdown(response.text)
    except Exception as e:
        ai_response = f"Error: {str(e)}"

    chat_window.insert(tk.END, f"AI: {ai_response}\n", "ai_text")
    chat_window.see(tk.END)


def ask_followup():
    """Send a follow-up question based on the previous interaction."""
    follow_up_prompt = "Can you elaborate on that?"
    chat_window.insert(tk.END, f"You: {follow_up_prompt}\n", "user_text")

    try:
        response = model.generate_content(follow_up_prompt)
        ai_response = clean_markdown(response.text)
    except Exception as e:
        ai_response = f"Error: {str(e)}"

    chat_window.insert(tk.END, f"AI: {ai_response}\n", "ai_text")
    chat_window.see(tk.END)


# Create the main window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("600x500")
root.configure(bg="#F0F8FF")

# Create the chat window
chat_window = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    state="normal",
    width=60,
    height=20,
    font=("Arial", 12),
    bg="#FFFFFF",
    fg="#000000",
)
chat_window.tag_configure("user_text", foreground="#1E90FF", font=("Arial", 12, "bold"))
chat_window.tag_configure("ai_text", foreground="#32CD32", font=("Arial", 12, "italic"))
chat_window.pack(pady=10, padx=10)

# Create the input frame
input_frame = tk.Frame(root, bg="#F0F8FF")
input_frame.pack(pady=5)

# Entry widget for user input
user_entry = tk.Entry(
    input_frame, width=45, font=("Arial", 12), bg="#FFFACD", fg="#000000"
)
user_entry.grid(row=0, column=0, padx=5)


# Button styles
def create_button(parent, text, command, bg_color, fg_color):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 12, "bold"),
        bg=bg_color,
        fg=fg_color,
        relief=tk.RAISED,
        borderwidth=3,
        activebackground="#FFA07A",
    )


# Button to send the question
ask_button = create_button(input_frame, "prompt", ask_question, "#1E90FF", "#FFFFFF")
ask_button.grid(row=0, column=1, padx=5)

# Button for follow-up question
followup_button = create_button(
    root, "prompt Follow-Up", ask_followup, "#32CD32", "#FFFFFF"
)
followup_button.pack(pady=5)

# Run the application
root.mainloop()