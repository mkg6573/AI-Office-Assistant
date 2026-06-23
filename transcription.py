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

    1. Detect different speakers whenever possible.
    2. Label them as:
    Speaker 1:
    Speaker 2:
    Speaker 3:
    3. Start a new paragraph when the speaker changes.
    4. Correct grammar and punctuation.
    5. Remove filler words such as um, uh, hmm.
    6. Return only the transcript.
    7. Do NOT use Markdown formatting.
    8. Do NOT use asterisks (*), bold text (**), bullet points, or code blocks.
    9. Write speaker labels as plain text exactly like:

    Speaker 1:
    Hello everyone.

    Speaker 2:
    Thank you.

    10. Keep the original meaning of the conversation.

    Transcript:
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded_file,
            prompt
        ]
    )

    return response.text