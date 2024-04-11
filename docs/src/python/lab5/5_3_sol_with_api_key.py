# Υλοποίηση από τον Γιάννη Ροδουσάκη, φοιτητή του Τμήματος Πληροφορικής και Τηλεπικοινωνιών του Παν. Ιωαννίνων (5/5/2022)

import calendar
import datetime
from tkinter import *

import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


def plot():
    # Enter your API key
    api_key = "ΣΥΜΠΛΗΡΩΣΤΕ ΤΟ ΔΙΚΟ ΣΑΣ API ΚΛΕΙΔΙ ΕΔΩ"

    # Set geographical coordinates (latitude, longitude)
    lat = latitude_entry.get()
    lon = longitude_entry.get()

    date_time = datetime.datetime.now() - datetime.timedelta(days=5)
    utc_time = calendar.timegm(date_time.utctimetuple())

    temperatures = []
    timezone = ""
    dates = []

    for _ in range(5):
        temp_date = str(date_time).split(" ")[0]
        temp_date = temp_date.split("-")
        dates.append(temp_date[2] + "/" + temp_date[1] + "/" + temp_date[0])

        # API url
        weather_url = (
            "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat="
            + lat
            + "&lon="
            + lon
            + "&units=metric&dt="
            + str(utc_time)
            + "&appid="
            + api_key
        )

        # Get the response from weather url
        response = requests.get(weather_url)

        # Response will be in json format and we need to change it to pythonic format
        weather_data = response.json()

        if timezone == "":
            timezone = weather_data["timezone"]

        for i in range(24):
            temp = int(weather_data["hourly"][i]["temp"])
            temperatures.append(temp)

        date_time = date_time + datetime.timedelta(days=1)
        utc_time = calendar.timegm(date_time.utctimetuple())

    temp_date = str(date_time).split(" ")[0]
    temp_date = temp_date.split("-")
    dates.append(temp_date[2] + "/" + temp_date[1] + "/" + temp_date[0])

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 5), dpi=100)

    plot1 = fig.add_subplot(111)

    plot1.plot(temperatures)
    plot1.set_title(f"Temperature in {lat=} {lon=}")
    plot1.set_ylabel("Temperature (°C)")
    plot1.set_xticks([0, 24, 48, 72, 96, 120])
    plot1.set_xticklabels(dates)

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, plot_frame)
    toolbar.update()

    canvas.get_tk_widget().pack()


window = Tk()
window.title("Plotting Temperature in Tkinter for the past 5 days")
window.geometry("1000x500")

frame = Frame(window)
frame.pack()

plot_frame = Frame(window)
plot_frame.pack(side=BOTTOM)

Label(frame, text="Latitude").grid(row=0, sticky="w")
Label(frame, text="Longitude").grid(row=1, sticky="w")

default_lat = StringVar(window, value="39.1606")
default_lon = StringVar(window, value="20.9853")

latitude_entry = Entry(frame, textvariable=default_lat)
longitude_entry = Entry(frame, textvariable=default_lon)

latitude_entry.grid(row=0, column=1, sticky="w")
longitude_entry.grid(row=1, column=1, sticky="w")

plot_button = Button(master=frame, command=plot, height=2, width=10, text="Plot")
plot_button.grid(row=2, column=0, columnspan=2, sticky="news")

if __name__ == "__main__":
    window.mainloop()
