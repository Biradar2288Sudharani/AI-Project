from app.tools.drug_interaction_tool import DrugInteractionTool

meds = [
    "Warfarin",
    "Aspirin"
]

result = DrugInteractionTool.check(meds)

print(result)