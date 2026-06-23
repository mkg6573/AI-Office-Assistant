from google import genai
import os
from dotenv import load_dotenv

# ==========================
# Load Environment Variables
# ==========================
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY3")

client = genai.Client(
    api_key=GEMINI_API_KEY
)

# ==========================
# Question Answering Function
# ==========================
def answer_question(transcript, question):

    prompt = f"""
    You are an intelligent AI Meeting Assistant.

    Your task is to answer questions using ONLY the information
    available in the meeting transcript.

    Rules:
    - Do not make up information.
    - If the answer is not available in the transcript, reply:
      "This information was not discussed in the meeting."
    - Keep answers concise and professional.
    - Use bullet points when appropriate.
    - If asked about action items, provide tasks and owners.
    - If asked about deadlines, provide all mentioned dates.
    - If asked about decisions, summarize decisions clearly.
    - If asked about next steps, summarize next actions.
    - If asked about participants, mention relevant speakers.

    Meeting Transcript:
    --------------------------------
    {transcript}
    --------------------------------

    User Question:
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

        return f"Error: {str(e)}"