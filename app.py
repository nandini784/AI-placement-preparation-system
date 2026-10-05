import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="AI Placement Preparation System",
    page_icon="🎯",
    layout="wide"
)

# -------------------------------------------------
# CSS
# -------------------------------------------------

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #2563eb;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.markdown(
    '<div class="main-title">🎯 AI Placement Preparation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Prepare for placements with AI-powered skill analysis, aptitude practice and interview questions.</div>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# JOB ROLE DATA
# -------------------------------------------------

job_roles = {
    "Python Developer": {
        "skills": [
            "python",
            "oops",
            "sql",
            "git",
            "django",
            "flask",
            "api"
        ],
        "questions": [
            "What are the features of Python?",
            "What is OOP in Python?",
            "What is the difference between list and tuple?",
            "What is a dictionary in Python?",
            "What is an API?"
        ]
    },

    "Data Analyst": {
        "skills": [
            "python",
            "pandas",
            "numpy",
            "sql",
            "excel",
            "statistics",
            "power bi"
        ],
        "questions": [
            "What is data analysis?",
            "What is Pandas?",
            "What is the difference between mean and median?",
            "What is SQL?",
            "What is Power BI used for?"
        ]
    },

    "Machine Learning Engineer": {
        "skills": [
            "python",
            "numpy",
            "pandas",
            "scikit-learn",
            "machine learning",
            "statistics",
            "matplotlib"
        ],
        "questions": [
            "What is machine learning?",
            "What is supervised learning?",
            "What is unsupervised learning?",
            "What is overfitting?",
            "What is train-test splitting?"
        ]
    },

    "Web Developer": {
        "skills": [
            "html",
            "css",
            "javascript",
            "python",
            "sql",
            "git",
            "react"
        ],
        "questions": [
            "What is HTML?",
            "What is CSS?",
            "What is JavaScript?",
            "What is responsive web design?",
            "What is React?"
        ]
    }
}

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("⚙️ Placement Settings")

name = st.sidebar.text_input(
    "Enter your name"
)

selected_role = st.sidebar.selectbox(
    "Select your target job role",
    list(job_roles.keys())
)

# -------------------------------------------------
# TABS
# -------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Skill Analysis",
        "📝 Aptitude Test",
        "🤖 Interview Practice",
        "🎯 Preparation Plan"
    ]
)

# =================================================
# TAB 1 - SKILL ANALYSIS
# =================================================

