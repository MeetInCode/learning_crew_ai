from crewai import Task
from tools import yt_tool
from agents import blog_content_researcher, blog_writer

##research task
research_task = Task(
    description=(
        "Identify the most relevant youtube videos for the topic {topic}. "
        "find the most relevant videos from the youtube channel. "
        "get detailed information about the video from the youtube channel"
    ),
    expected_output="A comprehensive 3 paragraph long report about the video {topic}",
    tools=[yt_tool],  
    agent=blog_content_researcher
)

##writing task
writing_task = Task(
    description=(
        "Write a compelling blog post about the video {topic} from the youtube channel"
    ),
    expected_output="A detailed blog post about the video {topic}",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="blog_post.md"
)







