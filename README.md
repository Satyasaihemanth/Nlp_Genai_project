# 🧠 NLP Generative AI Project

## 📌 Overview
This project uses Generative AI to generate responses based on user input.

## 🚀 Features
- Text generation using LLM
- Interactive UI
- Real-time responses

## 🛠 Tech Stack
- Python
- Streamlit
- FastAPI
- OpenAI / Gemini API

## 📂 Project Structure
- backend.py → API logic
- frontend.py → UI
- requirements.txt → Dependencies

## ⚙️ How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Add API key:
Create `.env` file:
API_KEY=your_key_here

3. Run backend:
uvicorn backend:app --reload

4. Run frontend:
streamlit run frontend.py

## 🎯 Output
AI-generated responses based on user input
