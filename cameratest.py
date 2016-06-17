#!/user/bin/env python3

#use sudo ln -sf /usr/bin/python3.4 /usr/bin/python
#changing the default python

import tweepy  
from subprocess import call  
from datetime import datetime 
import picamera
import time
from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO
from PIL import Image, ImageTk



def my_callback(channel):
    global pressed
    pressed = True
def showPreview(): 
    
    root.title("Add a caption")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    root.update_idletasks()
    w=mainframe.winfo_screenwidth()
    h=mainframe.winfo_screenheight()
    size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    root.geometry("%dx%d+%d+%d" % (920, 580, x-100, y-100))

    mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    #img = Image(file = filePath, imgtype = ".png")
    img = Image.open(filePath)
    img.thumbnail((800,600), Image.ANTIALIAS)
    newimg = ImageTk.PhotoImage(img)
    ttk.Label(mainframe, image = newimg).grid(column = 0, row = 1,sticky=W)
    
    captionBox = ttk.Entry(mainframe, width=40, textvariable=caption)
    captionBox.grid(column=0, row=3, sticky=(W,E))

    ttk.Label(mainframe, text="Add a caption for the tweet!").grid(column=0, row=2, sticky=W)
    ttk.Button(root, text="Tweet", command = tweet).grid(column=3, row=3, sticky=W)
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    captionBox.focus()

    root.bind('<Return>', tweet)
    root.protocol("WM_DELETE_WINDOW", onClose)

    root.mainloop()
    
def onClose():
    root.destroy()
    GPIO.cleanup()
    global exit1
    exit1 = True
def tweet(*args):
    i = datetime.now()               #take time and date for filename  
    now = i.strftime('%Y%m%d-%H%M%S')
      
    # Consumer keys and access tokens, used for OAuth  
    consumer_key = 'dtm5F7BJiX2QT57puB0BH1B4L'  
    consumer_secret = 'hOakLciU75EmvTEnZyg1S3vhu9xKWlglBBRxrwSbjp9bezLu1K'  
    access_token = '502556048-MCi4nOgMjwDg8TObzdmyZKYUhKLU4PHD7X9BFBnJ'  
    access_token_secret = 'E5wIw3Av3XlOKwPIn4jKlLJIuLx5OYEmSb4mEiZYk5Al0'  
      
    # OAuth process, using the keys and tokens  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
    auth.set_access_token(access_token, access_token_secret)  
       
    # Creation of the actual interface, using authentication  
    api = tweepy.API(auth)  
      
    # Send the tweet with photo  
        
    api.update_with_media(filePath, status=caption.get())
    root.destroy()
    print(caption.get())
    
GPIO.setmode(GPIO.BCM)
button1_pin = 18
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
exit1 = False
while not exit1:
    pressed = False
    fileName = 'pic2.jpg'
    filePath = "/home/pi/Desktop/" + fileName
    root = Tk()
    caption = StringVar()
    with picamera.PiCamera() as camera:
        camera.resoution = (1920, 1080)
        camera.start_preview()
        GPIO.wait_for_edge(button1_pin, GPIO.FALLING, bouncetime = 500)
        camera.stop_preview();
        camera.capture(fileName)
        showPreview()
