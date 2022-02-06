from tkinter import *
from PIL import Image, ImageTk
import networkx as nx
import matplotlib.pyplot as plt

root = Tk()

root.geometry('1000x800')
root.config(background = 'White')
root.resizable(width = False, height = False)

imag_1=Image.open('estrada3.jpg')

imag_1 = ImageTk.PhotoImage(imag_1)

background = Label(image=imag_1)
background.grid(row = 0, column = 0, columnspan = 3)


def caminhoneiro():

    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row = 1, column = 0, columnspan = 3)

    buttonEncontrar = Button(root,text='Encontrar a melhor rota para o meu destino',padx=117,pady=5,fg='white',bg='black')
    buttonEncontrar.place(relx=0.5,rely=0.1,anchor=CENTER)

    buttonAtivas = Button(root,text='Saber quais estradas estão ativas',padx=117,pady=5,fg='white',bg='black')
    buttonAtivas.place(relx=0.5,rely=0.2,anchor=CENTER)

    buttonInativas = Button(root,text='Saber quais estradas estão inativas',padx=117,pady=5,fg='white',bg='black')
    buttonInativas.place(relx=0.5,rely=0.3,anchor=CENTER)

    buttonMapa = Button(root,text='Ver um mapa com estradas atuais',padx=117,pady=5,fg='white',bg='black')
    buttonMapa.place(relx=0.5,rely=0.4,anchor=CENTER)

    buttonVoltar = Button(root,text='Voltar',padx=117,pady=5,fg='white',bg='black',command=menu)
    buttonVoltar.place(relx=0.5,rely=0.7,anchor=CENTER)

def fiscal():

    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row = 1, column = 0, columnspan = 3)

    buttonInativar = Button(root,text='Inativar uma estrada',padx=117,pady=5,fg='white',bg='black')
    buttonInativar.place(relx=0.5,rely=0.1,anchor=CENTER)

    buttonReativar = Button(root,text='Reativar uma estrada',padx=117,pady=5,fg='white',bg='black')
    buttonReativar.place(relx=0.5,rely=0.2,anchor=CENTER)

    buttonAtivas = Button(root,text='Saber quais estradas estão ativas',padx=117,pady=5,fg='white',bg='black')
    buttonAtivas.place(relx=0.5,rely=0.3,anchor=CENTER)

    buttonInativas = Button(root,text='Saber quais estradas estão inativas',padx=117,pady=5,fg='white',bg='black')
    buttonInativas.place(relx=0.5,rely=0.4,anchor=CENTER)

    buttonMapa = Button(root,text='Ver um mapa com estradas atuais',padx=117,pady=5,fg='white',bg='black')
    buttonMapa.place(relx=0.5,rely=0.5,anchor=CENTER)

    buttonVoltar = Button(root,text='Voltar',padx=117,pady=5,fg='white',bg='black',command=menu)
    buttonVoltar.place(relx=0.5,rely=0.7,anchor=CENTER)


def menu():

    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row = 1, column = 0, columnspan = 3)

    buttonCaminhoneiro = Button(root, text='Caminhoneiro',padx=85,pady=5,fg='white',bg='black',command=caminhoneiro)
    buttonCaminhoneiro.place(relx=0.5,rely=0.1,anchor=CENTER)

    buttonFiscal = Button(root, text='Fiscal do DER',padx=85,pady=5,fg='white',bg='black',command=fiscal)
    buttonFiscal.place(relx=0.5,rely=0.2,anchor=CENTER)

    buttonSaida = Button(root, text='Sair',padx=85,pady=5,fg='white',bg='black',command=root.quit)
    buttonSaida.place(relx=0.5,rely=0.5,anchor=CENTER)

menu()
root.mainloop()

