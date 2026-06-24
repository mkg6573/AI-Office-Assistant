import streamlit as st
from transcription import transcribe_audio
from summarizer import generate_summary
from email_generator import generate_email
from email_sender import send_email
from qa import answer_question

st.set_page_config(
    page_title="Smart Office Assistant",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Meeting Assistant")

audio_file = st.file_uploader(
    "Upload Meeting Audio",
    type=["mp3", "wav", "m4a"]
)

if audio_file:

    st.audio(audio_file)

    # ==========================
    # Process Meeting
    # ==========================
    if st.button("🚀 Process Meeting"):

        try:

            with st.spinner("🎤 Transcribing Audio..."):

                transcript = transcribe_audio(audio_file)

            st.session_state["transcript"] = transcript

            with st.spinner("📋 Generating Summary..."):

                summary = generate_summary(transcript)

            st.session_state["summary"] = summary

            with st.spinner("📧 Generating Professional Email..."):

                email = generate_email(transcript)

            st.session_state["email"] = email

            st.success(
                "✅ Transcript, Summary and Email Generated Successfully!"
            )

        except Exception as e:

            st.error(
                f"❌ Error: {e}"
            )

    # ==========================
    # Show Transcript
    # ==========================
    if "transcript" in st.session_state:

        st.subheader("📝 Transcript")

        st.text_area(
            "Transcript",
            st.session_state["transcript"],
            height=300
        )

        st.download_button(
            "📥 Download Transcript",
            st.session_state["transcript"],
            file_name="meeting_transcript.txt",
            mime="text/plain"
        )

    # ==========================
    # Show Summary
    # ==========================
    if "summary" in st.session_state:

        st.subheader("📋 Meeting Summary")

        st.markdown(
            st.session_state["summary"]
        )

        st.download_button(
            "📥 Download Summary",
            st.session_state["summary"],
            file_name="meeting_summary.txt",
            mime="text/plain"
        )

    # ==========================
    # Show Email
    # ==========================
    if "email" in st.session_state:

        st.subheader("📨 Professional Email")

        st.text_area(
            "Generated Email",
            st.session_state["email"],
            height=400
        )

        st.download_button(
            "📥 Download Email",
            st.session_state["email"],
            file_name="professional_meeting_email.txt",
            mime="text/plain"
        )

        # ==========================
        # Send Email
        # ==========================
        st.subheader("🚀 Send Email To Team")

        team_emails = st.text_area(
            "Enter Team Member Emails (comma separated)",
            placeholder="mohit@gmail.com, rahul@gmail.com, aman@gmail.com"
        )

        if st.button("📨 Send Email"):

            if team_emails.strip():

                recipients = [
                    email.strip()
                    for email in team_emails.split(",")
                    if email.strip()
                ]

                try:

                    send_email(
                        recipients=recipients,
                        subject="Meeting Follow-up & Action Items",
                        body=st.session_state["email"]
                    )

                    st.success(
                        f"✅ Email sent successfully to {len(recipients)} recipient(s)"
                    )

                except Exception as e:

                    st.error(
                        f"❌ Failed to send email: {e}"
                    )

            else:

                st.warning(
                    "⚠️ Please enter at least one email address."
                )

# ==========================================
# SIDEBAR AI CHATBOT
# ==========================================
with st.sidebar:

    st.header("💬 AI Meeting Assistant")

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    question = st.text_input(
        "Ask about the meeting",
        placeholder="What decisions were made?"
    )

    if st.button("🤖 Ask AI"):

        if "transcript" not in st.session_state:

            st.warning(
                "Please generate the transcript first."
            )

        elif question.strip():

            with st.spinner("Thinking..."):

                answer = answer_question(
                    st.session_state["transcript"],
                    question
                )

            st.session_state["chat_history"].append(
                {
                    "question": question,
                    "answer": answer
                }
            )

    st.divider()

    st.subheader("🗨️ Conversation")

    if st.session_state["chat_history"]:

        for chat in reversed(
            st.session_state["chat_history"]
        ):

            st.markdown(
                f"**🙋 You:** {chat['question']}"
            )

            st.markdown(
                f"**🤖 AI:** {chat['answer']}"
            )

            st.divider()