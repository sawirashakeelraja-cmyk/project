from services.gemini_service import generate_response

result = generate_response(
    "Create one simple English grammar question for a beginner."
)

print(result)