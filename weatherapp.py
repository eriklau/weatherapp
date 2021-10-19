from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests


url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


config_file = "key.ini"
key = ConfigParser()
key.read(config_file)
api_key = key["api_key"]["key"]



def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()

        city = json["name"]
        country = json["sys"]["country"]
        temperature_kelvin = json["main"]["temp"]
        temperature_celsius = int(temperature_kelvin - 273.15)

        icon = json["weather"][0]["icon"]
        
        weather = json["weather"][0]["main"]


        all = (city, country, temperature_celsius, icon, weather)
        print("all", all)
        return all
    else:
        return None

print(get_weather("Toronto"))

def search():
    global img
    city = city_text.get()
    weather = get_weather(city)
    print(weather)
    if weather:
        location["text"] = "{}, {}".format(weather[0], weather[1])
        img["file"] = 'C:\\Users\\Larkin\\Desktop\\python\\weather_icons\\{}.png'.format(weather[3])
        # image["bitmap"] = "weather_icons/{}.png".format(weather[3])
        temperature["text"] = "{:.2f}°C".format(weather[2])
        weathers["text"] = weather[4]
    else:
        messagebox.showerror("Error", "City Not Found".format(city))



app = Tk()
app.title("Weather")
app.geometry("1280x720")
app["bg"] = "gray"

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_button = Button(app, text="Search", width=12, command=search)
search_button.pack()

location = Label(app, text="ENTER LOCATION", font=("Arial", "24", "bold italic"))
location.pack()


img = PhotoImage(file= "") 
Image = Label(app, image = img)
Image.pack()

# image = Label(app, bitmap='')
# image.pack()

temperature = Label(app, text="")
temperature.pack()

weathers = Label(app, text="")
weathers.pack()



app.mainloop()
