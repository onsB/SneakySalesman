from src.llm import llm_generate
from src.schemas import FinalReport


def generate_report(product: str, data: dict) -> FinalReport:
    prompt = f"""
    You are a market analyst.

    Product: {product}
    Data: {data}

    Generate:
    - Executive summary
    - 3 business recommendations
    """

    text = llm_generate(prompt)

    return FinalReport(
        summary=text,
        insights=data,
        recommendations=[
            "Maintain premium pricing",
            "Emphasize battery life in marketing",
            "Monitor competitor discounts",
        ],
    )
