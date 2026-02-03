import os
import cohere
from dotenv import load_dotenv
load_dotenv()



API_KEY = os.getenv("COHERE_API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in environment variables")
co = cohere.Client(API_KEY)



def llm_generate(prompt: str, temperature: float = 0.3) -> str:
    response = co.chat(
        model="command-r7b-12-2024",
        message=prompt,
        temperature=temperature,
    )
    return response.text

# res = llm_generate("write a nice paragraph about running a sneaky sales business")
res = llm_generate("Analyze the market for wireless earbuds in France")
res
