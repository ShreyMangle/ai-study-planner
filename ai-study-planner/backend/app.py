from flask import Flask, request, jsonify
from flask_cors import CORS
from planner import generate_base_plan
from ai_engine import ai_reasoning
from adaptive import adapt_plan

app = Flask(__name__)
CORS(app) 


@app.route("/")
def home():
    return "AI Study Planner Backend is Running"


@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    data = request.json
    base_plan = generate_base_plan(data)
    ai_plan = ai_reasoning(base_plan, data)
    return jsonify(ai_plan)


@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    updated_plan = adapt_plan(data)
    return jsonify(updated_plan)


if __name__ == "__main__":
    app.run(debug=True)
