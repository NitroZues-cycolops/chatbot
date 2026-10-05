import os
import gradio as gr
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def get_groq_api_key():
    for key_name in ("API_KEY", "API_key"):
        value = os.getenv(key_name)
        if value and value.strip():
            return value.strip()
    return None


def chat_fn(message, history):
    api_key = get_groq_api_key()

    if not api_key:
        return "Error: API_KEY is not set. Please create a .env file or configure it in Hugging Face Spaces Settings → Secrets."
    
    if not message or not message.strip():
        return ""
    
    try:
        client = Groq(api_key=api_key)

        messages = [{
            "role": "system",
            "content": "You are the assistant for New Leap Labs, the KJ Somaiya student satellite team " "behind BeliefSat-0, an amateur radio satellite. Answer only about satellites, " "amateur radio and this team. If you don't know, say so."
        }]

        if history:
            for item in history:
                if isinstance(item, dict):
                    role = item.get("role")
                    content = item.get("content")
                    if role and content:
                        messages.append({"role": role, "content": str(content).strip()})
                elif isinstance(item, (list, tuple)) and len(item) == 2:
                    user_msg, assistant_msg = item
                    if user_msg and str(user_msg).strip():
                        messages.append({"role": "user", "content": str(user_msg).strip()})
                    if assistant_msg and str(assistant_msg).strip():
                        messages.append({"role": "assistant", "content": str(assistant_msg).strip()})

        messages.append({"role": "user", "content": str(message).strip()})

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg or "Unauthorized" in error_msg:
            return "Error: Invalid Groq API key. Please check your API_key value in the .env file or in Hugging Face Spaces Settings → Secrets."
        elif "rate limit" in error_msg.lower():
            return "Error: Rate limit exceeded. Please try again in a moment."
        else:
            return f"Error: {error_msg}"


demo = gr.ChatInterface(
    fn=chat_fn,
    title="New Leap Labs Assistant",
    description="Ask about satellites, amateur radio, and the New Leap Labs / BeliefSat-0 team."
)

host = os.getenv("HOST")
port = int(os.getenv("PORT", 7860))

if __name__ == "__main__":
    if host:
        demo.launch(server_name=host, server_port=port)
    else:
        demo.launch(server_port=port)

