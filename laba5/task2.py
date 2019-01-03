import _thread
import time
from tkinter import *

root = Tk()
c = Canvas(root, width=500, height=500, bg="white")
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='green')


def motion():
    _thread.start_new_thread(innerMotion, ())


def innerMotion():
    fps = 500
    while c.coords(ball)[2] < 1000:
        timeStart = time.time()
        c.move(ball, 1, 0)
        timeEnd = time.time()
        delay = 1 / fps - (timeEnd - timeStart)
        time.sleep(delay if delay > 0 else 0)


motion()

root.mainloop()
