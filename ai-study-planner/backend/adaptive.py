def adapt_plan(data):
    current_plan = data["current_plan"]
    feedback = data["feedback"]

    fatigue = feedback.get("fatigue_level", "normal")
    missed = feedback.get("missed_subjects", [])

    for s in current_plan:
        if s["subject"] in missed:
            s["allocated_hours"] = round(s["allocated_hours"] * 1.15, 2)

        if fatigue == "high":
            s["allocated_hours"] = round(s["allocated_hours"] * 0.85, 2)

    return {
        "updated_plan": current_plan,
        "note": "Plan adaptively rebalanced based on user feedback and cognitive fatigue."
    }
