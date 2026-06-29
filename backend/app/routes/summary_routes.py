from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.discharge_agent import DischargeAgent

router = APIRouter()


class SummaryRequest(BaseModel):
    file_path: str

@router.post("/generate-summary")
async def generate_summary(data: SummaryRequest):

    print(f"\nROUTE RECEIVED: {data.file_path}")

    agent = DischargeAgent()

    result = agent.run(
        data.file_path
    )

    return result



















































































