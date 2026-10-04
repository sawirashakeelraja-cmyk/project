from crewai import Agent
from services.gemini_service import generate_response


def language_practice(student_level, topic):
    prompt = f"""
You are an English Grammar and Vocabulary Specialist.

Student level: {student_level}
Topic: {topic}

Create a short language practice exercise.

Include:
1. Three grammar questions
2. Three vocabulary questions
3. Correct answers
4. A short explanation for each answer

Use simple language appropriate for the student's level.
"""

    return generate_response(prompt)


language_agent = Agent(
    role="Language Specialist",
    goal="Help students improve grammar and vocabulary.",
    backstory=(
        "You are an English grammar and vocabulary expert. "
        "You create grammar exercises, vocabulary questions, "
        "sentence corrections, fill-in-the-blanks, and explain answers."
    ),
    verbose=True
)