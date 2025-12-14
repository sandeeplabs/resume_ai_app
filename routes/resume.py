from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
# from services.resume_service import save_resume, list_resumes, get_resume_details

router = APIRouter()

# Upload a resume
@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload a resume (PDF or DOCX).
    """
    try:
        # result = await save_resume(file)
        result = file.filename
        return JSONResponse(content={"message": "Resume uploaded successfully", "data": result})
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

# List all uploaded resumes
@router.get("/list")
async def get_resumes():
    """
    List all uploaded resumes.
    """
    # resumes = list_resumes()
    resumes = ["resume1.pdf", "resume2.docx"]
    return {"resumes": resumes}

# Get structured details of a specific resume
@router.get("/{resume_id}")
async def get_resume(resume_id: str):
    """
    Get parsed information of a specific resume.
    """
    # details = get_resume_details(resume_id)
    details = {"name": "John Doe", "experience": "5 years"} if resume_id == "resume1" else None
    if not details:
        raise HTTPException(status_code=404, detail="Resume not found")
    return {"resume": details}
