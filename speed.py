from tkinter import *
from tkinter import messagebox
import pyspeedtest

class SpeedTest:
    def __init__(self, App):
        self.window = App
        self.window.title("Kfs Speed Test")
        self.window.geometry("500x500")
        self.window.resizable(False, False) 
        self.filename = PhotoImage(file="C:\python\speedInternet\speedtest.png")
        self.background_label = Label(App,image=self.filename)
        self.background_label.place(x=0,y=0,relwidth=1,relheight=1)
        self.b = Button(App,text="Click here to see speed internet",font=("sans serif",20), bg="yellow", height=1,width=30, command=self.app )
        self.b.pack()

    def app(self):
        self.st = pyspeedtest.SpeedTest("www.google.com")
        self.a  = str(self.st.download()) + "[Bytes Per Second]" #you can use ping or upload with another function
        messagebox.showinfo("Your Download Speed",self.a)




top = Tk()
MyApp = SpeedTest(top)
top.mainloop()
