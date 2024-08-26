import requests
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Weather App")
API_KEY = "My API key"

# Function to center the window on the screen
def center_window():
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate the position to center the window
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 280
    x = (screen_width/2) - (WINDOW_WIDTH/2)
    y = (screen_height/2) - (WINDOW_HEIGHT/2)

    root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, x, y))
center_window()

# Some padding in the window
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)

# Main header
titel_label = tk.Label(main_frame,text="Weather App",font=("Arial", 20))
titel_label.pack(pady=(0, 2))

# Dev tag
tag_label = tk.Label(main_frame, text="Build by: @jonaisadesigner", font=("Arial", 8))
tag_label.pack(pady=(0, 13))

# Header
city_label = tk.Label(main_frame, text="Enter your city:")
city_label.pack(pady=(0, 5))

city_entry = tk.Entry(main_frame)
city_entry.pack(pady=(0, 10))

# Funtion to get the weather, and display the result in the tkinter window.
def get_weather():
    # Captalize the city name
    city = city_entry.get().capitalize()

    # the acutal call to the API
    weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}")

    # Some logic to check for errrors.
    # If the city is not found, an error message will be displayed.
    if weather_data.json()['cod'] == '404':
        messagebox.showerror("Error", "No City Found")

    # If the city is found, the weather will be displayed.
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        result_label.config(text=f"The weather in {city}:\n Type of weather: {weather} \nTemperature is: {temp}°C")

# Button, when pushed, the weather will be displayed. Using the get_weather function.
submit_button = tk.Button(main_frame, text="See the Weather", command=get_weather)
submit_button.pack(pady=(0, 10))

result_label = tk.Label(main_frame, text="", wraplength=250)
result_label.pack(pady=(0, 10))

# Run the whole program
root.mainloop()