# E-commerce FAQ Chatbot

## Project Description

This project is an AI-powered FAQ chatbot designed for e-commerce platforms. The chatbot provides instant, accurate responses to user queries, enhancing the user experience and streamlining customer support. The project integrates machine learning with a graphical user interface and a database to manage conversations.

### Key Features

- **AI-Powered Responses**: Uses a neural network model built with PyTorch to understand and respond to user inputs with high accuracy.
- **Database Integration**: Conversations are stored in a MySQL database for analysis and improvement.
- **User Interface**: Provides an interactive chat interface using Tkinter for a seamless user experience.

## Technologies Used

- **Backend:**
  - Python
  - PyTorch
  - MySQL

- **Frontend:**
  - Tkinter (for UI)

## Files

- `chat.py`: Main script to run the chatbot with Tkinter UI and MySQL integration.
- `data.pth`: Saved model state and metadata (deprecated).
- `data.nego.pth`: Latest model state and metadata.
- `intent.json`: JSON file containing chatbot intents and responses.
- `model.py`: Contains the definition of the neural network model.
- `nltk_utils.py`: Contains utility functions for tokenizing and processing text.
- `train.py`: Script for training the chatbot model.

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/ecommerce_faq_chatbot.git
   cd ecommerce_faq_chatbot
## Setup Evn

1. **Set up the virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

## **Set up the database:**
   - Create a MySQL database named chatbot.
   - Create a table named interactions with the following columns:
       - `id` (INT, AUTO_INCREMENT, PRIMARY KEY)
       - `user_input` (TEXT)
       - `bot_response` (TEXT)
       - `timestamp` (DATETIME)
    
## **Configure the application:**
  - Update the database connection settings in `chat.py` if necessary.

## **Run the chatbot:**
    ```bash
    python train.py
    python chat.py
## **How It Works:**
  - **Training**: The `train.py` script trains the neural network model using the dataset provided in `intent.json`. The trained model is saved as `data_Nego.pth`.
  - **Chat Interface**: The `chat.py` script loads the trained model and provides a Tkinter-based chat interface. User interactions are processed, and responses are generated based on the model’s predictions.
  - **Database Logging**: Conversations between users and the chatbot are logged into the MySQL database for record-keeping and analysis.
