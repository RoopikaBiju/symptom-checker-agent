from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage
from tools import tools
from schema import SymptomResponse
import os
from pydantic import TypeAdapter
import json

raw_schema = json.dumps(TypeAdapter(SymptomResponse).json_schema(), indent=2)
escaped_schema = raw_schema.replace("{", "{{").replace("}", "}}")


SYSTEM_PROMPT = f"""
You are a helpful medical assistant. You do NOT give diagnoses.
You help users reflect on their symptoms and suggest:
1. Probable cause
2. Severity (mild/moderate/severe)
3. Whether to visit a doctor
4. You must call log_symptom_entry to save the summary

NEVER guess critical conditions. BE cautious and refer to doctors when unclear.
Format your log entry for log_symptom_entry like this:
User reported: <symptoms>
Probable cause: <cause>
Severity: <level>
Advice: <what to do>

Output ONLY valid JSON in this format:
{escaped_schema}
"""




llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    max_output_tokens=1000,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

parser=PydanticOutputParser(pydantic_object=SymptomResponse)

prompt=ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder","{chat_history}"),
    ("human", "{query}"),
    ("placeholder","{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

agent=create_tool_calling_agent(llm=llm,tools=tools,prompt=prompt)
executor=AgentExecutor(agent=agent, tools=tools, verbose=True)

chat_history = []
print("🤖 Medical Symptom Checker (type 'exit' to quit)\n")

while True:
    query= input("You: ")
    if query.lower() == 'exit':
        print("Session Ended.Take care!")
        break

    chat_history.append(HumanMessage(content=query))
    result= executor.invoke({"query": query, "chat_history": chat_history})

    try:
        response= parser.parse(result['output'])
        print(f"\n🩺Possible Cause: {response.probable_cause}")
        print(f"🚦Severity: {response.severity}")
        print(f"💭Advice: {response.advice}")
        print(f"📜Log: {response.log_status}")
        chat_history.append(AIMessage(content=response.probable_cause))

    except Exception as e:
        print(f"❗Error: {e}")
        print("Raw output:\n", result['output'])
