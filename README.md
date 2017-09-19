# TweetBox
note, the name changed after this was written. The documentation refers to it being Photobooth, but on github and on our blog it refers to TweetBox. I mean, it's basically a photobooth script. - NotTheAuthor.

An automated tweet system tied to a camera for documentation of physical projects.

The PhotoBooth is a python script that will capture, display, and tweet with a press of a button.

To make sure the the script runs properly you will need to install a few things to get the script to run properly.

Run these commands to install the necessary components.

Tweepy:

sudo apt-get update
sudo apt-get install python-dev python-pip
sudo pip install tweepy

Tkinter:

Tkinter should come with python, but if not run:

sudo apt-get install python-tk

PIL:

sudo pip install pil 
-or-
sudo pip install pillow

Twitter application:

To use the script you need to create a Twitter application.
Go to apps.twitter.com to create a new application.
Once the application is created you will need to add the Consumer Key, Consumer Secret, Access Token, and Access Token Secret.
These can be found under Keys and Access Tokens tab. Make sure to create Access token if you have not already done so.
The section to put in the keys will be in the tweet method of the script.


Once these components are installed, run the script from terminal using "python3 PhotoBooth.py"

The script will loop back to the camera once the picture was uploaded. To exit standard keyboard interrupt will exit it.
