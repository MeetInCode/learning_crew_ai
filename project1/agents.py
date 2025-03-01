from crewai import Agent
from crewai import LLM
from tools import yt_tool
from dotenv import load_dotenv

load_dotenv()

import os

my_llm = LLM(
              model='gemini/gemini-1.5-flash',
              temperature=0.7,
              verbose=True,
              api_key=os.environ["GEMINI_API_KEY"]
            )



## Create a senior blog content researcher

blog_content_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verbose=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm=my_llm
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm=my_llm
)