from tkinter import *
import tkinter.font as tkFont

def start():
    main.destroy()

main = Tk()
main.geometry("800x800")

main.configure(bg="green")

custom_font = tkFont.Font(family="Impact", size=150)
custom_font_btn = tkFont.Font(family="Impact", size=50)
custom_font_sur = tkFont.Font(family="Impact", size=25)

frm_titre = Frame(main)
frm_titre.configure(bg="green")
frm_titre.pack(pady=100)

surtitre = Label(frm_titre, text="Le meilleur jeu d'")
surtitre.configure(font=custom_font_sur, bg="green")
surtitre.pack(anchor=NW, padx=20,)

titre = Label(frm_titre, text="Othello")
titre.configure(font=custom_font, bg="green")
titre.pack(anchor=W)

jouer = Button(main, text="Jouer !", command=start)
jouer.configure(font=custom_font_btn)
jouer.pack()


main.mainloop()