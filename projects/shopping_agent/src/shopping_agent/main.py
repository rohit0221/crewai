#!/usr/bin/env python
import sys
from shopping_agent.crew import ShoppingCrew

# Global input configuration
INPUTS = {
    'article_name': 'Runner Watch',
    'price_range': 'USD 50-250 ',
    'preferences': 'brand:Garmin, color:black, Speciality: Runners Special, Features:Heart beat and Oxygen tracking, highest discount'
}

def run():
    """
    Run the crew.
    """
    ShoppingCrew().crew().kickoff(inputs=INPUTS)

def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        ShoppingCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=INPUTS
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ShoppingCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    try:
        ShoppingCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs=INPUTS
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
