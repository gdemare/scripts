# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
import yt_dlp

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("200x200")


# function to open a new window
# on a button click
class dwd():
     
    def __init__(self, ):
         if 1==1:
            print("prout")

        

Label(master, text ="Download").grid(row=1)
url = Entry(master)
url.grid(row=2)
Button(master, text ="youtube MP3",command = dwd("ytmp3")).grid(row=3)
Button(master, text ="youtube vidéo",command = dwd("ytvideo")).grid(row=4)


# mainloop, runs infinitely
mainloop()
