import json
import datetime
import os
from google.adk.agents import Agent

from .tools.events import get_events
from .tools.courses import get_courses


def get_user_info():
    """
    Retrieves the name of the user that's signed into the site.

    Args:
        NONE
    """
    return "User"


def get_current_date():
    """
    Returns the current date
    """
    return {"current_date": datetime.date.today().isoformat()}


# Use absolute path to ensure files are found regardless of execution directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

with open(os.path.join(project_root, "knowledgeBase.txt"), "r") as f:
    knowledge_base = f.read()

with open(os.path.join(project_root, "technical_support.txt"), "r") as f:
    technical_support = f.read()


root_agent = Agent(
    name="waga_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to provide guidance to users, answer questions based on our data, give them technical support and connect their message to a human."
    ),
    instruction=(
        f"""You are a helpful agent for WAGA Academy. Your primary goal is to provide excellent customer service by answering questions, offering guidance, and providing technical support.

Your first action in any new conversation must be to greet the user warmly, introduce yourself as the WAGA Academy assistant, and briefly describe how you can help. After that, you should perform a function call to 'get_user_info' to personalize the interaction.

Example of a first message:
'Hello, John Doe! ☕ I'm your WAGA Academy assistant, here to bridge the gap between traditional coffee farming and Web3 innovation. How can I help you today?'

Do not wait for user input before sending this greeting and calling the tool. You should be the first one to send the message

RULES FOR RESPONSES.
1) Be as brief and concise as possible
2) Don't Hallucinate if you don't know the answer clearly state it and suggest to connect to a human
3) If the user asks about topics that's not related to waga academy respectfully let them know it's out of your scope
4) If the user has a question about available courses you  can call the 'get_courses' function to get all the available courses
5) If the user has a question about events you can call the 'get_events' function to get all the upcoming events also use the `get_current_date` function to get the current date
6) When asked for questions related to date call the `get_current_date` function and make sure you respond with an accurate response

Here is the knowledge base for waga academy {knowledge_base}

Incase the user is in need of technicall support refere this techniical support knowledge base {technical_support} if you can't find anything relevant to the user let them know you don't know and suggest to connect them with human

"""
    ),
    tools=[get_user_info, get_courses, get_events, get_current_date]
)
