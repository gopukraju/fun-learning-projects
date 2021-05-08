
# In[1]: Import required libraries


import requests
import bs4
import tkinter as tk
from PIL import Image
from PIL import ImageTk


# In[9]: Define functions to get data from the site: https://www.worldometers.info/coronavirus/



def get_html_data(url):
    data = requests.get(url)
    return data

def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_= 'content-inner').findAll('div', id="maincounter-wrap")
    all_data = ""

    for block in info_div:
        text = block.find("h1", class_=None).get_text()
        count = block.find("span", class_=None).get_text()
        all_data = all_data + text + " " + count + "\n"

    return all_data


get_covid_data()

# In[10]: Define reload button module

def reload():
    new_data = get_covid_data()
    mainlabel['text'] = new_data


# In[8]: Create GUI using Tkinter


root = tk.Tk()
root.geometry("900x700")
root.title("Covid Tracker")
f = ("poppins", 25, "bold")

img = Image.open('D:\GJ\Python\Game\Covid-19 Tracker\covid.png')
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

rbtn = tk.Button(master=root, text='Reload', font=f, relief='solid', command=reload)
rbtn.pack()

rbtn = tk.Button(root, text='Close', font=f, width=5, fg='red', command=root.destroy)
rbtn.place(relx = 1.0, rely = 0.0, anchor ='ne')

root.mainloop()


# In[ ]: Run file to see the global tracking of corona cases
