
# Groq Chatbot

This project is a Gradio chatbot powered by Groq.

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate it:
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project folder with your Groq key:
```env
API_key=your_groq_api_key_here
```

You can also set it in the terminal if needed:
```bash
export API_key="your_groq_api_key_here"
```

On Windows PowerShell:
```powershell
$env:API_key = "your_groq_api_key_here"
```

5. Run the app:
```bash
python app.py
```

## What this app does

- Uses Gradio to create a chat interface
- Sends the user message and conversation history to Groq
- Uses a custom system prompt for the New Leap Labs / BeliefSat-0 context
- Returns the model response back in the browser

## Deploy on Hugging Face Spaces

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click Create new Space
3. Create the Space
4. Upload `app.py` and `requirements.txt`
5. Go to Settings → Secrets
6. Add a new secret:
   - Name: `API_key`
   - Value: your Groq key
7. Launch the Space

This project is set up to read the variable named `API_key` from a local `.env` file or platform secrets.
# chatbot
