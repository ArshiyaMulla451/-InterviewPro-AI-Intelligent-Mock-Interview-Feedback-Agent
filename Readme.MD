# 🎯 InterviewPro AI – Intelligent Mock Interview & Feedback Agent

InterviewPro AI is an AI-powered mock interview application that helps students, freshers, and job seekers practice interviews in an interactive and personalized environment.

The application uses **Ollama and a locally running Large Language Model (LLM)** to conduct mock interviews, dynamically generate interview questions, evaluate candidate responses, provide constructive feedback, and generate a final performance report.

The application is built using **Python and Streamlit** and includes a **Text-to-Speech (TTS)** feature that allows users to listen to AI-generated interview questions.

Unlike cloud-based AI APIs, this project uses **Ollama to run the AI model locally**, making the application suitable for offline AI experimentation and reducing dependency on external AI API keys.

---

## 🚀 Features

### 🎤 AI-Powered Mock Interviews

Conduct an interactive mock interview with a locally running AI interviewer powered by Ollama.

The AI dynamically generates interview questions based on the candidate's selected preferences.

---

### 💼 Multiple Interview Types

Users can choose from different interview categories:

* HR Interview
* Technical Interview
* Coding Interview
* Aptitude Interview
* Communication Interview

---

### 👨‍💻 Personalized Interview Setup

The interview can be customized based on:

* Job Role
* Experience Level
* Difficulty Level
* Candidate Skills
* Number of Questions

---

### 🤖 AI-Generated Interview Questions

Ollama generates relevant interview questions based on:

* Interview Type
* Job Role
* Experience Level
* Difficulty Level
* Candidate Skills

The AI returns one question at a time to create an interactive interview experience.

---

### 🔊 Text-to-Speech

Users can listen to AI-generated interview questions using the **gTTS (Google Text-to-Speech)** feature.

This allows the application to simulate a more realistic interview experience where the AI interviewer can speak the question aloud.

---

### 📝 AI-Powered Answer Evaluation

The AI evaluates the candidate's answers and provides:

* Score out of 10
* Strengths
* Weaknesses
* Constructive Feedback
* Improvement Suggestions

---

### 🧠 Adaptive Interview Questions

The next interview question is dynamically generated based on the candidate's previous question and answer.

This makes the interview more personalized and interactive rather than using a fixed set of questions.

---

### 📊 Final Performance Report

After completing the interview, Ollama generates a detailed performance report containing:

* Overall Performance
* Key Strengths
* Areas for Improvement
* Technical Skills Assessment
* Communication Assessment
* Interview Readiness
* Personalized Improvement Plan
* Final Recommendation

---

### 📈 Interview Readiness Assessment

The application calculates the candidate's average interview score.

Based on the final score, the candidate receives an interview readiness level:

* **Excellent**
* **Good**
* **Needs Improvement**

---

## 🛠️ Technologies Used

* **Python** – Core programming language
* **Streamlit** – Interactive web application framework
* **Ollama** – Local AI model runtime
* **Llama 3.2** – Local Large Language Model used for AI responses
* **Ollama Python Library** – Connects the Python application with the local Ollama model
* **gTTS (Google Text-to-Speech)** – Converts interview questions into speech
* **Regular Expressions (re)** – Used to extract scores from AI-generated evaluations

---

## 🧠 AI Model

This project uses **Ollama** to run the AI model locally.

The default model used in the application is:

```text
llama3.2
```

The model is accessed from Python using the Ollama library:

```python
import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
```

The application uses the local model for:

* Interview question generation
* Candidate answer evaluation
* Adaptive question generation
* Final performance report generation

---

## 🏗️ Project Workflow

```text
User Configures Interview
        ↓
Select Interview Type
        ↓
Enter Job Role & Skills
        ↓
Select Experience & Difficulty
        ↓
Choose Number of Questions
        ↓
Start Interview
        ↓
Ollama Local AI Generates Question
        ↓
Question Displayed on Screen
        ↓
🔊 Listen to Question
        ↓
User Enters Answer
        ↓
Ollama AI Evaluates Answer
        ↓
Score + Feedback + Suggestions
        ↓
Generate Next Adaptive Question
        ↓
Repeat Interview Process
        ↓
Complete All Questions
        ↓
Ollama Generates Final Performance Report
        ↓
📊 Interview Readiness Assessment
```

---

## 📂 Project Structure

