from tkinter import *
from tkinter import ttk
import requests

def data_get():
  city=city_name.get()
  data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=799e32c9c85c34ed372ed19cee083309").json()
  wc_label1.config(text=data["weather"][0]["main"])
  wd_label1.config(text=data["weather"][0]["description"])
  wt_label1.config(text=str(int(data["main"]["temp"]-273.15)))
  wp_label1.config(text=data["main"]["pressure"])
  wh_label1.config(text=data["main"]["humidity"])
  ww_label1.config(text=str(data["wind"]["speed"]))

win=Tk()
win.title("Weather App")
win.config(bg ="sky blue")
win.geometry("500x600")

name_label=Label(win,text="My Weather App",font=("Time New Roman",30,"bold"))

name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
combo_box=ttk.Combobox(win,values=list_name,font=("Time New Roman",10,"bold"),textvariable=city_name)
combo_box.place(x=100,y=120,height=30,width=300)


wc_label=Label(text="Weather Climate",font=("Time New Roman",10,"bold"))
wc_label.place(x=100,y=270,height=30,width=135)

wc_label1=Label(text=" ",font=("Time New Roman",10,"bold"))
wc_label1.place(x=270,y=270,height=30,width=130)


wd_label=Label(text="Weather Description",font=("Time New Roman",10,"bold"))
wd_label.place(x=100,y=310,height=30,width=135)

wd_label1=Label(text=" ",font=("Time New Roman",10,"bold"))
wd_label1.place(x=270,y=310,height=30,width=130)


wt_label=Label(text="Temperature",font=("Time New Roman",10,"bold"))
wt_label.place(x=100,y=350,height=30,width=135)


wt_label1=Label(text=" ",font=("Time New Roman",10,"bold"))
wt_label1.place(x=270,y=350,height=30,width=130)


wp_label=Label(text="Pressure",font=("Time New Roman",10,"bold"))
wp_label.place(x=100,y=390,height=30,width=135)

wp_label1=Label(text=" ",font=("Time New Roman",10,"bold"))
wp_label1.place(x=270,y=390,height=30,width=130)

wh_label=Label(text="Humidity",font=("Time New Roman",10,"bold"))
wh_label.place(x=100,y=430,height=30,width=135)

wh_label1=Label(text=" ",font=("Time New Roman",10,"bold"))
wh_label1.place(x=270,y=430,height=30,width=130)

ww_label=Label(text="Wind",font=("Time New Roman",10,"bold"))
ww_label.place(x=100,y=470,height=30,width=135)

ww_label1=Label(text=" ",font=("Time New Roman",10,"bold"))
ww_label1.place(x=270,y=470,height=30,width=130)



update_button=Button(win,text="Update",font=("Time New Roman",12,"bold"),command=data_get)
update_button.place(x=200,y=170,height=30,width=100)


win.mainloop()