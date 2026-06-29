from app.agents.planner_agent import Planner
from app.agents.summary_agent import SummaryGenerator

from app.tools.trace_logger import TraceLogger
from app.tools.escalation_tool import EscalationTool


class DischargeAgent:

    MAX_STEPS = 10

    def __init__(self):

        self.trace = TraceLogger()

        self.plan = Planner().create_plan()

    def run(self, patient_data):

        current_step = 0

        while current_step < self.MAX_STEPS:

            if current_step >= len(self.plan):
                break

            action = self.plan[current_step]

            self.trace.add_step(
                reasoning=f"Executing {action}",
                action=action,
                result="Completed"
            )

            current_step += 1

        summary = SummaryGenerator.generate(
            patient_data
        )

        return {
            "summary": summary,
            "trace": self.trace.get_trace()
        }