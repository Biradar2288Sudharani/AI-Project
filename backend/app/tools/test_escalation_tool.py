from app.tools.escalation_tool import EscalationTool

result = EscalationTool.escalate(
    "Diagnosis Conflict Found"
)

print(result)