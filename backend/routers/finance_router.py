from fastapi import APIRouter

from backend.schemas.finance import (
    FinanceRequest,
    FinanceResponse
)

from backend.services.finance_service import analyze_finance

router = APIRouter(
    prefix="/finance",
    tags=["Finance"]
)


@router.post(
    "/analyze",
    response_model=FinanceResponse
)
def analyze(data: FinanceRequest):
    return analyze_finance(data)