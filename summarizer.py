from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY1")

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_summary(transcript):

    prompt = f"""
    You are an expert meeting assistant.

    Analyze the following meeting transcript and provide:

    1. Executive Summary
    2. Key Discussion Points
    3. Decisions Made
    4. Action Items
    5. Next Steps

    Transcript:
    {transcript}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text