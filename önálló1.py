from tkinter import *

foablak=Tk()
foablak.title("tk")
Icon = PhotoImage(file = "Png.png")
foablak.iconphoto(True, Icon)
cimke=Label(foablak, text="Első mező:", fg="black", compound="top")
cimke.grid()
mezo=Entry(foablak, width=10,)
mezo.grid(row=0, column=2)
cimke1=Label(foablak, text="Második mező:", fg="black", compound="center" )
cimke1.grid()
mezo1=Entry(foablak, width=10,)
mezo1.grid(row=1, column=2)
cimke2=Label(foablak, text="Harmadik mező:", fg="black", compound="bottom")
cimke2.grid()
mezo2=Entry(foablak, width=10,)
mezo2.grid(row=2, column=2)
can1 = Canvas(foablak, width =160, height =160, bg ="white",)
photo = PhotoImage(file = 'R.gif')
item = can1.create_image(100, 100, image =photo,)
can1.grid(rowspan=3, columnspan=1, column=3, row=0, padx=15)



foablak.mainloop()