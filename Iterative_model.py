import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

def generate_weather_data(start, end, num_points, a, b, c, noise_factor=10):
    x = np.linspace(start, end, num_points)
    y = quadratic_model(x, a, b, c) + np.random.normal(0, noise_factor, num_points)
    return x, y

def plot_iteration(x, y, title):
    plt.scatter(x, y, label='Iteration Data')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.show()
    
a_values = [0.3, 0.4, 0.5]   # incrementing 'a' value
b, c = -5, 20

start_time, end_time, num_points = 0, 10, 100

for i, a in enumerate(a_values, 1):
    x_data, y_data = generate_weather_data(start_time, end_time, num_points, a, b, c)
    plot_iteration(x_data, y_data, f"Iterative Model - Iteration {i}")
    final_temp = y_data[-1]
    print(f"Iteration {i}: Final Temperature = {final_temp}")
