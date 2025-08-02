# 🩺 Medical Symptom Checker (AI Agent)

This is an AI-powered command-line tool that helps users reflect on their symptoms. It analyzes user input using Google’s Gemini model and provides:

- Probable cause of the symptoms  
- Estimated severity (mild/moderate/severe)  
- Advice on whether to consult a doctor  
- Log summary saved to file via tool integration  

---

## 🚀 Features

- 🧠 Built using LangChain + Gemini (Google Generative AI)  
- ✅ Uses Pydantic for structured JSON output  
- 🛠️ Tool integration to log symptom summaries  
- 🧾 Format enforced using dynamic JSON schema  
- 💬 Chat-like experience in terminal  

---

## 📂 Project Structure

```bash
symptom-checker-agent/
├── main.py              # Main CLI application
├── tools.py             # Tool definition for logging
├── schema.py            # Pydantic schema for output
├── requirement.txt      # All required packages
├── .env                 # API key (ignored by Git)
├── logs/                # Directory where logs are saved
└── README.md            # You're here!
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/RoopikaBiju/symptom-checker-agent.git
cd symptom-checker-agent
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

### 4. Add your API key (Gemini)

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 🏃 Run the app

```bash
python main.py
```

Then type symptoms like:

```text
I have a headache and nausea for 2 days
```

To exit:

```bash
exit
```

---

### 📦 Dependencies

```text
langchain
langchain-google-genai
pydantic
python-dotenv
```

Install them with:

```bash
pip install -r requirement.txt
```

### 📜 Sample Log Output

Logs are saved in the logs/ folder in this format:

```text
[2025-08-02 20:44:12]
User reported: nausea and stomach cramps after eating
Probable cause: Food poisoning
Severity: Moderate
Advice: Rest, hydrate, eat bland food. Consult a doctor if persists.
```
---

## 🛡 Disclaimer

This tool does not provide medical diagnoses. It is a reflective aid only. Always consult a licensed doctor for serious or unclear symptoms.