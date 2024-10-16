import os
from crewai import Crew
from agent import researcher, writer
from tasks import research, write

import os
from dotenv import load_dotenv
load_dotenv()

# Assemble a crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    verbose=True
)

# Execute tasks
crew.kickoff()