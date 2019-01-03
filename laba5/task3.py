import _thread
import time
from tkinter import *

root = Tk()
c = Canvas(root, width=500, height=500, bg="white")
c.pack()

red = c.create_oval(30, 100,130, 200, fill='black')
yellow = c.create_oval(30, 210, 130, 310, fill='black')
green = c.create_oval(30, 320, 130, 420, fill='black')


def main():
    _thread.start_new_thread(innerMotion, ())


def innerMotion():
    fps = 60
    trafficLightStartTime = time.time()
    while True:
        frameTimeStart = time.time()
        trafficLightTime = frameTimeStart - trafficLightStartTime
        if 0 < trafficLightTime % 3 < 1:
            print("red")
            c.itemconfig(red, fill="red")
            c.itemconfig(yellow, fill="black")
            c.itemconfig(green, fill="black")
        if 1 < trafficLightTime % 3 < 2:
            print("Yellow")
            c.itemconfig(red, fill="black")
            c.itemconfig(yellow, fill="yellow")
            c.itemconfig(green, fill="black")
        if 2 < trafficLightTime % 3 < 3:
            print("green")
            c.itemconfig(red, fill="black")
            c.itemconfig(yellow, fill="black")
            c.itemconfig(green, fill="green")

        frameTimeEnd = time.time()
        delay = 1 / fps - (frameTimeEnd - frameTimeStart)
        time.sleep(delay if delay > 0 else 0)


main()

root.mainloop()
