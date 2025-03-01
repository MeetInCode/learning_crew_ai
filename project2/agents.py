from crewai import Agent,LLM
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool 
import os
load_dotenv()

## call gemini models

my_llm = LLM(
              model='gemini/gemini-1.5-flash',
              temperature=0.7,
              verbose=True,
              api_key=os.environ["GEMINI_API_KEY"]
            )

# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool],
    llm=my_llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=my_llm,
  allow_delegation=False
)
