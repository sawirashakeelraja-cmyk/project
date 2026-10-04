from flows.english_coach_flow import run_english_coach


performance = """
Reading: 80%
Writing: 60%
Vocabulary: 45%
Grammar: 50%
"""

result = run_english_coach(
    student_level="Beginner",
    performance=performance,
    activity="Choose the best next practice"
)

print("\n===== COACH DECISION =====")
print(result["coach_decision"])

print("\n===== NEXT PRACTICE =====")
print(result["practice"])