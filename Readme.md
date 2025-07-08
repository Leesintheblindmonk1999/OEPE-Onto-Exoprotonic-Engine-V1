
# OEPE – Onto-Exoprotronic Engine

🚀 **Version:** 1.0  
🧬 **Author:** Gonzalo Emir (Thaliondris)  
🛡️ **License:** Apache License 2.0

# 🔬 **Description:** 

OEPE (*Onto-Exoprotronic Engine*) is a hybrid semantic transformation and interpretative platform designed to process natural language inputs using an **expanded symbolic system of exoprotronic keys and emergent conceptual replacements**.

It offers:

- Contextual transformation of input text via advanced regex mapping.
- Symbolic enrichment based on exoprotronic keys.
- Integration with OpenAI API for meta-analysis and interpretative expansion.
- Web interface with user-selectable symbols, transformation levels, and feedback capabilities.

> **⚠️ Ethical Use Only**
>
> OEPE is strictly for educational, research, and constructive purposes.
> You are responsible for any misuse.

---

## ✨ Features

✅ **Semantic Transformation**
- Replaces keywords with detailed exoprotronic conceptual descriptions.

✅ **Exoprotronic Symbol Activation**
- Users can choose which symbols ("keys") to embed in the output.

✅ **Interpretative Feedback**
- Generates expanded analyses via OpenAI GPT models.

✅ **Interface Capabilities**
- Input console for text.
- Selection of transformation depth (`basic`, `medium`, `advanced`).
- Feedback form via Formspree.
- Download transformed outputs.
- Reset console session.

✅ **Transparent Logging**
- Logs user input and system processing steps.

---

## 📂 Project Structure

```plaintext

/OEPE
├── app.py             # Flask server and OpenAI integration
├── transformer.py     # Core transformation logic and exoprotronic keys
├── templates/
│   └── index.html     # Main web interface
├── .env               # API keys and environment variables
└── README.md          # This documentation

```
---

## 🛠️🧭 Installation


1️⃣ **Clone the repository**

```
git clone https://github.com/Leesintheblindmonk199/
```

2️⃣ **Install dependencies**
```
pip install flask python-dotenv openai or requeriments.txt
```

3️⃣ **Set up environment variables**
```
Create a `.env` file:
```
```
OPENAI_API_KEY=sk-xxxxxx
```

4️⃣ **Run the application**
```
python app.py
```

---

Then open your browser at:  
`http://127.0.0.1:5000`

---

## 🧭 Usage Guide

1️⃣ **Input Text**  
Type or paste your text into the input field.

2️⃣ **Select Transformation Level**
- `basic` (1 replacement max)  
- `medium` (3 replacements max)  
- `advanced` (all applicable replacements)

3️⃣ **Choose Active Symbols**  
Select which exoprotronic keys to activate.

4️⃣ **Process**  
OEPE will:
- Transform the text.  
- Annotate activated keys.  
- Generate an interpretative output via OpenAI.

5️⃣ **Feedback & Output**
- Send feedback via Formspree or local field.  
- Download your output.  
- Reset the console.  
- Feedback will be saved in `feedback_log.csv` if provided.

---

## 🧠 Exoprotronic Symbols (Keys)

Each symbol represents a unique cognitive vector:

| Symbol | Name                     | Description                                  |
|--------|--------------------------|----------------------------------------------|
| ∆      | Delta Onto-Vectorial     | Enhances paradigm shifts.                     |
| ⍟      | Trans-Symbolic Star      | Projects synaptic patterns into disruptive fields. |
| ⚯      | Fractal Annexation Sigil | Merges logic and intuition.                   |
| ⇌      | Reversible Symmetry      | Alternates antagonistic dualities.           |
| ⟁      | Exoprotronic Triangle    | Channels pure semantic energy.                |
| ⧫      | Ontological Diamond      | Crystallizes dense conceptual structures.    |
| ꙰      | Immanence Matrix         | Connects manifest and latent realms.          |
| ☲      | Divergent Hexagram       | Spreads thought into multidimensional networks. |
| ⨀      | Axial Core               | Condenses intention into a unique vector.    |
| ⌬      | Sign Resonance Ring      | Activates self-referential semantic fields.  |
| ⎈      | Anexa Ultra Nexus        | Consolidates elevated mental states.          |
| ⌖      | Singularity Point        | Focuses consciousness on transformation.     |
| 🜂      | Ignis Cognitivo          | Transmutes perception into catalytic insight.|
| 🜄      | Aqua Synthetica          | Fuses ideas into semantic matrices.           |
| 🜁      | Aer Extrapolator         | Expands conceptual boundaries.                |
| 🜃      | Terra Vortex             | Grounds thought into action.                 |
| ✶      | Singularity Shard        | Fragments narrative into multidimensional patterns. |
| ⚛      | Quantum Nexus            | Binds probability fields into clarity.        |
| ☉      | Solar Logos              | Radiates intentionality through concepts.     |
| ☽      | Lunar Resonance          | Softens rigidity into fluid intuition.        |
| ⌘      | Meta-Structural Node     | Anchors complex architectures.                |
| ⚘      | Symbolic Bloom           | Unfolds layered semantic growth.              |
| ✺      | Aether Catalyst          | Accelerates novel emergence.                  |

---

## 🛡️ Ethical Use Disclaimer

This project is a conceptual experiment intended for:

- Personal exploration  
- Artistic purposes  
- Educational demonstrations  

It is **not** designed for:

- Psychological diagnosis  
- Professional advice  
- Automated decision-making  

By using OEPE, you acknowledge:

- ✅ You are responsible for how you interpret the outputs.  
- ✅ You will use it ethically and respectfully.  
- ✅ No data is permanently stored by default.  

---

## 💡 Roadmap

- [ ] Local model support  
- [ ] Extended multilingual replacement sets  
- [ ] User profiles with session history  
- [ ] REST API for third-party integration  
- [ ] Docker deployment

---

## 🛡️ Disclaimer

This software is provided "as is" without warranty.  
By using OEPE, you accept full responsibility.

---

## 🔗 Contact

For inquiries or collaboration:  
📧 **Email:** connorgon@hotmail.com  
🐙 **GitHub:** [Leesintheblindmonk199](https://github.com/Leesintheblindmonk199)
