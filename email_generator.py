from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY2")

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_email(transcript):

    prompt = f"""
    You are a professional executive assistant.

    Analyze the meeting transcript and generate a professional business email.

    Requirements:

    1. Create a professional subject line.
    2. Write a concise meeting summary.
    3. Highlight key discussion points.
    4. Highlight decisions made.
    5. List action items.
    6. Extract all important dates, deadlines, milestones, and upcoming meetings.
    7. Create a separate section:
       IMPORTANT DATES & DEADLINES
    8. If no dates are found, write:
       "No specific dates or deadlines were mentioned."
    9. Use a professional corporate tone.
    10. Format the email clearly using headings and bullet points.

    Transcript:
    {transcript}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text