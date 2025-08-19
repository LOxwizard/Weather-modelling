import numpy as np
import matplotlib.pyplot as plt

# Base model coefficients
a_base = -0.2
b_base = 1.5
c_base = 24

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

# Simple version for a single time input
def quadratic_weather_model(time):
    return quadratic_model(time, a_base, b_base, c_base)

# ==== TEXT OUTPUTS ====
print("=== WATERFALL MODE ===")
for hour in range(0, 25, 6):
    temp = quadratic_weather_model(hour)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")

print("\n=== ITERATIVE MODE ===")
for iteration in range(1, 4):
    print(f"Iteration {iteration}:")
    for hour in range(0, 25, 12):
        temp = quadratic_weather_model(hour)
        print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
    print("---")

print("\n=== AGILE MODE ===")
times_to_check = [0, 6, 12, 18, 24]
for sprint in range(1, 3):
    print(f"Sprint {sprint}:")
    for t in times_to_check:
        temp = quadratic_weather_model(t)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    print("---")

# ==== GRAPHICAL PLOTS ====
x = np.linspace(0, 30, 100)

# -- Plot 1: Base Model --
y = quadratic_model(x, a_base, b_base, c_base)
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', marker='o', markersize=3, label=f'T = {a_base}x² + {b_base}x + {c_base}')
plt.title("Weather Modeling (Quadratic Model)")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# -- Plot 2: Iterative Model --
iterations = [
    (a_base, b_base, c_base),
    (a_base - 0.05, b_base + 0.3, c_base),
    (a_base - 0.1, b_base + 0.6, c_base)
]

plt.figure(figsize=(8, 5))
for i, (a, b, c) in enumerate(iterations, 1):
    y_iter = quadratic_model(x, a, b, c)
    plt.plot(x, y_iter, label=f"Iteration {i}")
plt.title("Iterative Model Weather Curve")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# -- Plot 3: Agile Model --
sprints = [
    (a_base, b_base, c_base),
    (a_base - 0.02, b_base + 0.1, c_base),
    (a_base - 0.04, b_base + 0.2, c_base),
    (a_base - 0.06, b_base + 0.3, c_base)
]

plt.figure(figsize=(8, 5))
for i, (a, b, c) in enumerate(sprints, 1):
    y_sprint = quadratic_model(x, a, b, c)
    plt.plot(x, y_sprint, label=f"Sprint {i}")
plt.title("Agile Model Weather Curve")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
