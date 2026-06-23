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

   1. Generate a clear and professional subject line.
    2. Keep the email short and focused (150-250 words maximum).
    3. Summarize only the most important discussion points.
    4. Include key decisions and critical action items naturally within the email body.
    5. Mention important dates, deadlines, and upcoming milestones only if they were discussed.
    6. Do NOT use bullet points, numbered lists, tables, or headings.
    7. Write in a formal corporate tone suitable for managers, clients, and team members.
    8. Use clear paragraphs and natural business language.
    9. Avoid repeating information.
    10. End the email with:

    Best regards,

    AI Meeting Assistant

    11. Never use placeholders such as:
        [Your Name]
        [Executive Assistant]
        [Sender Name]

    12. Always sign the email as:

    Best regards,

    AI Meeting Assistant

    The email should read like a real business follow-up email sent after a meeting.

    Transcript:
    {transcript}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text