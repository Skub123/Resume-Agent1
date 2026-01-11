from fastapi import FastAPI
from app.api.resume import router as resume_router

app = FastAPI(title="AI Resume Agent")

app.include_router(resume_router, prefix="/api")

@app.get("/")
def health():
    return {"status": "running"}
