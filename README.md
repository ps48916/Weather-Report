# Weather-Report

# Overview
This python program is use to tell the weather report of nearly every part of the world program uses the open weather API to show the weather report the is free to use.

# Modules
There are few pre built modules used in the program. It is highly recommended to Install these Modules before running program.
1. Jason
2. requests
3. tkinter

# Open Weather
Before Running the program do create an account on [openweathermap](https://www.openweathermap.org) and generate your API key and past it in the program in the API section

Replace **Paste your API here** with your **API** which you have Genearated on above site

```import tkinter as tk
import requests
import json
win=tk.Tk()
win.title("Weather")
win.geometry("500x200")

api="Paste Your API here"
