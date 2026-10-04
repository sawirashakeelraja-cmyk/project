from crewai import Agent
from services.gemini_service import generate_response


def coach_analyze(student_level, performance):
    prompt = f"""
You are an English Learning Coach.

Student level: {student_level}

Student performance:
{performance}

Analyze the student's performance and decide:

1. What is the student's strongest area?
2. What is the student's weakest area?
3. What should the student practice next?
4. Should the difficulty be increased, decreased, or kept the same?

Give a short and clear recommendation.
"""

    return generate_response(prompt)


coach_agent = Agent(
    role="English Learning Coach",
    goal="Analyze student performance and decide the best next English learning activity.",
    backstory=(
        "You are an experienced English learning coach who analyzes "
        "student performance, identifies weak areas, adjusts difficulty, "
        "and recommends personalized practice."
    ),
    verbose=True
)