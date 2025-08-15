from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ExamBuddy.AI API", version="1.0")

# Models
class IngestRequest(BaseModel):
    text: str

class PlanRequest(BaseModel):
    syllabus: list[str]

class QuizRequest(BaseModel):
    topic: str

# Stub endpoints
@app.post("/ingest")
def ingest_file(req: IngestRequest):
    # Stub: Later parse PDF/notes here
    return {"status": "success", "message": "File ingested", "text_length": len(req.text)}

@app.post("/plan")
def generate_plan(req: PlanRequest):
    # Stub: Later generate AI-based plan here
    return {"plan": [{"day": 1, "topic": t} for t in req.syllabus]}

@app.post("/quiz")
def generate_quiz(req: QuizRequest):
    # Stub: Later generate AI-based quiz here
    return {
        "topic": req.topic,
        "questions": [
            {"q": f"Sample question 1 for {req.topic}", "options": ["A", "B", "C", "D"], "answer": "A"}
        ]
    }
