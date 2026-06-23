from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY3")

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def answer_question(transcript, question):

    prompt = f"""
You are an AI Meeting Assistant.

Your responsibility is to answer questions using ONLY the meeting transcript provided below.

Guidelines:
- Do not invent information.
- If the answer is not explicitly mentioned in the transcript, reply:
  "This information was not discussed in the meeting."
- Keep answers clear, concise, and professional.
- When appropriate, mention speaker names or speaker labels.
- For action items, include task owner and task details.
- For deadlines, include all relevant dates.
- For decisions, summarize the final decision reached.
- For next steps, summarize upcoming actions.
- Answer naturally as if assisting a meeting participant.

Meeting Transcript:
{transcript}

Question:
{question}

Answer:
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        error_text = str(e)

        if "429" in error_text:
            return "The AI service quota has been exceeded. Please try again later."

        if "503" in error_text:
            return "The AI service is currently busy. Please try again in a few minutes."

        return f"Error: {error_text}"