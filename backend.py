from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

# ---------------- API KEY ----------------
# 👉 Replace with your real key (for now)
genai.configure(api_key="AIzaSyCIlzjjtBYO5i8P_yIf_nmWObWrV1TBB70")

model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- APP ----------------
app = FastAPI()

# Request schema
class BlogRequest(BaseModel):
    topic: str
    tone: str
    length: str

# Root (optional)
@app.get("/")
def home():
    return {"message": "Backend is running"}

# Blog endpoint
@app.post("/generate_blog")
def generate_blog(req: BlogRequest):
    prompt = f"""
    Write a {req.length} blog about "{req.topic}" 
    in a {req.tone} tone.
    """

    try:
        response = model.generate_content(prompt)
        return {"blog": response.text}
    except Exception as e:
        return {"error": str(e)}