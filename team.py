from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team
load_dotenv()  # It stores the GROQ_API_KEY in the environment variables for secure access

eng_agent = Agent(name="English Agent", role="You answer questions in English")
chin_agent = Agent(name="Chinese Agent", role="You answer questions in Chinese")
hin_agent = Agent(name="Hindi Agent", role="You answer questions in Hindi")

team = Team(
    name = "Answer & Translation Team",
    members = [eng_agent, chin_agent, hin_agent],
    model= Groq(id="qwen/qwen3-32b"),
    markdown = True,
    instructions = """ All members respond to the query in their Specific language. 
                       Do not call just one agent.
                       Output the response of All agents. """

    
)

team.print_response("What is the Capital of India?")
