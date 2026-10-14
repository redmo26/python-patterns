# Ask an AI a question from Python. The key lives in .env, never in the code.
# GOTCHAS: 503 = Google is busy (wait, or try another model), 404 = model name
# retired (use a "-latest" name), 400 = bad key.
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=input("talk to this ai: "),
)
print(response.text)



