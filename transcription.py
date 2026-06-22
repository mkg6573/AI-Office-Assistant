from google import genai
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def transcribe_audio(uploaded_audio):

    # Save uploaded audio temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=os.path.splitext(uploaded_audio.name)[1]
    ) as tmp_file:

        tmp_file.write(uploaded_audio.getvalue())
        temp_path = tmp_file.name

    # Upload file to Gemini
    uploaded_file = client.files.upload(
        file=temp_path
    )

    prompt = """
    Transcribe this meeting audio.

    Instructions:
    - Detect different speakers whenever possible.
    - Label them as Speaker 1, Speaker 2, Speaker 3.
    - Start a new paragraph when the speaker changes.
    - Correct grammar.
    - Remove filler words.
    - Return only the transcript.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded_file,
            prompt
        ]
    )

    return response.text