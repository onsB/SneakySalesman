from src.llm import llm_generate
from src.schemas import SentimentResult, TrendResult, ProductInfo


def generate_report(product: str, location:str, sentiment: SentimentResult, trend: TrendResult, product_info: ProductInfo) -> str:

    prompt = f"""
    You are a market analyst. generate a final report about a product based on the data provided.

    Product: {product}
    Data is in the following fields:

    Consumer Sentiment: {sentiment}
    Product trend: {trend}
    Product info: {product_info}
    location: {location}

    If one or many of these fields values are vague, do not use them in the report. 
    For example, if the location is 'global' or 'south'.. do not factor it into the market report

    Generate:
    - Executive summary and insights (3-4 sentences)
    - 3 business recommendations
    """

    text = llm_generate(prompt)

    return text
