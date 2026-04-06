import tkinter
import tkinter.messagebox
import random
screen = tkinter.Tk()
screen.geometry("600x600")
screen.title("Tic Tac Toe")


turn = "X"
def selected(buttonselect):
    if len(buttons) == 0 :
        tiemessage = "There is a tie!"
        tkinter.messagebox.showinfo("Tie!",tiemessage)
    if len(buttons) > 0 :
        buttonselect.config(text=turn)
        buttons.remove(buttonselect)
        checkwin()
    if len(buttons) == 0 :
        tiemessage = "There is a tie!"
        tkinter.messagebox.showinfo("Tie!",tiemessage)
    if len(buttons) > 0 :
        computerbutton = random.choice(buttons)
        computerbutton.config(text="O")
        buttons.remove(computerbutton)
        checkwin()

def checkwin():
    
    for i in winning_combinations:
        if i[0]["text"] == "X" and i[1]["text"] == "X" and i[2]["text"] == "X" :
           winmessage = "Player has won!"
           tkinter.messagebox.showinfo("Winner!",winmessage)
        if i[0]["text"] == "O" and i[1]["text"] == "O" and i[2]["text"] == "O" :
            winmessage = "Computer has won!"
            tkinter.messagebox.showinfo("Winner!",winmessage)
        
        
    

selectButton1 = tkinter.Button(text="Select",command=lambda:selected(selectButton1))
selectButton2 = tkinter.Button(text="Select",command=lambda:selected(selectButton2))
selectButton3 = tkinter.Button(text="Select",command=lambda:selected(selectButton3))
selectButton4 = tkinter.Button(text="Select",command=lambda:selected(selectButton4))
selectButton5 = tkinter.Button(text="Select",command=lambda:selected(selectButton5))
selectButton6 = tkinter.Button(text="Select",command=lambda:selected(selectButton6))
selectButton7 = tkinter.Button(text="Select",command=lambda:selected(selectButton7))
selectButton8 = tkinter.Button(text="Select",command=lambda:selected(selectButton8))
selectButton9 = tkinter.Button(text="Select",command=lambda:selected(selectButton9))
buttons = [selectButton1,selectButton2,selectButton3,selectButton4,selectButton5,selectButton6,selectButton7,selectButton8,selectButton9]

winning_combinations = [
    [selectButton1,selectButton2,selectButton3],
    [selectButton4,selectButton5,selectButton6],
    [selectButton7,selectButton8,selectButton9],
    [selectButton1,selectButton5,selectButton9],
    [selectButton3,selectButton5,selectButton7],
    [selectButton1,selectButton4,selectButton7],
    [selectButton2,selectButton5,selectButton8],
    [selectButton3,selectButton6,selectButton9]
]
selectButton1.place(x=100,y=100)
selectButton2.place(x=100,y=200)
selectButton3.place(x=100,y=300)
selectButton4.place(x=200,y=100)
selectButton5.place(x=200,y=200)
selectButton6.place(x=200,y=300)
selectButton7.place(x=300,y=100)
selectButton8.place(x=300,y=200)
selectButton9.place(x=300,y=300)


screen.mainloop()
