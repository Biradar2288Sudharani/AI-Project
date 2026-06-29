from fastapi import APIRouter

from app.agents.discharge_agent import DischargeAgent

router = APIRouter()

@router.post("/generate-summary")
async def generate_summary():

    agent = DischargeAgent()

    result = agent.run(
        "uploads/patient_1.pdf"
    )

    return result