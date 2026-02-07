def generate_plan(data):
    pace_factor = {
        "slow": 1.2,
        "medium": 1.0,
        "fast": 0.8
    }[data.learning_pace]

    plans = []

    for t in data.topics:
        learning_gap = max(t.difficulty - t.confidence, 1)
        urgency = 1 / max(t.deadline_days, 1)

        priority = (learning_gap * t.weight) * urgency
        predicted_time = priority * pace_factor

        max_time = 1.0 if t.difficulty >= 7 else 1.5

        plans.append({
            "topic": t.name,
            "allocated_hours": round(min(predicted_time, max_time), 2),
            "reason": {
                "learning_gap": learning_gap,
                "urgency": urgency
            }
        })

    return plans
