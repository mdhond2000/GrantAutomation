from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from grant_automation.tools.custom_tool import send_email_tool


@CrewBase
class GrantAutomation():
    """GrantAutomation crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Agents
    @agent
    def grant_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['grant_writer'],  # from agents.yaml
            verbose=True
        )

    @agent
    def grant_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['grant_reviewer'],
            verbose=True
        )

    @agent
    def grants_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['grants_coordinator'],
            verbose=True
        )

    @agent
    def grants_administrator(self) -> Agent:
        return Agent(
            config=self.agents_config['grants_administrator'],
            verbose=True
        )

    # Tasks
    @task
    def find_grants(self) -> Task:
        return Task(
            config=self.tasks_config['find_grants'],
        )

    @task
    def review_grants(self) -> Task:
        return Task(
            config=self.tasks_config['review_grants'],
        )

    @task
    def organize_grants(self) -> Task:
        return Task(
            config=self.tasks_config['organize_grants'],
        )

    @task
    def finalize_and_email(self) -> Task:
        return Task(
        config=self.tasks_config['finalize_and_email'],
        output_file="final_grant_report.md",
        callback=lambda report: send_email_tool(str(report))
    )



    @crew
    def crew(self) -> Crew:
        """Creates the GrantAutomation crew"""
        print("🔎 DEBUG: agents_config =", self.agents_config)
        print("🔎 DEBUG: tasks_config =", self.tasks_config)

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
