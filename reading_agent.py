from crewai import Agent
from services.gemini_service import generate_response


def reading_practice(student_level, topic):
    prompt = f"""
You are an English Reading Specialist.

Student level: {student_level}
Topic: {topic}

Create a short English reading passage suitable for the student's level.

Then provide:
1. The reading passage
2. Three comprehension questions
3. The correct answers
4. A short explanation for each answer

Keep the language appropriate for the student's level.
"""

    return generate_response(prompt)


reading_agent = Agent(
    role="Reading Specialist",
    goal="Help students improve English reading comprehension.",
    backstory=(
        "You are an experienced English reading teacher. "
        "You create suitable reading passages, comprehension questions, "
        "evaluate answers, and explain mistakes clearly."
    ),
    verbose=True
)