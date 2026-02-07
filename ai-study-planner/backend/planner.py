import copy


def generate_base_plan(data):
    subjects = data["subjects"]
    daily_hours = data["daily_hours"]
    pace = data["learning_pace"]

    pace_factor = {
        "slow": 1.2,
        "medium": 1.0,
        "fast": 0.8
    }[pace]

   
    for s in subjects:
        confidence = s.get("confidence", 3)  # default confidence
        learning_gap = max(s["difficulty"] - confidence, 1)
        urgency = 1 / s["deadline_days"]

       
        s["priority"] = learning_gap * urgency

    total_priority = sum(s["priority"] for s in subjects)

    plan = []

    for s in subjects:
        raw_time = (daily_hours * s["priority"] / total_priority) * pace_factor

       
        if s["difficulty"] >= 4:
            max_time = 1.0
        elif s["difficulty"] == 3:
            max_time = 1.5
        else:
            max_time = 2.0

        allocated_time = round(min(raw_time, max_time), 2)

        plan.append({
            "subject": s["name"],
            "allocated_hours": allocated_time,
            "difficulty": s["difficulty"],
            "confidence": s.get("confidence", 3),
            "deadline_days": s["deadline_days"]
        })

    return plan


def generate_multi_day_plan(data, days=3):
    """
    Generates a rolling multi-day plan WITHOUT mutating input data.
    This is important for correctness and reliability.
    """
    plans = {}

    
    working_data = copy.deepcopy(data)

    for day in range(1, days + 1):
        plans[f"Day {day}"] = generate_base_plan(working_data)

        for s in working_data["subjects"]:
            s["deadline_days"] = max(1, s["deadline_days"] - 1)

    return plans
