from tkinter import *
import math


def térfogat():
    a = float(mezo.get())
    b = float(mezo1.get())
    c = round(a**2*b*math.pi, 0)
    d = float(mezo5.get())
    m = float(c/1000)
    x = m-d
    mezo2.delete(0, END)
    mezo2.insert(0,""+str(m)+" liter")
    if m > d:
        mezo3.delete(0, END)
        mezo3.insert(0,"Igen")
        mezo4.insert(0,""+str(x)+" liter")

    else:
        mezo3.delete(0, END)
        mezo3.insert(0,"Nem")
"""
def hord():
    a = float(mezo.get())
    b = float(mezo1.get())
    c = str(mezo5.get)
    V = a**2*b*math.pi
    m=str(V/1000)
    if m > c:
        mezo3.delete(0, END)
        mezo3.insert(0,"Igen")
    else:
        mezo3.delete(0, END)
        mezo3.insert(0,"Nem")
"""

foablak=Tk()
foablak.title("tk")
cimke=Label(foablak, text="Sugár (cm):", fg="black", compound="top")
cimke.grid()
mezo=Entry(foablak, width=23,)
mezo.grid(row=0, column=2)
cimke1=Label(foablak, text="Magasság (cm):", fg="black", compound="top")
cimke1.grid()
cimke2=Label(foablak, text="Bor (liter):", fg="black", compound="top")
cimke2.grid()
mezo5=Entry(foablak, width=23,)
mezo5.grid(row=2, column=2)
mezo1=Entry(foablak, width=23,)
mezo1.grid(row=1, column=2)
gomb=Button(foablak, text="Kiszámít", command=lambda:[térfogat()])
gomb.grid(row=3, column=3)
cimke3=Label(foablak, text="Hordó ennyi literes:", fg="black")
cimke3.grid()
mezo2=Entry(foablak, width=23,)
mezo2.grid(row=4, column=2)
cimke4=Label(foablak, text="Belefér-e:", fg="black",)
cimke4.grid()
mezo3=Entry(foablak, width=23,)
mezo3.grid(row=5, column=2)
cimke5=Label(foablak, text="Ennyi fér még bele:", fg="black")
cimke5.grid()
mezo4=Entry(foablak, width=23,)
mezo4.grid(row=6, column=2)
can1 = Canvas(foablak, width =400, height =400, bg ="white",)
photo = PhotoImage(file = 'hordocska.png')
item = can1.create_image(300, 200, image =photo,)
can1.grid(rowspan=3, columnspan=1, column=3, row=0)



foablak.mainloop()

