from src.llm import llm_generate_structured


def parse_request(prompt: str) -> tuple[str, str]:
    parsing_prompt = f"""
    You are a helpful assistant that extracts relevant information from user requests.

    Given the following user request, extract and return only the product name and location (if provided). 
    If no location is specified, return 'global' as the default location.

    User Request: {prompt}

    Generate a JSON with the fields 'product' and 'location'.
    """

    response = llm_generate_structured(parsing_prompt)

    product = response.get("product", "").strip()
    location = response.get("location", "global").strip()
    if not location:
        location = "global"
    return product, location