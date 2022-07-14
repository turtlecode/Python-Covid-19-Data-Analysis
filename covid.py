from tkinter import *
import requests
from bs4 import BeautifulSoup

country = "india"

page2 = requests.get('https://www.worldometers.info/coronavirus/')

Soup2 = BeautifulSoup(page2.content, 'html.parser')

info2 = Soup2.find_all(class_="maincounter-number")

root = Tk()
root.title("Corona Report")
root.geometry("400x550")
font = ('Helvetica', 12, "bold")

def btn_click():
  country = c.get()
  page = requests.get('https://www.worldometers.info/coronavirus/country/' + country)
  Soup = BeautifulSoup(page.content, 'html.parser')
  info = Soup.find_all(class_='maincounter-number')

  a = [items.get_text() for items in info]
  ccd = Label(root,font=font, text=country + "Cases Of Corona")
  ccd.pack()
  cc = Label(root,font=font,text=a[0])
  cc.pack()

  ccd = Label(root,font=font, text=country + "Cases Of Deaths")
  ccd.pack()
  cd = Label(root,font=font,text=a[1])
  cd.pack()

  ccd = Label(root,font=font, text=country + "Cases Of Recovered")
  ccd.pack()
  cr = Label(root,font=font,text=a[2])
  cr.pack()

b = [items.get_text() for items in info2]

wc = Label(root,font=font,text="World Cases Of Corona")
wc.pack()
wc = Label(root,font=font,text=b[0])
wc.pack()

wc = Label(root,font=font,text="World Cases Of Death")
wc.pack()
wc = Label(root,font=font,text=b[1])
wc.pack()

wc = Label(root,font=font,text="World Cases Of Recovered")
wc.pack()
wc = Label(root,font=font,text=b[2])
wc.pack()

wc = Label(root,font=font,text="Enter Country Name")
wc.pack()
c = Entry(root,font=font)
c.pack()

sendBtn = Button(root, text="Find", command=btn_click, bg="green")
sendBtn.pack()

root.mainloop()