from services.gemini_service import generate_response


def run_english_coach(
    student_level="Beginner",
    performance="No previous performance available",
    activity="General English practice"
):
    """
    Main AI English Coach workflow.

    The Coach analyzes the student's performance
    and creates a suitable practice activity.
    """

    coach_prompt = f"""
You are the main English Learning Coach.

Student level:
{student_level}

Previous performance:
{performance}

Requested activity:
{activity}

Analyze the student and decide which specialist
should handle the next practice.

Available specialists:
- Reading
- Writing
- Language

Return:
1. Recommended specialist
2. Reason
3. Difficulty level
4. Short instructions for that specialist

Keep the response simple and encouraging.
"""

    coach_decision = generate_response(coach_prompt)

    specialist_prompt = f"""
You are an English learning specialist.

Student level:
{student_level}

Previous performance:
{performance}

Requested activity:
{activity}

Coach decision:
{coach_decision}

Create one suitable practice activity for the student.

Include:
- Activity
- Questions or task
- Correct answers where appropriate
- Short explanation

Keep the activity suitable for a {student_level} student.
"""

    practice = generate_response(specialist_prompt)

    return {
        "coach_decision": coach_decision,
        "practice": practice
    }