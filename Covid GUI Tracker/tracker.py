#import necessary modules

import pandas as pd
import requests
import bs4
import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

#funtion to get covid details from url: 'https://www.worldometers.info/coronavirus/'

def get_covid_data(): #funtion to get global case
    url = "https://www.worldometers.info/coronavirus/"
    page = requests.get(url).text
    bs = bs4.BeautifulSoup(page, 'html.parser')
    info_div = bs.find("div", class_= 'content-inner').findAll('div', id="maincounter-wrap")
    all_data = ""

    for block in info_div:
        text = block.find("h1", class_=None).get_text()
        count = block.find("span", class_=None).get_text()
        all_data = all_data + text + " " + count + "\n"

    return all_data

def get_country_data(): #funtion to get country wise details
    url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread'
    page = requests.get(url).content
    pf = pd.read_html(page)
    df = pf[0]


    tv1['column'] = list(df.columns)
    tv1['show'] = "headings"
    for column in tv1['columns']:
        tv1.heading(column, text=column)

    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("","end", values=row)

def reload():
    new_data = get_covid_data()
    mainlabel['text'] = new_data


#Creating tkinter GUI

root = tk.Tk()
root.geometry("900x700")
root.title("Covid Tracker")
f = ("poppins", 25, "bold")


img = Image.open('D:\GJ\Python\Game\Covid GUI Tracker\covid.png')
img = img.resize((100,100), Image.ANTIALIAS)
banner = ImageTk.PhotoImage(img)
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()

msg = tk.Label(root, text='Stay Home. Stay Safe!')
msg.config(bg='lightgreen')
msg.pack()

mainlabel = tk.Label(master=root, text=get_covid_data(), font=f)
mainlabel.pack()

textfield = tk.Entry(root, width = "50")
textfield.pack()

#frame for TreeView
frame1 = tk.LabelFrame(root, text="Country wise data")
frame1.place(height=550, width=900, rely=0.65, relx=0)


tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

#Adding buttons
button1 = tk.Button(master=root, text='Get Country wise data', relief='solid', command=get_country_data)
button1.pack()

button2 = tk.Button(root, text='Close', font=f, width=5, fg='red', command=root.destroy)
button2.place(relx = 1.0, rely = 0.0, anchor ='ne')

button3 = tk.Button(master=root, text='Reload', font=f, relief='solid', command=reload)
button3.pack()

root.mainloop()

#Run the file to open Covid-19 Tracker GUI
