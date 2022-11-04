from tkinter import *

ws = Tk()
ws.geometry("400x800")
ws.title('Pass-Buildozer')
ws.resizable(False, False)

backg = PhotoImage(file="/home/bhargav/My_projects/Screen_Recorder/welcome.png")
label1 = Label(image=backg)
label1.image = backg
label1.pack()

def nextPage():
    ws.destroy()
    import Mycode
    
# continue button
continue_img = PhotoImage(file="/home/bhargav/My_projects/Screen_Recorder/Lets_go.png")
continue1 = Button(ws, image=continue_img, text="Let's Go" ,bd=0, command=nextPage, bg="white")
continue1.place(x=110, y=725)

ws.mainloop()