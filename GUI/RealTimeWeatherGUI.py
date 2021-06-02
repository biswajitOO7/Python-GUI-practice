from tkinter import * 
from tkinter import messagebox

def tell_weather() :
    import requests, json
    api_key = "6fb346b973f68ff543c00d1172998dff"
  
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_field.get()
    complete_url = base_url + "appid=" + api_key+ "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    print(complete_url)
    print(x)

    if x["cod"] != "404" :
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        temp_field.insert(15, str(current_temperature) + " Kelvin")
        atm_field.insert(10, str(current_pressure) + " hPa")
        humid_field.insert(15, str(current_humidiy) + " %")
        desc_field.insert(10, str(weather_description) )

    else :
  

        messagebox.showerror("Error", "City Not Found \n"
                             "Please enter valid city name")
  
        city_field.delete(0, END)


def clear_all() : 
    city_field.delete(0, END)  
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)
  
    # set focus on the city_field entry box 
    city_field.focus_set()


if __name__ == "__main__" :
    root = Tk()
    root.title("Gui Application")
    root.configure(background = "light green")
    root.geometry("425x175")
    headlabel = Label(root, text = "Weather Gui Application",fg = 'black', bg = 'red')
    # Create a City name : label
    label1 = Label(root, text = "City name : ",fg = 'black', bg = 'dark green')
    # Create a City name : label
    label2 = Label(root, text = "Temperature :",
                   fg = 'black', bg = 'dark green')
  
    # Create a atm pressure : label
    label3 = Label(root, text = "atm pressure :",
                   fg = 'black', bg = 'dark green')
  
    # Create a humidity : label
    label4 = Label(root, text = "humidity :",
                   fg = 'black', bg = 'dark green')
  
    # Create a description :label
    label5 = Label(root, text = "description  :",
                   fg = 'black', bg = 'dark green')
    
    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 1, column = 0, sticky ="E") 
    label2.grid(row = 3, column = 0, sticky ="E") 
    label3.grid(row = 4, column = 0, sticky ="E") 
    label4.grid(row = 5, column = 0, sticky ="E") 
    label5.grid(row = 6, column = 0, sticky ="E")

    city_field = Entry(root) 
    temp_field = Entry(root) 
    atm_field = Entry(root) 
    humid_field = Entry(root) 
    desc_field = Entry(root)

    city_field.grid(row = 1, column = 1, ipadx ="100") 
    temp_field.grid(row = 3, column = 1, ipadx ="100") 
    atm_field.grid(row = 4, column = 1, ipadx ="100") 
    humid_field.grid(row = 5, column = 1, ipadx ="100") 
    desc_field.grid(row = 6, column = 1, ipadx ="100")



    button1 = Button(root, text = "Submit", bg = "red", 
                     fg = "black", command = tell_weather)

    
    button1.grid(row = 2, column = 1)

    button2 = Button(root, text = "Clear", bg = "red", 
                     fg = "black", command = clear_all)
    button2.grid(row = 7, column = 1)


    root.mainloop()