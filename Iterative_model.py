import matplotlib.pyplot as plt
import numpy as np
import random

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

def generate_weather_data(start, end, num_points, a, b, c, noise_factor=10):
    x = np.linspace(start, end, num_points)
    y = quadratic_model(x, a, b, c) + np.random.normal(0, noise_factor, num_points)
    return x, y

def plot_sprint(x, y, sprint_num):
    plt.scatter(x, y, label=f'Sprint {sprint_num}')
    plt.title(f'Agile Model - Sprint {sprint_num}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.show()

# Agile approach: small increments (sprints)
start_time, end_time, num_points = 0, 10, 100
a, b, c = 0.5, -5, 20

for sprint in range(1, 4):  # simulate 3 sprints
    # each sprint tweaks coefficients slightly (like changing requirements)
    a += random.uniform(-0.05, 0.05)
    b += random.uniform(-0.2, 0.2)
    c += random.uniform(-0.5, 0.5)
    x_data, y_data = generate_weather_data(start_time, end_time, num_points, a, b, c)
    plot_sprint(x_data, y_data, sprint)
    print(f"Sprint {sprint}: Final Temperature = {y_data[-1]}")
