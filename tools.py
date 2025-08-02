import os
from datetime import datetime
from langchain.tools import Tool

def log_symptom_entry(entry:str):
    os.makedirs('logs', exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename=f"logs/symptoms_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.txt"
    with open(filename,"a",encoding="utf-8") as f:
        f.write(f"[{timestamp}]{entry}\n")
    return f"Symptom logged at {timestamp}"

tools=[
    Tool(
        name="log_symptom_entry",
        func=log_symptom_entry,
        description="Logs a symptom entry with a timestamp and summary to a file."
    )
]