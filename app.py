from flask import Flask, render_template, request
from transformer import transform, keys
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    transformed = ""
    symbols = ""
    user_input = ""
    level = "medium"
    api_choice = "openai"

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
                    keys=keys
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

    return render_template(
        "index.html",
        output=output,
        transformed=transformed,
        symbols=symbols,
        user_input=user_input,
        level=level,
        api_choice=api_choice,
        keys=keys
    )

if __name__ == "__main__":
    app.run(debug=True)