```text
InterviewPro-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── question_audio.mp3
```

> **Note:** `question_audio.mp3` is generated automatically when the user selects the **🔊 Listen to Question** option.

---

## ⚙️ Installation & Setup

### 1. Install Ollama

Download and install Ollama on your computer.

After installation, verify that Ollama is working:

```bash
ollama --version
```

---

### 2. Download the AI Model

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2
```

This downloads the model to your local system.

---

### 3. Create a Virtual Environment

Open the project folder in VS Code and create a virtual environment:

```bash
python -m venv venv
```

---

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

---

### 5. Install Python Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install streamlit ollama gTTS
```

---

### 6. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your web browser.

---

## 📦 Requirements

The `requirements.txt` file should contain:

```text
streamlit
ollama
gTTS
```

---

## 🎯 How to Use

### Step 1 – Configure Your Interview

Use the sidebar to select:

* Interview Type
* Job Role
* Experience Level
* Difficulty Level
* Skills
* Number of Questions

---

### Step 2 – Start the Interview

Click:

```text
🎤 Start Interview
```

Ollama will generate the first interview question using the local AI model.

---

### Step 3 – Listen to the Question

The generated question will appear on the screen.

Click:

```text
🔊 Listen to Question
```

The application converts the question into speech using gTTS.

---

### Step 4 – Answer the Question

Enter your response in the answer box.

Click:

```text
📊 Submit Answer
```

---

### Step 5 – Receive AI Feedback

Ollama evaluates your response and provides:

* Score
* Strengths
* Weaknesses
* Feedback
* Improvement Suggestions

---

### Step 6 – Continue the Interview

Click:

```text
➡️ Next Question
```

The next question is generated based on the previous interview interaction.

---

### Step 7 – Generate Final Report

After answering all questions, click:

```text
🏆 Finish Interview & Generate Report
```

The application generates a complete interview performance report.

---

## 🔄 AI Interview Flow

```text
Question Generation
        ↓
Candidate Answer
        ↓
Answer Evaluation
        ↓
Score Calculation
        ↓
Feedback Generation
        ↓
Adaptive Question Generation
        ↓
Final Performance Analysis
```

---

## 🌟 Why InterviewPro AI?

Traditional interview preparation often requires finding a human interviewer or practicing with static question lists.

InterviewPro AI provides an interactive alternative by combining:

* Artificial Intelligence
* Local LLM Processing
* Personalized Interview Questions
* Adaptive Question Generation
* AI-Powered Answer Evaluation
* Text-to-Speech
* Performance Analysis
* Personalized Improvement Recommendations

The use of **Ollama** allows the AI model to run locally on the user's computer, making the application independent of cloud-based AI API keys.

---

## 🧠 Agentic AI Capabilities

InterviewPro AI demonstrates agentic behavior through its ability to:

1. **Understand** the candidate's interview configuration.
2. **Generate** personalized interview questions.
3. **Evaluate** candidate responses.
4. **Adapt** the next question based on previous responses.
5. **Provide** actionable feedback.
6. **Track** interview performance scores.
7. **Generate** a personalized final performance report.

The adaptive interview flow allows the system to dynamically respond to the candidate's performance.

---

## 🔮 Future Enhancements

The project can be further improved by adding:

* 🎙️ Voice-based candidate answers
* 🗣️ Speech-to-Text conversion
* 📄 Resume Upload
* 📌 Resume-Based Interview Questions
* 🎤 Real-Time Voice Interview
* 🧠 Confidence and Communication Analysis
* 📈 Performance Analytics Dashboard
* 📊 Interview Performance Charts
* 📝 Downloadable Interview Reports
* 🌐 Multilingual Interview Support
* 💼 Job Description-Based Questions
* 🔐 User Authentication
* 📚 Interview History
* 💻 Coding Questions with Automated Code Evaluation
* 🤖 Multiple Ollama Model Selection

---

## 🔒 Privacy Advantage

Since the core AI processing is performed using a locally running Ollama model, the project can provide improved privacy compared with applications that send every interview prompt to a cloud-based AI service.

The candidate's interview questions and answers can be processed locally by the selected Ollama model.

> **Note:** The Text-to-Speech feature currently uses gTTS, which requires an internet connection. The AI interview generation and evaluation are handled locally through Ollama.

---




---

## 📄 License

This project is created for educational and learning purposes.

You are free to modify and improve the project for personal and educational use.
