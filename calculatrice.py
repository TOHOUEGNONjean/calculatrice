from tkinter import *
#definition les fonction pour les opérations

def click(iteme): #pour afficher les laveurs à l'écrant
    global espression
    espression = espression + str(iteme)
    input_text.set(espression)

def effacer():#effacé l'écrant
    global espression
    espression = ""
    input_text.set(espression)

def operation(): #faire les opérations
    global espression
    resultat = str(eval(espression))
    input_text.set(resultat)
    espression = ""


espression = ""

#creationd de l'écran 
ecran =Tk()
ecran.title(" CALCULATRICE JB")
ecran.geometry("320x400")
ecran.resizable(FALSE,FALSE)
#definition de la couleur des boutons
couleur = "blue"
text_couleur = "#fff"

#création des ecrants d'affichage
input_text = StringVar()
afichage = Entry(ecran, textvariable=input_text,font="arial, 30")
afichage.place( height=100,)
input_text.set("0")


#création du block des boutons numériques
btns_frame = Frame(ecran)
btns_frame.place(relx=0.5, rely=0.65, anchor=CENTER, width=315, height=300)

#bouton effacer
efface = Button(btns_frame, text='C', command=effacer,height= 5, width=5)
efface.grid(column=4, row=0)
val1 = Button(btns_frame, text = "1",bg=couleur, command=lambda: click(1), height= 5, width=5,fg=text_couleur)
val1.grid(column=0, row=0)
val2 = Button(btns_frame, text = "2",bg = couleur, command=lambda: click(2),height= 5, width=5,fg=text_couleur)
val2.grid(column=1, row=0)
val3 = Button(btns_frame, text = "3",bg = couleur, command=lambda: click(3), height= 5, width=5,fg=text_couleur)
val3.grid(column=2, row=0)

val4 = Button(btns_frame, text = "4",bg=couleur, command=lambda: click(4),height= 5, width=5,fg=text_couleur)
val4.grid(column=0, row=1)
val5 = Button(btns_frame, text = "5",bg = couleur, command=lambda: click(5),height= 5, width=5,fg=text_couleur)
val5.grid(column=1, row=1)
val6 = Button(btns_frame, text = "6",bg = couleur, command=lambda: click(6) ,height= 5, width=5,fg=text_couleur)
val6.grid(column=2, row=1)


val7 = Button(btns_frame, text = "7",bg=couleur, command=lambda: click(7), height= 5, width=5,fg=text_couleur)
val7.grid(column=0, row=2)
val8 = Button(btns_frame, text = "8",bg = couleur, command=lambda: click(8), height= 5, width=5,fg=text_couleur)
val8.grid(column=1, row=2)
val9 = Button(btns_frame, text = "9",bg = couleur, command=lambda: click(9), height= 5, width=5,fg=text_couleur)
val9.grid(column=2, row=2)

#les opérateurs
op1 = Button(btns_frame, text='/', command= lambda: click("/"),height= 5, width=5)
op1.grid(column=3,row=0)

op1 = Button(btns_frame, text='x', command= lambda: click("*"),height= 5, width=5)
op1.grid(column=3,row=1)

op1 = Button(btns_frame, text='0', command= lambda: click(0),height= 5, width=5)
op1.grid(column=3,row=2)

op3 = Button(btns_frame, text='+', command= lambda: click("+"), width=5, height=5)
op3.grid(column=4, row=1)

op4 = Button(btns_frame, text='-', command= lambda: click("-"), width=5, height=5)
op4.grid(column=4, row=2)

op4 = Button(btns_frame, text='=', command= operation, width=5, height=5,bg='red',fg='#FFF')
op4.place(rely=0.7,width=320, height=60)

ecran.mainloop()