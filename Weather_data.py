import requests
import os
from datetime import datetime
import matplotlib.pyplot as plt

city_nm = "Kolhapur"
API_KEY = "" # Api key required to run code

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_nm}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Console output
    print("Weather:", data['weather'][0]['description'])
    print("Current Temperature:", data['main']['temp'], "°C")
    print("Feels Like:", data['main']['feels_like'], "°C")
    print("Humidity:", data['main']['humidity'], "%")

    # -----------------------------
    # 📊 Matplotlib Visualization
    # -----------------------------
    labels = ["Temperature (°C)", "Feels Like (°C)", "Humidity (%)"]
    values = [
        data['main']['temp'],
        data['main']['feels_like'],
        data['main']['humidity']
    ]

    plt.figure()
    plt.bar(labels, values)
    plt.title(f"Weather in {city_nm}")
    plt.xlabel("Weather Parameters")
    plt.ylabel("Values")
    plt.show()

else:
    print("Failed to fetch weather data")
    print(response.json())

