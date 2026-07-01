from pydantic import BaseModel

class FinanceRequest(BaseModel):
    income: float
    expense: float


class FinanceResponse(BaseModel):
    analysis: str