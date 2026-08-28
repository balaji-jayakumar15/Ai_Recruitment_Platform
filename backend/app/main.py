from fastapi import FastAPI

app = FastAPI(
    title="AI Recruitment Platform API",
    description="AI-powered recruitment platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Recruitment Platform API is running"
    }