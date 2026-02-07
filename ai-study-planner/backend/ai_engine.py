def ai_reasoning(plan, user_data):
    strategies = []
    ordered_subjects = []
    decision_trace = []

    for s in plan:
        
        if s["difficulty"] >= 4 and s["deadline_days"] <= 7:
            strategy = "Use focused 25-minute Pomodoro sessions with active recall."
        elif s["difficulty"] >= 4:
            strategy = "Apply spaced repetition and frequent revision."
        elif s["deadline_days"] <= 5:
            strategy = "Prioritize quick summaries and practice questions."
        else:
            strategy = "Use concept mapping and light practice."

        strategies.append({
            "subject": s["subject"],
            "recommended_strategy": strategy,
            "reason": f"Difficulty {s['difficulty']} and deadline in {s['deadline_days']} days."
        })

        ordered_subjects.append(s["subject"])

        # === Decision trace (EXPLAINABILITY UPGRADE) ===
        confidence = s.get("confidence", user_data.get("confidence", 3))
        learning_gap = s["difficulty"] - confidence

        if learning_gap >= 2:
            decision_trace.append(
                f"{s['subject']} prioritized due to low confidence ({confidence}) "
                f"and high difficulty ({s['difficulty']})."
            )

        if s["difficulty"] >= 4:
            decision_trace.append(
                f"{s['subject']} session duration capped to prevent cognitive fatigue."
            )

        if s["deadline_days"] <= 7:
            decision_trace.append(
                f"{s['subject']} given urgency boost due to upcoming deadline."
            )

    explanation = (
        "This study plan is generated using an explainable AI engine that combines "
        "deterministic planning with human-centric learning heuristics. "
        "Each decision is traceable to factors such as confidence, difficulty, urgency, "
        "and cognitive load constraints."
    )

    return {
        "daily_schedule": plan,
        "study_order": ordered_subjects,
        "personalized_strategies": strategies,
        "decision_trace": decision_trace,
        "ai_explanation": explanation,
        "ai_type": "Explainable, Confidence-Aware Rule-Based AI (Offline, Free)"
    }
