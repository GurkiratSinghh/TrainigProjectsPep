from fastapi import FastAPI
import numpy as np
from app.schema import EmployeeData
from app.model import load_model

app = FastAPI(title="Employee Attrition Prediction API")

# Automatically loads or trains model
model = load_model()

@app.get("/")
def home():
    return {"message": "Employee Attrition API is running"}

@app.post("/predict")
def predict(data: EmployeeData):
    input_data = np.array([[
        data.age,
        data.monthly_income,
        data.years_at_company,
        data.job_satisfaction,
        data.work_life_balance,
        data.mess
    ]])

    prediction = model.predict(input_data)[0]

    return {
        "prediction": "LEAVE ❌" if prediction == 1 else "STAY ✅"
    }
