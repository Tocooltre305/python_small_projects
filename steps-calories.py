import math

class MetabolicCalculator:
    def __init__(self):
        self.speeds_met = {2.0: 2.0, 3.0: 2.8, 4.0: 3.5, 5.0: 4.3, 6.0: 5.0, 7.0: 7.0}

    def get_stride_length(self, height_cm, gender):
        return height_cm * 0.415 if gender == 'm' else height_cm * 0.413

    def get_bmr(self, weight, height, age, gender):
        s = 5 if gender == 'm' else -161
        return (10 * weight) + (6.25 * height) - (5 * age) + s

    def run(self):
        print("--- Professional Biometric Step Analyzer ---")
        try:
            w = float(input("Weight (kg): "))
            h = float(input("Height (cm): "))
            a = int(input("Age: "))
            g = input("Gender (m/f): ").lower()
            v = float(input("Speed (km/h): "))

            bmr_per_min = self.get_bmr(w, h, a, g) / 1440
            
            closest_speed = min(self.speeds_met.keys(), key=lambda x: abs(x - v))
            met_value = self.speeds_met[closest_speed]
            
            cal_per_min_activity = (met_value * 3.5 * w) / 200
            total_cal_per_min = cal_per_min_activity + bmr_per_min
            
            stride_m = self.get_stride_length(h, g) / 100
            dist_per_min_m = (v * 1000) / 60
            steps_per_min = dist_per_min_m / stride_m
            
            steps_per_cal = steps_per_min / total_cal_per_min
            cal_per_step = 1 / steps_per_cal

            print(f"\n{' METRICS ':=^30}")
            print(f"BMR (Resting): {bmr_per_min * 60:.2f} kcal/hr")
            print(f"Active Burn: {cal_per_min_activity * 60:.2f} kcal/hr")
            print(f"Stride Length: {stride_m:.2f} m")
            print(f"Steps/Minute: {steps_per_min:.0f}")
            print(f"{' RESULT ':=^30}")
            print(f"1 Calorie = {steps_per_cal:.2f} steps")
            print(f"1 Step = {cal_per_step:.5f} kcal")
            print(f"{'='*30}")

        except ValueError:
            print("Error: Please enter numeric values only.")

if __name__ == "__main__":
    app = MetabolicCalculator()
    app.run()