from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("376x800")
root.title("Chad Screen Recorder")
root.config(bg="black")
root.resizable(False, False)

# FUNCTIONS
def start_rec():
    file = Filename.get()
    rec.start_recording(str(file+" .mp4"), 12)

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()


rec = pyscreenrec.ScreenRecorder()

#icon
# image_icon = PhotoImage(file="")
# root.iconphoto(False, image_icon)

#background
# image_1 = PhotoImage(file="")
# Label(root, image = image_1,bg="#fff").place(x=2, y=31)

# image_2 = PhotoImage(file="")
# Label(root, image = image_2,bg="").place(x=51, y=311)

#heading
lbl = Label(root,text="Screen Recorder", bg="#fff", font="arial 17 bold" )
lbl.pack(pady = 15)

#entry
Filename = StringVar()
entry = Entry(root,textvariable=Filename, width=18, font="arial 17")
entry.place(x = 100, y=350)
Filename.set("recording12")

image_3 = PhotoImage(file="start.png")
Label(root, image="start.png", bd=0).pack(pady=22)

#buttons
start = Button(root,text="start", font="arial 22", bd = 0, command=start_rec)
start.place(x=123, y=233)


image_4 = PhotoImage(file ="resume.png",)
resume = Button(root, image="resume.png", bd=0, bg="#fff", command=resume_rec)
resume.place(x=50, y=450)

image_5 = PhotoImage(file ="pause.png",)
pause = Button(root, image="pause.png", bd=0, bg="#fff", command=pause_rec)
pause.place(x=70, y=450)

image_6 = PhotoImage(file ="stop.png",)
stop = Button(root, image="stop.png", bd=0, bg="#fff", command=stop_rec)
stop.place(x=90, y=450)

root.mainloop()