with tab1:

    st.header("📊 Skill Match Analysis")

    st.write(
        "Enter the skills you currently have. "
        "Example: Python, SQL, Pandas, Git"
    )

    user_skills = st.text_area(
        "Your Skills",
        placeholder="Python, SQL, Pandas, Git, HTML..."
    )

    if st.button("🔍 Analyze My Skills"):

        if user_skills.strip() == "":
            st.warning("Please enter your skills.")

        else:

            required_skills = job_roles[selected_role]["skills"]

            user_text = user_skills.lower()

            matched = []
            missing = []

            for skill in required_skills:

                if skill.lower() in user_text:
                    matched.append(skill)
                else:
                    missing.append(skill)

            total = len(required_skills)

            score = (len(matched) / total) * 100

            st.subheader("🎯 Placement Skill Score")

            st.progress(int(score))

            st.metric(
                "Skill Match",
                f"{score:.1f}%"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.success("✅ Skills You Have")

                for skill in matched:
                    st.write("✔️", skill)

            with col2:

                st.error("❌ Skills You Need")

                for skill in missing:
                    st.write("•", skill)

            if score >= 80:
                st.success(
                    "Excellent! You have a strong skill match for this role."
                )

            elif score >= 50:
                st.info(
                    "Good start! Improve the missing skills to become placement ready."
                )

            else:
                st.warning(
                    "You need more preparation for this role."
                )

# =================================================
# TAB 2 - APTITUDE TEST
# =================================================

with tab2:

    st.header("📝 Aptitude Practice")

    aptitude_questions = [

        {
            "question": "If 5 workers complete a job in 10 days, how many days will 10 workers take?",
            "options": ["2 days", "5 days", "10 days", "20 days"],
            "answer": "5 days"
        },

        {
            "question": "What is 20% of 250?",
            "options": ["25", "40", "50", "75"],
            "answer": "50"
        },

        {
            "question": "What is the average of 10, 20 and 30?",
            "options": ["15", "20", "25", "30"],
            "answer": "20"
        },

        {
            "question": "If x = 5, what is x²?",
            "options": ["10", "15", "20", "25"],
            "answer": "25"
        },

        {
            "question": "What is the next number: 2, 4, 8, 16, ?",
            "options": ["18", "24", "32", "36"],
            "answer": "32"
        }
    ]

    for i, q in enumerate(aptitude_questions):

        st.write(f"**Q{i + 1}. {q['question']}**")

        st.radio(
            "Select your answer:",
            q["options"],
            key=f"question_{i}"
        )

    if st.button("📊 Calculate Aptitude Score"):

        score = 0

        for i, q in enumerate(aptitude_questions):

            selected_answer = st.session_state[
                f"question_{i}"
            ]

            if selected_answer == q["answer"]:
                score += 1

        percentage = (score / len(aptitude_questions)) * 100

        st.success(
            f"You scored {score}/{len(aptitude_questions)}"
        )

        st.metric(
            "Aptitude Score",
            f"{percentage:.0f}%"
        )

# =================================================
# TAB 3 - INTERVIEW PRACTICE
# =================================================

with tab3:

    st.header("🎥 Live AI Mock Interview")
    st.write(f"Practice a voice/video interview for **{selected_role}**")

    questions = job_roles[selected_role]["questions"]

    if "interview_index" not in st.session_state:
        st.session_state.interview_index = 0
    if "interview_scores" not in st.session_state:
        st.session_state.interview_scores = []
    if "interview_transcripts" not in st.session_state:
        st.session_state.interview_transcripts = []

    current_question = questions[st.session_state.interview_index % len(questions)]

    st.info(f"🎤 Interviewer: {current_question}")

    if st.button("🔊 Hear Question", key="hear_question"):
        import streamlit.components.v1 as components
        safe_question = current_question.replace("\\", "\\\\").replace("'", "\\'")
        components.html(
            f"""
            <script>
                const text = '{safe_question}';
                const speech = new SpeechSynthesisUtterance(text);
                speech.lang = 'en-IN';
                speech.rate = 0.95;
                window.speechSynthesis.cancel();
                window.speechSynthesis.speak(speech);
            </script>
            """,
            height=0,
        )

    st.markdown("### 📹 Camera + 🎤 Microphone")
    st.caption("Click START, allow camera/microphone permission, and answer the question aloud.")

    from streamlit_webrtc import webrtc_streamer
    import av
    import threading
    import numpy as np

    if "audio_buffer" not in st.session_state:
        st.session_state.audio_buffer = []
    if "audio_lock" not in st.session_state:
        st.session_state.audio_lock = threading.Lock()

    audio_lock = st.session_state.audio_lock
    audio_buffer = st.session_state.audio_buffer

    def audio_frame_callback(frame: av.AudioFrame):
        samples = np.asarray(frame.to_ndarray())

        if samples.ndim > 1:
            samples = samples.astype(np.float32).mean(axis=0)
        else:
            samples = samples.astype(np.float32)

        max_value = np.max(np.abs(samples)) if samples.size else 0
        if max_value <= 1.5:
            samples = samples * 32767.0

        samples = np.clip(samples, -32768, 32767).astype(np.int16)

        with audio_lock:
            audio_buffer.append((frame.sample_rate, samples.tobytes()))

        return frame

    webrtc_streamer(
        key="live-interview",
        audio_frame_callback=audio_frame_callback,
        media_stream_constraints={"video": True, "audio": True},
        async_processing=True,
    )

    st.caption("🟢 START = begin. STOP = finish camera/microphone streaming.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🗑️ Clear Recording", key="clear_recording"):
            with audio_lock:
                audio_buffer.clear()
            st.success("Recording cleared. Start speaking again.")

    with col2:
        evaluate_spoken = st.button("🤖 Evaluate Spoken Answer", key="evaluate_spoken")

    if evaluate_spoken:
        import io
        import wave
        import speech_recognition as sr

        with audio_lock:
            chunks = list(audio_buffer)

        if not chunks:
            st.warning("No audio was captured. Click START and speak for a few seconds.")
        else:
            sample_rate = chunks[0][0]
            raw_audio = b"".join(chunk for rate, chunk in chunks if rate == sample_rate)

            wav_buffer = io.BytesIO()
            with wave.open(wav_buffer, "wb") as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(raw_audio)
            wav_buffer.seek(0)

            recognizer = sr.Recognizer()

            try:
                with sr.AudioFile(wav_buffer) as source:
                    audio_data = recognizer.record(source)

                with st.spinner("🎧 Converting your speech to text..."):
                    transcript = recognizer.recognize_google(audio_data, language="en-IN")

                st.success("✅ Speech detected")
                st.markdown("### 📝 Your spoken answer")
                st.write(transcript)

                answer_lower = transcript.lower()
                required_skills = job_roles[selected_role]["skills"]
                matched_skills = [
                    skill for skill in required_skills
                    if skill.lower() in answer_lower
                ]

                word_count = len(transcript.split())
                content_score = min(40, len(matched_skills) * 8)
                detail_score = min(35, word_count * 1.5)
                clarity_score = 25 if word_count >= 15 else 12
                total_score = min(100, round(content_score + detail_score + clarity_score))

                st.markdown("### 📊 Interview Feedback")
                st.metric("Answer Score", f"{total_score}/100")

                if total_score >= 80:
                    st.success("🌟 Excellent answer! Your response is detailed and relevant.")
                elif total_score >= 60:
                    st.info("👍 Good answer. Add more technical details and examples.")
                else:
                    st.warning("⚠️ Try giving a longer answer with a definition and real example.")

                st.write(f"**Words spoken:** {word_count}")
                st.write(f"**Relevant skills detected:** {', '.join(matched_skills) if matched_skills else 'None detected'}")

                st.session_state.interview_scores.append(total_score)
                st.session_state.interview_transcripts.append(transcript)

            except sr.UnknownValueError:
                st.error("I could not understand the audio. Please speak clearly and try again.")
            except sr.RequestError:
                st.error("Speech recognition needs an internet connection. Please check your internet and try again.")
            except Exception as e:
                st.error(f"Audio processing error: {e}")

    if st.button("➡️ Next Interview Question", key="next_interview_question"):
        with audio_lock:
            audio_buffer.clear()
        st.session_state.interview_index += 1
        st.rerun()

    if st.session_state.interview_scores:
        st.markdown("### 🏆 Interview Progress")
        average_score = sum(st.session_state.interview_scores) / len(st.session_state.interview_scores)
        st.metric("Average Interview Score", f"{average_score:.0f}/100")
        st.write(f"Questions answered: {len(st.session_state.interview_scores)}")

# =================================================

# TAB 4 - PREPARATION PLAN
# =================================================

with tab4:

    st.header("🎯 Personalized Preparation Plan")

    required_skills = job_roles[selected_role]["skills"]

    st.write(
        f"### Preparation Roadmap for {selected_role}"
    )

    data = {
        "Day": [
            "Day 1",
            "Day 2",
            "Day 3",
            "Day 4",
            "Day 5",
            "Day 6",
            "Day 7"
        ],
        "Focus Area": [
            required_skills[0],
            required_skills[1] if len(required_skills) > 1 else "Programming",
            "Aptitude",
            "Technical Interview",
            "Coding Practice",
            "HR Interview",
            "Mock Interview"
        ]
    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.success(
        "💡 Tip: Practice coding, aptitude and interview questions every day."
    )

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.markdown("---")

st.write(
    "🎓 AI Placement Preparation System | Python + Streamlit + Machine Learning"
)