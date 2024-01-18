##############################################  REALbot version 3.0  #############################################

"""
TO DO:
1 -> voice recognition ------->
2 -> use the camera too! ----->
"""
"""
This is the main file!
** ALL the GUI related stuff are here
** This handles the user
"""

import threading
import tkinter as tk
import winsound as sound
from datetime import datetime
import pyttsx3
import random
import features

engine = pyttsx3.init() # creating object

# say the output
def speak(say):
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(say)
    engine.runAndWait()

# seperation operator to use when splitting a string
sep_operator = ":"

# making a window and naming it
window = tk.Tk()
window.title("REALbot v3.0")
# nice sound created by looping
hertz = 100
while hertz < 1600:
    sound.Beep(hertz, 250)
    hertz += 100
print("REALbot started!")

# nicely prints the text to the window
def TKtxt(*args):
    # concatenate the args into a string
    message = ""
    for arg in args:
        message += arg

    txt = tk.Text(window, bg="#17202A", fg="#FFEEEE", font="Arial", width=60)
    txt.grid(row=0,column=0,columnspan=2)
    txt.insert(tk.END, "\n" + "REALbot ➡️ \n" + message)
    say_it = threading.Thread(target=speak, args=(message,))
    say_it.start()

# wish the author of REALbot on his b'day
today = datetime.now().strftime("%m/%d")
if today == "02/27":
    TKtxt("Today is my creator's B'day!!!🎂")

# begin to chat
TKtxt("""Hello!, how can I help you?
if you are new enter 'help'😊""")

# format the input and gives a reply to the user
def send():
    # doesn't work
    """
    display_sent = "You ➡️ " + inField.get()
    TKtxt(display_sent)
    """
    user = inField.get().lower().strip()

    # tree of replies
    match user:
        case "help":
            TKtxt("""This is REALbot 3.0\nI'm here to assist you and make you happy!
            Available commands:
            \tsing a song\n\ttell me a joke\n\ttoss a coin\n\tweather:{city}\n\twikipedia:{somethig}\n\topen:{website}\n\tquit\n""")
        
        case "sing a song":
            TKtxt("Mary had a little lamb, little lamb...")
        
        case "tell me a joke":
            TKtxt(random.choice(["blah blah",
                               "Where do frogs keep there money?\n\tIn the river bank!",
                               "What did the buffalo say when his son left for college?\n\tBison"]))
        
        case "toss a coin":
            TKtxt(random.choice(["Heads", "Tales"]))
        
        case user if "weather" in user:
            key_w, place = user.split(sep_operator)
            weather = features.get_weather(place, "LK")
            if weather == "Error occured when getting weather information!":
                TKtxt("Sorry, an error occured when getting weather information")
            else:
                TKtxt(f"""\tTemperature: ", {weather[0]}°C
                Humidity: ", {weather[1]}%
                Weather: ", {weather[2]}""")
        
        case user if "wikipedia" in user:
            key_wiki, thing = user.split(sep_operator)
            TKtxt(features.get_wikiSummary(thing))
        
        case user if "open" in user:
            key_open, site = user.split(sep_operator)
            features.website(site)

        case "quit" | "bye":
            TKtxt("Ok then bye, hope you enjoyed!👋")
        
        case _:
            TKtxt("Sorry I didn't understand that!😔")

    # clean the input field
    inField.delete(0, tk.END)

# make an input field
inField = tk.Entry(window, width=50, bg="#9999AA", font="Helvetica 13")
inField.grid(row=1,column=0)
send = tk.Button(window, text="SEND", font="ArialBold", bg="#00FF00", command=send).grid(row=1,column=1)

# this loops forever
window.mainloop()

# when the window is closed
# nice sound created by looping
hertz = 1600
while hertz > 100:
    sound.Beep(hertz, 250)
    hertz -= 100
print("REALbot closed!")