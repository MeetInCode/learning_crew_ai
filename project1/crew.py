from crewai import Crew,Process
from tasks import research_task, writing_task
from agents import blog_content_researcher, blog_writer

crew = Crew(
    agents=[blog_content_researcher, blog_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=True,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result=crew.kickoff(inputs={'topic':'AI VS ML VS DL vs Data Science'})
print(result)


