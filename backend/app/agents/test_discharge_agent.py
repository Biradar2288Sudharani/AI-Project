from app.agents.discharge_agent import (
    DischargeAgent
)

agent = DischargeAgent()

result = agent.run(
    r"uploads/patient 1.pdf"
)

print("\n===== SUMMARY =====\n")

print(
    result["summary"]
)

print("\n===== TRACE =====\n")

for step in result["trace"]:

    print(step)

print("\n===== VALIDATION =====\n")

print(
    result["validation"]
)