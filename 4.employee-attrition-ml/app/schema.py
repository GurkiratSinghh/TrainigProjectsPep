from tokenize import String
from pydantic import BaseModel, Field

class EmployeeData(BaseModel):
    age: int = Field(..., ge=18, le=65)
    monthly_income: int = Field(..., ge=10000)
    years_at_company: int = Field(..., ge=0)
    job_satisfaction: int = Field(..., ge=1, le=5)
    work_life_balance: int = Field(..., ge=1, le=5)
    mess: int= Field(..., ge=0, le=1)
