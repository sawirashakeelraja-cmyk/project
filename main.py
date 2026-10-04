
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.practice import router as practice_router
from api.writing import router as writing_router


app = FastAPI(
    title="AI English Coach API",
    description="Personalized English learning platform",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API Routers
app.include_router(practice_router)
app.include_router(writing_router)


@app.get("/")
def home():

    return {
        "message": "AI English Coach backend is running!"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

