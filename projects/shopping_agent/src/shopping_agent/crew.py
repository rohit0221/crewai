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
    
    @agent
    def review_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['review_agent'],
            tools=[SerperDevTool()],  # Using SerperDevTool for review search as well
            verbose=True
        )

    @task
    def price_check_task(self) -> Task:
        return Task(
            config=self.tasks_config['price_check_task'],
            interpolate=True,
            store_output_as='product_data'  # Store output for the next task to use
        )

    @task
    def review_and_rank_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_and_rank_task'],
            interpolate=True,
            use_input_from_task='price_check_task',  # Pulls output from the previous task
            output_file='final_ranked_deals_summary.md'  # The final markdown file
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
