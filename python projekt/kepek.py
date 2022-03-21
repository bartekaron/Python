from tkinter import *
def klikk():
    print("Klikkeltem")
ablak1 = Tk()
gyoker = "H:\\IKT Projektmunka\\python projekt\\"
ablak1.geometry("450x450")
ablak1.title("Ikt Tkinter")
Icon = PhotoImage(file = "Png.png")
ablak1.iconphoto(True, Icon)
ablak1.config(background="black")
#elsokep =(PhotoImage(file=gyoker+"Png.png"))
gombkep = (PhotoImage(file=gyoker+"Png.png", width="10", height='10'))
"""cimke = Label(ablak1, 
                text="Üdvözlet",
                fg="#553388",
                bg="#c3cee9",
                font=("Arial", 45, "bold"),
                bd=10,
                relief=RAISED,
                padx=25,
                pady=30,
                image=elsokep,
                compound="top").pack()
"""
gomb = Button(ablak1,
             text = "Kattints",
             fg="blue",
             font=("Comic Sans", 35, "bold"),
             relief=SUNKEN,
             bd=10,
             command=klikk,
             padx=12,
             pady=12,
             image=gombkep, 
             compound="bottom",
             activebackground="blue",
             activeforeground="yellow",
             state=ACTIVE).pack()
                



ablak1.mainloop()