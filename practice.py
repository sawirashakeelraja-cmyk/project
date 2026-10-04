from fastapi import APIRouter
from pydantic import BaseModel

from flows.english_coach_flow import run_english_coach
from services.gemini_service import generate_response


router = APIRouter(
    prefix="/api",
    tags=["Practice"]
)


# -----------------------------
# Practice Request
# -----------------------------

class PracticeRequest(BaseModel):
    student_level: str = "Beginner"
    performance: str = "No previous performance available"
    activity: str = "General English practice"


# -----------------------------
# Practice Result Request
# -----------------------------

class PracticeResultRequest(BaseModel):
    student_level: str = "Beginner"
    activity: str = "Reading"
    score: int
    total_questions: int
    answers: dict


# -----------------------------
# Generate AI Practice
# -----------------------------

@router.post("/practice")
def practice(request: PracticeRequest):

    result = run_english_coach(
        student_level=request.student_level,
        performance=request.performance,
        activity=request.activity
    )

    return {
        "success": True,
        "coach_decision": result["coach_decision"],
        "practice": result["practice"]
    }


# -----------------------------
# Save Practice Result
# -----------------------------

@router.post("/practice/result")
def save_practice_result(
    request: PracticeResultRequest
):

    percentage = round(
        (request.score / request.total_questions) * 100
    )

    prompt = f"""
You are an encouraging English Learning Coach.

Student level:
{request.student_level}

Activity:
{request.activity}

Score:
{request.score}/{request.total_questions}

Percentage:
{percentage}%

Give short personalized feedback.

Include:

1. What the student did well
2. What they should improve
3. One simple tip for improvement
4. A short encouraging message

Keep the language simple.

Do not be too long.
"""

    feedback = generate_response(prompt)

    return {
        "success": True,
        "activity": request.activity,
        "score": request.score,
        "total_questions": request.total_questions,
        "percentage": percentage,
        "feedback": feedback
    }


# -----------------------------
# Progress Endpoint
# -----------------------------

@router.get("/progress")
def get_progress():

    return {
        "success": True,
        "total_practices": 0,
        "average_score": 0,
        "reading_completed": 0,
        "writing_completed": 0,
        "vocabulary_completed": 0,
        "grammar_completed": 0,
        "streak": 0
    }