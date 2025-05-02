import os
from dotenv import load_dotenv
from grant_automation.crew import GrantAutomation  # <- This line is the fix

load_dotenv()

def run():
    result = GrantAutomation().crew().kickoff()
    print("Crew finished!")
    print(result)

if __name__ == "__main__":
    run()
