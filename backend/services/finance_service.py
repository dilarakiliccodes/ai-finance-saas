from openai import OpenAI

from backend.core.config import settings
from backend.schemas.finance import FinanceRequest, FinanceResponse


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def analyze_finance(data: FinanceRequest):
    prompt = f"""
    You are an AI finance assistant.

    Analyze this user's monthly finance situation:
    Income: {data.income}
    Expense: {data.expense}

    Give a short, helpful, professional financial analysis in Turkish.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return FinanceResponse(
        analysis=response.choices[0].message.content
    )