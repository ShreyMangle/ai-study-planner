from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import PlanRequest
from scheduler import generate_plan

app = FastAPI(title="CogniPlan API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:5501",
        "http://localhost:5501",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/plan")
def create_plan(request: PlanRequest):
    plan = generate_plan(request)
    return {
        "plan": plan,
        "message": "Explainable cognitive plan generated"
    }
