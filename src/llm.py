import os
import cohere
import json
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("COHERE_API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in environment variables")
co = cohere.ClientV2(API_KEY)


def llm_generate(prompt: str, temperature: float = 0.3) -> str:
    response = co.chat(
        model="command-r7b-12-2024",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.message.content[0].text

def llm_generate_structured(prompt: str, temperature: float = 0.1) -> dict:
    response = co.chat(
        model="command-r7b-12-2024",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=temperature
    )
    # convert the content to a dictionary
    response_dict = json.loads(response.message.content[0].text)
    return response_dict
    