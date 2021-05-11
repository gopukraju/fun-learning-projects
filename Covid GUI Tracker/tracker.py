#import necesary libraries

import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


#Define URL and make request to fetch the raw HTML content

url = "https://www.worldometers.info/coronavirus/"
html_content = requests.get(url).text

#define the functions

#funtion to get global data
def get_covid_data():
    bs = bs4.BeautifulSoup(html_content, 'html.parser')
    info_div = bs.find("div", class_= 'content-inner').findAll('div', id="maincounter-wrap")
    all_data = ""

    for block in info_div:
        text = block.find("h1", class_=None).get_text()
        count = block.find("span", class_=None).get_text()
        all_data = all_data + text + " " + count + "\n"

    return all_data

 #funtion to get country wise data
def get_country_data():

    # Parse HTML code for the entire site
    soup = BeautifulSoup(html_content, "lxml")

    #getting the table from the site
    covid_table = soup.find("table", attrs={"id": "main_table_countries_today"})

    #the head will form our columns
    head = covid_table.thead.find_all("tr")

    headings = []
    for th in head[0].find_all("th"):
        # remove any newlines and extra spaces from left and right
        headings.append(th.text.replace("\n","").strip())

    body = covid_table.tbody.find_all("tr")

    #lets declare empty list data that will hold all rows data
    data = []
    for r in range(1,len(body)):
        row = [] # empty lsit to hold one row data
        for tr in body[r].find_all("td"):
            row.append(tr.text.replace("\n","").strip())
            #append row data to row after removing newlines escape and triming unnecesary spaces
        data.append(row) #data contains all the rows excluding header


    #We can now pass data into a pandas dataframe headings as the columns
    df = pd.DataFrame(data,columns=headings)

    # Data points with # value are the countries of the world while the data points with
    # null values for # columns are features like continents totals etc
    data = df[df["#"]!=""].reset_index(drop=True)

    data = data.drop_duplicates(subset = ["Country,Other"])
    #Reason to drop duplicates : Worldometer reports data for 3 days: today and 2 days back
    #I found out that removing duplicates removes the values for the best two days and keep today's

    #We can drop the following columns:
    cols = ['#',
 'Tot\xa0Cases/1M pop',
 'Deaths/1M pop',
 'Tests/1M pop',
 'Population',
 '1 Caseevery X ppl',
 '1 Deathevery X ppl',
 '1 Testevery X ppl',
 'New Cases/1M pop',
 'New Deaths/1M pop',
 'Active Cases/1M pop']

    df = data.drop(cols,axis=1)

    tv1['column'] = list(df.columns)
    tv1['show'] = "headings"
    for column in tv1['columns']:
        tv1.heading(column, text=column)

    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("","end", values=row)

#define reload funtion triggered on button press
def reload():
    new_data = get_covid_data()
    mainlabel['text'] = new_data


#Make tkinter GUI

root = tk.Tk()
root.geometry("900x700")
root.title("Covid Tracker")
f = ("poppins", 25, "bold")

#Upload necesary images
img = Image.open('D:\GJ\Python\Game\Covid GUI Tracker\covid.png')
img = img.resize((100,100), Image.ANTIALIAS)
banner = ImageTk.PhotoImage(img)
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()


img2 = Image.open('D:\GJ\Python\Game\Covid GUI Tracker\load.png')
img2 = img2.resize((80,80), Image.ANTIALIAS)
banner2 = ImageTk.PhotoImage(img2)

img3 = Image.open('D:\GJ\Python\Game\Covid GUI Tracker\close.png')
img3 = img3.resize((50,50), Image.ANTIALIAS)
banner3 = ImageTk.PhotoImage(img3)

#displaying message 'Stay Home. Stay Safe!'
msg = tk.Label(root, text='Stay Home. Stay Safe!')
msg.config(bg='lightgreen')
msg.pack()

#Define Label
mainlabel = tk.Label(master=root, text=get_covid_data(), font=f)
mainlabel.pack()


#frame for TreeView
frame1 = tk.LabelFrame(root, text="Country wise data")
frame1.place(height=250, width=900, rely=0.65, relx=0)

#Define TreeView
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

#Define necessary buttons
button1 = tk.Button(master=root, text='Get Country wise data', relief='solid', command=get_country_data)
button1.place(relx=0.43, rely=0.60)

button2 = tk.Button(root, image = banner3, command=root.destroy)
button2.place(relx = 1.0, rely = 0.0, anchor ='ne')

button3 = tk.Button(master=root, text='Reload', font='sans 11 bold', image = banner2, compound = 'top', command=reload)
button3.pack()

root.mainloop()

#Run the tracker.py file to open GUI with Covid 19 tracking data!
