from pydantic import BaseModel, Field

class SymptomResponse(BaseModel):
    probable_cause:str=Field(..., description="What could be causing this symptom")
    severity:str=Field(..., description="Severity level:mild/moderate/severe)")
    advice:str=Field(..., description="Advice on what to do next")
    log_status:str=Field(...,description="Status of logging")