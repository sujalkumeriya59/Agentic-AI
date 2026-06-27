from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import  pprint

load_dotenv()  # It stores the GROQ_API_KEY in the environment variables for secure access

db=SqliteDb(db_file="agno.db")
db.clear_memories()  # Clear the memory of the agent to start fresh


def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"), # model=Groq(id="llama-3.3-70b-versatile")
        db=db,
        markdown=True,
        add_history_to_context=True,
        # enable_user_memory=True, # Enable user memory to store and retrieve user-specific information

     )

user_id = "rahul@gmail.com"
agent = build_agent()
# agent.print_response("What is the Capital of USA?",user_id=user_id)
# agent.print_response("what is the best time to visit it?",user_id=user_id)


agent.print_response("I am Rahul. I am a Data Analyst.",user_id=user_id)
agent.print_response("who am I?",user_id=user_id)

print("MEMORIES")
pprint(memories:=db.get_memories(user_id=user_id))

# agent.print_response("My favourate color is Red.")
# agent.print_response("Suggest me some names of my favourate color car ")