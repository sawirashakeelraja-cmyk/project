
from fastapi import APIRouter
from pydantic import BaseModel

from services.gemini_service import generate_response


router = APIRouter(
    prefix="/api/writing",
    tags=["Writing"]
)


class WritingRequest(BaseModel):

    student_level: str = "Beginner"

    topic: str = (
        "Write 5 to 7 sentences about your daily routine."
    )

    answer: str


@router.post("/evaluate")
def evaluate_writing(request: WritingRequest):

    prompt = f"""
You are an expert English Writing Coach.

Student level:
{request.student_level}

Writing topic:
{request.topic}

Student's answer:
{request.answer}

Evaluate the student's writing.

Give simple and encouraging feedback.

Include:

1. Overall score out of 10
2. Grammar feedback
3. Vocabulary feedback
4. Spelling and punctuation feedback
5. Coherence and sentence structure feedback
6. What the student did well
7. What the student should improve
8. Corrected version of the student's writing
9. One simple tip for improvement

The student is a beginner, so use simple English.

Do not be too harsh.
Do not make the feedback extremely long.
"""


    feedback = generate_response(prompt)


    return {
        "success": True,
        "student_level": request.student_level,
        "topic": request.topic,
        "feedback": feedback
    }
