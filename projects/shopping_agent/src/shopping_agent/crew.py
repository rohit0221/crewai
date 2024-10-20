from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool  # Using SerperDevTool as the internet search tool

@CrewBase
class ShoppingCrew():
    """ShoppingCrew crew"""

    @agent
    def shopping_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['shopping_agent'],
            tools=[SerperDevTool()],  # Assigning an internet search tool
            verbose=True
        )

    @task
    def price_check_task(self) -> Task:
        return Task(
            config=self.tasks_config['price_check_task'],
            output_file='deals_summary.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ShoppingCrew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,  # Executes tasks sequentially
            verbose=True
        )
