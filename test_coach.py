from agents.coach_agent import coach_analyze


performance = """
Reading: 80%
Writing: 60%
Vocabulary: 45%
Grammar: 50%
"""

result = coach_analyze(
    student_level="Beginner",
    performance=performance
)

print("\n===== COACH RECOMMENDATION =====")
print(result)