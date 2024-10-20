#!/usr/bin/env python
import sys
from shopping_agent.crew import ShoppingCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'article_name': 'Wireless Headphones',
        'price_range': '50-150',
        'preferences': 'brand:Sony, color:black, fast delivery'
    }
    ShoppingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'article_name': 'Wireless Headphones',
        'price_range': '50-150',
        'preferences': 'brand:Sony, color:black, fast delivery'
    }
    try:
        ShoppingCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ShoppingAgentCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'article_name': 'Wireless Headphones',
        'price_range': '50-150',
        'preferences': 'brand:Sony, color:black, fast delivery'
    }
    try:
        ShoppingAgentCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
