#GUI - mouse.py
from tkinter import *  #Lib: Tk Interface
from tkinter import ttk
import webbrowser
import pyautogui as pg


GUI = Tk()
GUI.geometry('500x300')

def Calender():
    pg.click(x=1868, y=1051)

B1 = Button(GUI,text='Calendar1',command=Calender)
B1.pack(ipadx=20,ipady=10,pady=20)

B2 = ttk.Button(GUI,text='Calendar2',command=Calender)
B2.pack(ipadx=20,ipady=10)

def Google():
    webbrowser.open('https://www.google.co.th/')

B3 = ttk.Button(GUI,text='Google',command=Google)
B3.pack(ipadx=20,ipady=10)


GUI.mainloop()