import random
import json
import torch
import tkinter as tk
from tkinter import scrolledtext
import mysql.connector
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from datetime import datetime

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="chatbot"
)
cursor = conn.cursor()

# Load the chatbot model and data
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('D:/chatbot_project3/chatbot-deployment-main/intent.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "D:/chatbot_project3/chatbot-deployment-main/data_Nego.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "I do not understand..."

# Function to save conversation to the database
def save_to_db(user_input, bot_response):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = "INSERT INTO interactions (user_input, bot_response, timestamp) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_input, bot_response, timestamp))
    conn.commit()

# Define the UI using Tkinter
def send():
    user_input = entry.get()
    chat_area.configure(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_input}\n")
    entry.delete(0, tk.END)
    
    if user_input.lower() == "quit":
        root.destroy()
        cursor.close()
        conn.close()
        return
    
    response = get_response(user_input)
    chat_area.insert(tk.END, f"{bot_name}: {response}\n")
    chat_area.configure(state=tk.DISABLED)
    chat_area.yview(tk.END)
    
    # Save the conversation to the database
    save_to_db(user_input, response)

# Initialize the Tkinter root window
root = tk.Tk()
root.title("Chatbot")

# Chat area with a scrollbar
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_area.configure(state=tk.DISABLED)
chat_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Entry field for user input
entry = tk.Entry(root, width=80)
entry.pack(padx=20, pady=10)

# Button to send the message
send_button = tk.Button(root, text="Send", command=send)
send_button.pack(pady=5)

# Bind the Enter key to the send function
root.bind('<Return>', lambda event: send())

# Start the Tkinter event loop
root.mainloop()
