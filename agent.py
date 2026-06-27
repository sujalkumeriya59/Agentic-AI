
from agno.agent import Agent
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()  # It stores the GROQ_API_KEY in the environment variables for secure access

from agno.tools.duckduckgo import DuckDuckGoTools  # WebSearch tool

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"), # model=Groq(id="llama-3.3-70b-versatile")
        tools=[DuckDuckGoTools()],
        instructions="You are a helpful & expert level travel assistant.",
        markdown=True,
        add_datetime_to_context=True # For checking the date and time in the context of the conversation
    )

agent = build_agent()
agent.print_response("Is it possible to travel to Pahalgam right now?")
# agent.print_response("What is tomorrow's date?")