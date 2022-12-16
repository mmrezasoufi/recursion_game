# import libraries
from tkinter import *
from tkinter import messagebox
import winsound

# define a func to choose starter player
def choose_starter1():
    global choose
    winsound.PlaySound('turn.wav', winsound.SND_FILENAME)
    canvas.itemconfig(starter1, text='player1')
    choose = True
def choose_starter2():
    global choose
    winsound.PlaySound('turn.wav', winsound.SND_FILENAME)
    canvas.itemconfig(starter1, text='player2')
    choose = False
# defult player1 is starter
choose = True

# menu_info
def show_info():
    messagebox.showinfo("Info", "developed by Soufi and Vatankhah")

# message box ready for game
def close():
    winsound.PlaySound('click.wav', winsound.SND_FILENAME)
    msg = messagebox.askyesno("Ready ?", "Did you read the rules correctly? \n  Are you ready ?")
    if msg:
        tk.destroy()
def no() :
    winsound.PlaySound('click.wav', winsound.SND_FILENAME)

# create an instanceof tkinter frame or window
tk = Tk()
tk.geometry('563x560')
tk.resizable(width=False,height=False)
# background
background = PhotoImage(file='image.png')
canvas = Canvas(tk)
canvas.pack(fill=BOTH,expand=True)
canvas.create_image(0, 0, image=background, anchor="nw")
# line rules
canvas.create_text(205, 130, text='''                                  This game has some rules ; please pay attention ! 
                                  
                                  1) You are player1 and your beads can move from up to down 
                                  ... and your oponent from left to right
                                  2) If the next house of your bead is full, it jumps twice
                                  3) If the next two houses have a full bead, that bead will be locked
                                  4) If your three beads are locked, you miss your turn until you can make one move !
                                  
                                  ... This game is vocal, please turn up the volume on your system to the end''' )

# Selection section of the game starter
canvas.create_text(230,260 , text="Which player do you want to start ?",font=('Helvetica','10','bold','italic'))
button3 = Button(tk, text="We", bd=3, command=choose_starter1)
button4 = Button(tk, text="our oponent", bd=3, command=choose_starter2)
button3_canvas = canvas.create_window(260, 290, anchor="nw", window=button3)
button4_canvas = canvas.create_window(260, 315, anchor="nw", window=button4)
canvas.create_text(173, 355, text="starter :", font=('Helvetica', '10', 'bold', 'italic'))
starter1 = canvas.create_text(222, 355, text="player1", font=('Helvetica', '10', 'bold', 'italic'))


# Player readiness section
canvas.create_text(205, 400, text="Are you ready for game ?",font=('Helvetica', '10', 'bold', 'italic'))
button1 = Button(tk, text="Yes ☻", bd=3, command=close)
button2 = Button(tk, text="no ☺", bd=3, command=no)
button1_canvas = canvas.create_window(260, 420,anchor="nw", window=button1)
button2_canvas = canvas.create_window(260, 450, anchor="nw", window=button2)


# menu
menubar = Menu(tk)
menubar.add_command(label="Info", command=show_info)
tk.config(menu=menubar)

# mainloop
tk.mainloop()

# for send turn from tkinter to game
if choose:
    turn = 1
if not choose:
    turn = 2
