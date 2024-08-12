# WebRAG: Your AI-Powered Website Explorer

Dive into the world of website exploration with WebRAG! This project lets you have insightful conversations about any webpage. Simply provide the URL, and our LangChain-powered chatbot will answer your questions based on the website's content, all powered by the cutting-edge Mixtral LLM. No more tedious scrolling – get your information quickly and efficiently!

## Features:

- **Website Question Answering:** Input any URL and ask questions directly related to the webpage content.
- **LangChain Integration:**  Utilizes the LangChain framework for seamless integration with LLMs and other components. 
- **Chroma Vector Database:** Employs Chroma for efficient storage and retrieval of webpage content embeddings. 
- **Google Generative AI Embeddings:** Uses Google's powerful embedding model for high-quality text representation. 
- **Groq Integration:** Leverages the Groq API for enhanced semantic search and information retrieval from web content.
- **Mixtral LLM:**  Powered by the advanced Mixtral-8x7b-32768 Large Language Model for comprehensive and context-aware responses.
- **User-Friendly Interface:** A simple and intuitive Gradio-based chat interface makes interacting with the chatbot effortless. 

## Requirements:

- Python 3.7+
- Required Python packages (install via `pip install -r requirements.txt`)
- A Groq account and API key ( [https://groq.com/](https://groq.com/))

## How to Run:

1. Clone the repository: `git clone https://github.com/corazon71/WebRAG.git`
2. Navigate to the project directory: `cd WebRAG`
3. Install the dependencies: `pip install -r requirements.txt`
4. Set up your `.env` file (see below)
5. Run the application: `main.py`

## .env File Configuration

Edit `.env` file in the root directory and add the following with your actual Google Cloud credentials:
**Configure Credentials:**
- Open the `.env` file and update the `GOOGLE_APPLICATION_CREDENTIALS` value with the path to your downloaded Google Cloud service account credentials JSON file. 
- Also set up the `GROQ_API_KEY` value with your Groq API key.
## Usage:

1. Run the application and access the Gradio interface in your web browser.
2. Paste the URL of the webpage you want to explore in the "Enter the URL of the Webpage" textbox. 
3. Type your questions about the webpage in the chat interface and press enter.
4. The chatbot will analyze the webpage content and provide you with an accurate answer.

## Example:

**URL:** https://onepiece.fandom.com/wiki/One_Piece_Wiki

**Question:** What is the name of the latest chapter?

**Answer:** The latest One Piece manga chapter 1122 is titled "Time is Right".