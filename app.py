from flask import Flask, render_template, request
from transformer import transform, keys
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging
from bs4 import BeautifulSoup  

load_dotenv()
logging.basicConfig(level=logging.INFO)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = Flask(__name__)

def generate_session_text(user_input, transformed, symbols, output):
    parts = []
    if user_input:
        parts.append(f"Original Text:\n{user_input}\n")
    if transformed:
        parts.append(f"Transformation:\n{transformed}\n")
    if symbols and symbols != "None":
        clean_symbols = BeautifulSoup(symbols, "html.parser").get_text()
        parts.append(f"Activated Symbols:\n{clean_symbols}\n")
    if output:
        parts.append(f"Engine Response:\n{output}\n")
    return "\n".join(parts)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    transformed = ""
    symbols = ""
    user_input = ""
    level = "medium"
    api_choice = "openai"
    session_text = ""

    if request.method == "POST":
        user_input = request.form.get("input_text", "").strip()
        level = request.form.get("level", "medium")
        api_choice = request.form.get("api_choice", "openai")
        active_keys = request.form.getlist("active_keys") or None

        if not user_input:
            output = "Please enter a text to transform."
        else:
            logging.info(f"User input: {user_input}")

            try:
                transformed, symbols = transform(user_input, level, active_keys)
            except Exception as e:
                transformed = ""
                symbols = "None"
                output = f"Error during transformation: {e}"
                return render_template(
                    "index.html",
                    output=output,
                    transformed=transformed,
                    symbols=symbols,
                    user_input=user_input,
                    level=level,
                    api_choice=api_choice,
                    keys=keys,
                    session_text=""
                )

            if api_choice == "openai":
                prompt = (
                    f"[Activated symbols: {symbols}]\n{transformed}\n\n"
                    "Interpret and expand this concept within an onto-exoprotronic framework."
                )
                try:
                    completion = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are a symbolic analyst."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    output = completion.choices[0].message.content
                except Exception as e:
                    output = f"Error processing with OpenAI: {e}"
            else:
                output = "Currently, only OpenAI processing is available. Local models coming soon."

        session_text = generate_session_text(user_input, transformed, symbols, output)

    return render_template(
        "index.html",
        output=output,
        transformed=transformed,
        symbols=symbols,
        user_input=user_input,
        level=level,
        api_choice=api_choice,
        keys=keys,
        session_text=session_text
    )

if __name__ == "__main__":
    app.run(debug=True)
