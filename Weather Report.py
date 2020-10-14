import tkinter as tk
import requests
import json
win=tk.Tk()
win.title("Weather")
win.geometry("500x200")

api="06f72727914c5abb0ce4248abd1d1ceb"
url="http://api.openweathermap.org/data/2.5/weather?"

def weather():
    location= entry.get()
    answer = url+"q=" +location+ "&appid=" + api
    response= requests.get(answer)
    res= response.json()
    if res["cod"] != "404":
        x= res["main"]
        temperature= x["temp"]
        pressure= x["pressure"]
        humidity= x["humidity"]
        y= res["weather"]
        weather_description=y[0]["description"]
        label= tk.Label(win,text=f'Temperature(In kelvin unit)= {temperature},\n'
                                 f'Atmospheric Pressure(In hPa unit)= {pressure},\n'
                                 f'Humidity(In percentage)= {humidity},\n'
                                 f'Description= {weather_description}')
        label.grid(row=2,column=0)
    else:
        label2=tk.Label(win,text="Enter Correct City")
        label2.grid(row=2,column=0)

label=tk.Label(win,text="Enter City Name Here: ",bg='#add8e6')
label.grid(row=0,column=0)
label.config(fon=("times",20,"bold"))

entry=tk.Entry(win)
entry.grid(row=1,column=0,padx=100)

button= tk.Button(win,text="Search", command=weather)
button.grid(row=1,column=1)

win.mainloop()
