import math

# -------------------------------
# VALIDATION
# -------------------------------
def validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0")

# -------------------------------
# STRIDE LENGTH
# -------------------------------
def calculate_stride_length(height_cm, activity):
    if activity == "walk":
        return (height_cm * 0.415) / 100
    else:  # running stride is longer
        return (height_cm * 0.65) / 100

# -------------------------------
# SPEED
# -------------------------------
def calculate_speed_kmh(stride_m, steps_per_min):
    meters_per_min = stride_m * steps_per_min
    return (meters_per_min * 60) / 1000

# -------------------------------
# MET INTERPOLATION
# -------------------------------
def estimate_met(speed_kmh, activity):
    if activity == "walk":
        # walking MET curve
        return 1.5 + (speed_kmh ** 1.2) / 2
    else:
        # running MET curve
        return 4 + (speed_kmh ** 1.05)

# -------------------------------
# CALORIE CALCULATION
# -------------------------------
def calories_per_minute(met, weight_kg):
    return (met * 3.5 * weight_kg) / 200

# -------------------------------
# MAIN LOGIC
# -------------------------------
def steps_to_burn_one_calorie(weight, height, steps_per_min, activity):
    validate_positive(weight, "Weight")
    validate_positive(height, "Height")
    validate_positive(steps_per_min, "Steps per minute")

    stride = calculate_stride_length(height, activity)
    speed = calculate_speed_kmh(stride, steps_per_min)
    met = estimate_met(speed, activity)
    cal_per_min = calories_per_minute(met, weight)

    steps_per_calorie = steps_per_min / cal_per_min

    return {
        "speed_kmh": round(speed, 2),
        "stride_m": round(stride, 3),
        "met": round(met, 2),
        "calories_per_min": round(cal_per_min, 2),
        "steps_per_calorie": round(steps_per_calorie)
    }

# -------------------------------
# USER INPUT
# -------------------------------
activity = input("Activity (walk/run): ").lower()
weight = float(input("Weight (kg): "))
height = float(input("Height (cm): "))
steps_per_min = int(input("Steps per minute: "))

results = steps_to_burn_one_calorie(weight, height, steps_per_min, activity)

# -------------------------------
# OUTPUT
# -------------------------------
print("\n--- PHYSIOLOGICAL ESTIMATE ---")
print(f"Activity: {activity.capitalize()}")
print(f"Speed: {results['speed_kmh']} km/h")
print(f"Stride length: {results['stride_m']} m")
print(f"MET value: {results['met']}")
print(f"Calories/min: {results['calories_per_min']}")
print(f"Steps to burn 1 calorie: {results['steps_per_calorie']}")
