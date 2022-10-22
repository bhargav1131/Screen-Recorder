from tkinter import *
import tkinter.messagebox
from tkinter import font
import pyscreenrec
from PIL import Image, ImageTk

root = Tk()
root.geometry("410x808")
root.title("Chad Screen Recorder")
root.config(bg="black")
root.resizable(False, False)
back = PhotoImage(file="background.png")
label1 = Label(image=back)
label1.image = back
label1.pack()

# ____________________________________________________________________


# ____________________________________________________________________
# FUNCTIONS
def start_rec():
    file = Filename.get()
    rec.start_recording(str(file+" .mp4"), 9)
    tkinter.messagebox.showinfo("Started..")


def pause_rec():
    rec.pause_recording()
    tkinter.messagebox.showinfo("Paused..")


def resume_rec():
    rec.resume_recording()
    tkinter.messagebox.showinfo("Resume..")


def stop_rec():
    rec.stop_recording()
    tkinter.messagebox.showinfo("Stopped..")

# ____________________________________________________________________


# entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=20, font=(
    "Lucida Console", 12),  bg="#EFF2F0", bd=0, selectborderwidth=0)
entry.place(x=70, y=700)
Filename.set("            File Name")

rec = pyscreenrec.ScreenRecorder()
# icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# ____________________________________________________________________


Button(root, text="Start", command=start_rec,
       bd=0, bg="#EFF2F0"). place(x=78, y=275)

Button(root, text="Resume", command=resume_rec, bd=0,
       bg="#EFF2F0", relief=RIDGE). place(x=240, y=275)

Button(root, text="Pause", command=pause_rec,
       bd=0, bg="#EFF2F0"). place(x=78, y=443)

Button(root, text="Stop", command=stop_rec,
       bd=0, bg="#EFF2F0"). place(x=255, y=443)


def callback():
    pass

# Button(root, text="Demo Button", command=callback, bd=0, bg="#EFF2F0"). place(x=260, y=600)


root.mainloop()
