import os
from crewai import Crew
from agent import researcher, writer
from tasks import research, write


# Assemble a crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    verbose=2
)

# Execute tasks
crew.kickoff()