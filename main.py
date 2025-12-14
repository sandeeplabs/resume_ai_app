from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routes
from routes import resume #, job, tailor, ai_tailor

app = FastAPI(
    title="AI Resume Tailor",
    description="Upload resumes, match to job descriptions, AI-powered tailoring",
    version="0.1.0"
)

# Enable CORS (optional, useful for frontend dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(resume.router, prefix="/resume", tags=["Resume"])
# app.include_router(job.router, prefix="/job", tags=["Job"])
# app.include_router(tailor.router, prefix="/tailor", tags=["Tailoring"])
# app.include_router(ai_tailor.router, prefix="/ai-tailor", tags=["AI Tailoring"])

# Root endpoint for sanity check
@app.get("/")
def root():
    return {"message": "AI Resume Tailor API is running 🚀"}
