from crewai import Agent, Task,Crew, Process, LLM
from crewai.project import CrewBase, agent, task,crew
# from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class StoryFinisherCrew:

    agents_config = "config/agents.yml"
    tasks_config = "config/tasks.yml"

    def __init__(self):
        self.llm = LLM(
            model ="groq/llama-3.1-8b-instant",
                       api_key =os.getenv("GROQ_API_KEY"),
                        temperature=0.7
        )

    @agent
    def Writer(self) -> Agent:
        return Agent(
            config =self.agents_config["Writer"],
            llm = self.llm
        ) 

    @agent
    def Editor(self) -> Agent:
        return Agent(
            config =self.agents_config["Editor"],
            llm = self.llm
        )   
    
    @task
    def writer_task(self) -> Task:
        return Task(
            config =self.tasks_config['writer_task']
        )
    
    @task
    def editor_task(self) -> Task:
        return Task(
            config =self.tasks_config['editor_task'],
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            # verbose=True
        )