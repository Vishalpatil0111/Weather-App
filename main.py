import tkinter as tk

import params as params
import requests
from PIL import Image, ImageTk

root = tk.Tk()

root.title("weather app")
root.geometry('600x400')

def format_response(weather):
    try:
         city=weather['name']
         condition=weather['weather'][0]['description']
         temp=weather['main']['temp']
         final_str='city:%s\nCondition:%s\nTemperature:%s'%(city,condition,temp)
    except:
        final_str='there was a problem in retriving information '

    return final_str


def get_weather(city):
    weather_key = 'c09faddcd390bb351e23e0a4942622cb'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url,params)
    #print(response.json())
    weather=response.json()


    #print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])

    result['text']=format_response(weather)

img = Image.open('./background-3268840_1920.jpg')
img = img.resize((600, 400), Image.LANCZOS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=400)

heading_title = tk.Label(bg_lbl, text='get weather now !!', fg='red', bg='light yellow',
                         font=('times new roman', 17, 'bold'))
heading_title.place(x=80, y=18)

frame_one = tk.Frame(bg_lbl, bg="#42c2f4", bd=5)
frame_one.place(x=80, y=50, width=450, height=48)

txt_box = tk.Entry(frame_one, font=('times new roman', 25), width=16)
txt_box.grid(row=0, column=0, sticky='w')

btn = tk.Button(frame_one, text='get weather', fg='green', font=('times new roman', 16, 'bold'), command=lambda:get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

frame_two = tk.Frame(bg_lbl, bg="#42c2f4", bd=5)
frame_two.place(x=80, y=100, width=450, height=280)

result = tk.Label(frame_two, font=40, bg='white',justify='left',anchor='nw')
result.place(relwidth=1, relheight=1)





root.mainloop()
