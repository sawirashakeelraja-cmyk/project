from crewai import Agent
from services.gemini_service import generate_response


def writing_practice(student_level, topic):
    prompt = f"""
You are an English Writing Specialist.

Student level: {student_level}
Topic: {topic}

Create a writing exercise for the student.

Provide:
1. A clear writing prompt
2. What the student should write
3. Important points they should include
4. A simple evaluation guide

Keep the task appropriate for the student's English level.
"""

    return generate_response(prompt)


writing_agent = Agent(
    role="Writing Specialist",
    goal="Help students improve English writing skills.",
    backstory=(
        "You are an experienced English writing teacher. "
        "You evaluate grammar, vocabulary, coherence, content, "
        "and provide useful corrections."
    ),
    verbose=True
)