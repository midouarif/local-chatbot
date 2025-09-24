# DeepSeek Chatbot with Streamlit

This is a local chatbot application built with Streamlit and LangChain, powered by the DeepSeek R1 model running through Ollama.
Unlike cloud-based chatbots, this app runs entirely on your machine, keeping data private and secure.

## Features
- Chat-like interface (similar to ChatGPT)
- Keeps chat history
- Spinner animation while generating responses

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/deepseek-chatbot.git
   cd deepseek-chatbot
2. Create a virtual environment (recommended):
   ```bash
   conda create -n chatbot python=3.10
   conda activate chatbot
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Make sure you have Ollama running locally with the DeepSeek model:
   ```bash
   ollama pull deepseek-r1:1.5b

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
