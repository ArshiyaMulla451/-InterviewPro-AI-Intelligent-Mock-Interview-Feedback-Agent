import streamlit as st
import ollama
import re
from gtts import gTTS
import os

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="InterviewPro AI",
    page_icon="🎯",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #777;
    font-size: 18px;
    margin-bottom: 30px;
}

.question-card {
    padding: 30px;
    border-radius: 15px;
    background-color: #f5f7fb;
    border: 1px solid #ddd;
    margin-top: 20px;
    margin-bottom: 20px;
}

.question-text {
    font-size: 24px;
    font-weight: 600;
}

.feedback-card {
    padding: 25px;
    border-radius: 15px;
    background-color: #f8f9fa;
    border: 1px solid #ddd;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "started": False,
    "question_number": 0,
    "current_question": "",
    "answers": [],
    "feedback": "",
    "scores": [],
    "answer_submitted": False,
    "finished": False,
    "final_report": ""
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# OLLAMA AI FUNCTION
# =========================================================

def ask_ollama(prompt):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()


# =========================================================
# GENERATE INTERVIEW QUESTION
# =========================================================

def generate_question(
    interview_type,
    job_role,
    experience,
    difficulty,
    skills,
    previous_question="",
    previous_answer=""
):

    prompt = f"""
You are a professional AI interviewer.

Conduct a mock interview.

Interview Type: {interview_type}
Job Role: {job_role}
Experience Level: {experience}
Difficulty: {difficulty}
Candidate Skills: {skills}

Previous Question:
{previous_question}

Previous Answer:
{previous_answer}

Generate the next interview question.

Rules:
1. Ask exactly ONE question.
2. Do not provide an answer.
3. Do not provide feedback.
4. Do not add numbering.
5. Do not add explanations.
6. The question must be relevant to the job role.
7. If a previous answer is available, adapt the next question based on it.
8. Return ONLY the interview question.
"""

    return ask_ollama(prompt)


# =========================================================
# TEXT TO SPEECH
# =========================================================

def create_audio(text):

    filename = "question_audio.mp3"

    tts = gTTS(
        text=text,
        lang="en",
        slow=False
    )

    tts.save(filename)

    return filename


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🎯 InterviewPro AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your Intelligent AI Mock Interview & Feedback Agent</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ Interview Setup")

    interview_type = st.selectbox(
        "Interview Type",
        [
            "HR Interview",
            "Technical Interview",
            "Coding Interview",
            "Aptitude Interview",
            "Communication Interview"
        ]
    )

    job_role = st.text_input(
        "Job Role",
        placeholder="Example: Software Developer"
    )

    experience = st.selectbox(
        "Experience Level",
        [
            "Fresher",
            "0-2 Years",
            "2-5 Years",
            "5+ Years"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    skills = st.text_area(
        "Your Skills",
        placeholder="Python, Java, SQL, Machine Learning"
    )

    total_questions = st.slider(
        "Number of Questions",
        3,
        10,
        5
    )


# =========================================================
# START INTERVIEW
# =========================================================

if not st.session_state.started:

    st.subheader("🚀 Start Your AI Mock Interview")

    st.write(
        "Configure your interview using the sidebar and start your personalized AI interview."
    )

    if st.button(
        "🎤 Start Interview",
        type="primary",
        use_container_width=True
    ):

        if not job_role.strip():

            st.warning(
                "⚠️ Please enter a job role before starting."
            )

        else:

            with st.spinner(
                "🤖 Ollama AI is preparing your first question..."
            ):

                try:

                    question = generate_question(
                        interview_type,
                        job_role,
                        experience,
                        difficulty,
                        skills
                    )

                    if not question:

                        st.error(
                            "❌ Ollama returned an empty question."
                        )

                    else:

                        st.session_state.current_question = question

                        st.session_state.question_number = 1

                        st.session_state.started = True

                        st.session_state.answer_submitted = False

                        st.rerun()

                except Exception as e:

                    st.error(
                        f"❌ Ollama Error: {e}"
                    )


# =========================================================
# INTERVIEW SCREEN
# =========================================================

if (
    st.session_state.started
    and not st.session_state.finished
):

    st.subheader(
        f"🎤 Question {st.session_state.question_number} "
        f"of {total_questions}"
    )

    progress = (
        st.session_state.question_number
        / total_questions
    )

    st.progress(progress)


    # =====================================================
    # QUESTION DISPLAY
    # =====================================================

    st.markdown(
        f"""
        <div class="question-card">

        <div class="question-text">
        ❓ {st.session_state.current_question}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # LISTEN TO QUESTION
    # =====================================================

    if st.button(
        "🔊 Listen to Question",
        use_container_width=True
    ):

        with st.spinner(
            "🔊 Preparing audio..."
        ):

            try:

                audio_file = create_audio(
                    st.session_state.current_question
                )

                st.audio(
                    audio_file,
                    format="audio/mp3"
                )

            except Exception as e:

                st.error(
                    f"Could not generate audio: {e}"
                )


    # =====================================================
    # ANSWER INPUT
    # =====================================================

    answer = st.text_area(
        "📝 Your Answer",
        height=200,
        placeholder="Type your answer here..."
    )


    # =====================================================
    # SUBMIT ANSWER
    # =====================================================

    if not st.session_state.answer_submitted:

        if st.button(
            "📊 Submit Answer",
            type="primary",
            use_container_width=True
        ):

            if not answer.strip():

                st.warning(
                    "⚠️ Please enter your answer."
                )

            else:

                with st.spinner(
                    "🤖 Ollama AI is evaluating your answer..."
                ):

                    try:

                        evaluation_prompt = f"""
You are an expert interview evaluator.

Evaluate the candidate's answer.

Interview Type:
{interview_type}

Job Role:
{job_role}

Experience:
{experience}

Difficulty:
{difficulty}

Question:
{st.session_state.current_question}

Candidate Answer:
{answer}

Give the evaluation in exactly this format:

SCORE: X/10

STRENGTHS:
- Strength 1
- Strength 2

WEAKNESSES:
- Weakness 1
- Weakness 2

FEEDBACK:
Give constructive feedback.

IMPROVEMENT:
Give specific advice to improve the answer.

Do not ask another question.
"""

                        feedback = ask_ollama(
                            evaluation_prompt
                        )

                        # Extract score
                        match = re.search(
                            r"SCORE:\s*(\d+)",
                            feedback,
                            re.IGNORECASE
                        )

                        score = 0

                        if match:

                            score = int(
                                match.group(1)
                            )

                        st.session_state.scores.append(
                            score
                        )

                        st.session_state.answers.append(
                            {
                                "question":
                                    st.session_state.current_question,

                                "answer":
                                    answer,

                                "feedback":
                                    feedback
                            }
                        )

                        st.session_state.feedback = feedback

                        st.session_state.answer_submitted = True

                        st.rerun()

                    except Exception as e:

                        st.error(
                            f"❌ Evaluation Error: {e}"
                        )


    # =====================================================
    # SHOW FEEDBACK
    # =====================================================

    if st.session_state.answer_submitted:

        st.divider()

        st.subheader("📊 AI Evaluation")

        st.markdown(
            f"""
            <div class="feedback-card">

            {st.session_state.feedback}

            </div>
            """,
            unsafe_allow_html=True
        )


        # =================================================
        # NEXT QUESTION
        # =================================================

        if (
            st.session_state.question_number
            < total_questions
        ):

            if st.button(
                "➡️ Next Question",
                type="primary",
                use_container_width=True
            ):

                previous_question = (
                    st.session_state.current_question
                )

                previous_answer = (
                    st.session_state.answers[-1]["answer"]
                )

                with st.spinner(
                    "🤖 Ollama AI is preparing your next question..."
                ):

                    try:

                        next_question = generate_question(
                            interview_type,
                            job_role,
                            experience,
                            difficulty,
                            skills,
                            previous_question,
                            previous_answer
                        )

                        st.session_state.current_question = (
                            next_question
                        )

                        st.session_state.question_number += 1

                        st.session_state.feedback = ""

                        st.session_state.answer_submitted = False

                        st.rerun()

                    except Exception as e:

                        st.error(
                            f"❌ Error generating next question: {e}"
                        )


        # =================================================
        # FINISH INTERVIEW
        # =================================================

        else:

            if st.button(
                "🏆 Finish Interview & Generate Report",
                type="primary",
                use_container_width=True
            ):

                with st.spinner(
                    "📊 Ollama is generating your final report..."
                ):

                    try:

                        history = ""

                        for i, item in enumerate(
                            st.session_state.answers,
                            start=1
                        ):

                            history += f"""
QUESTION {i}:
{item['question']}

ANSWER:
{item['answer']}

FEEDBACK:
{item['feedback']}

"""


                        final_prompt = f"""
You are a professional interview coach.

Create a final interview performance report.

Job Role:
{job_role}

Interview Type:
{interview_type}

Candidate Experience:
{experience}

Interview History:
{history}

Provide:

1. Overall Performance
2. Key Strengths
3. Areas for Improvement
4. Technical Skills Assessment
5. Communication Assessment
6. Interview Readiness
7. Personalized Improvement Plan
8. Final Recommendation

Be professional and constructive.
"""

                        final_report = ask_ollama(
                            final_prompt
                        )

                        st.session_state.final_report = (
                            final_report
                        )

                        st.session_state.finished = True

                        st.rerun()

                    except Exception as e:

                        st.error(
                            f"❌ Report Generation Error: {e}"
                        )


# =========================================================
# FINAL REPORT
# =========================================================

if st.session_state.finished:

    st.header(
        "🏆 Final Interview Performance Report"
    )

    if st.session_state.scores:

        average_score = (
            sum(st.session_state.scores)
            /
            len(st.session_state.scores)
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Overall Score",
                f"{average_score:.1f}/10"
            )

        with col2:

            st.metric(
                "Questions",
                len(st.session_state.answers)
            )

        with col3:

            if average_score >= 8:

                readiness = "Excellent"

            elif average_score >= 6:

                readiness = "Good"

            else:

                readiness = "Needs Improvement"

            st.metric(
                "Interview Readiness",
                readiness
            )


    st.divider()

    st.markdown(
        st.session_state.final_report
    )


    st.divider()


    # =====================================================
    # START NEW INTERVIEW
    # =====================================================

    if st.button(
        "🔄 Start New Interview",
        use_container_width=True
    ):

        for key in list(
            st.session_state.keys()
        ):

            del st.session_state[key]

        st.rerun()