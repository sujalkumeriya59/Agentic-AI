from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv
load_dotenv()  


def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"), # model=Groq(id="llama-3.3-70b-versatile")
        tools=[YFinanceTools(), DuckDuckGoTools()],
        markdown=True,
        add_datetime_to_context=True, # For checking the date and time in the context of the conversation
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use given tools whenever possible. Format your response using markdown and use tables to display data where possible."],
        debug_mode=True
    )

agent = build_agent()
agent.print_response("Share the NVDA stock price and analyst recommendations", markdown=True)
agent.print_response("Share the MSFT stock price in INR and show the current exchange rate", markdown=True)


