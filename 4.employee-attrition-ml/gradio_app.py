import gradio as gr
import numpy as np
from app.model import load_model

# Automatically loads or trains model
model = load_model()

def predict(age, income, years, satisfaction, worklife):
    data = np.array([[age, income, years, satisfaction, worklife]])
    result = model.predict(data)[0]
    return "Employee will LEAVE ❌" if result == 1 else "Employee will STAY ✅"

interface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Age"),
        gr.Number(label="Monthly Income"),
        gr.Number(label="Years at Company"),
        gr.Slider(1, 5, step=1, label="Job Satisfaction"),
        gr.Slider(1, 5, step=1, label="Work Life Balance")
    ],
    outputs="text",
    title="Employee Attrition Predictor",
    description="Predict whether an employee will leave or stay"
)

def launch_gradio():
    interface.launch()
