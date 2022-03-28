# importando o tkinter
from tkinter import *
from tkinter import ttk
# importando a biblioteca math
import math

# cores
cor1 = "#363434"  # black/preta
cor2 = "#feffff"  # white/branca
cor3 = "#37474F"  # black/preta
cor4 ="#424345"

fundo = "#e8e6e6"
co10 ="#363434"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x281")
janela.config(bg=cor1)


#criando frames

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_cientifica = Frame(janela, width=300, height=86)
frame_cientifica.grid(row=1, column=0)

frame_corpo = Frame(janela, width=300, height=340)
frame_corpo.grid(row=2, column=0)


global todos_valores

todos_valores = ''
texto = StringVar()

def entra_valores(evento):
    global todos_valores
  
    todos_valores = todos_valores + str(evento)
    texto.set(todos_valores)


# função calcular

def calcular():
    global todos_valores

    modulos = ['math.tan', 'math.sin', 'math.cos', 'math.sqrt', 'math.log', 'math.log10', 'math.e', 'math.pow', 'math.pi']


    for i in modulos:
        if i=='math.tan':
            todos_valores = todos_valores.replace("tan", i)

        if i=='math.sin':
            todos_valores = todos_valores.replace("sin", i)

        if i=='math.cos':
            todos_valores = todos_valores.replace("cos", i)

        if i=='math.sqrt':
            todos_valores = todos_valores.replace("sqrt", i)

  
        # ---------------------------------------------------

        if i=='math.log':
            todos_valores = todos_valores.replace("log", i)

        if i=='math.log10':
            todos_valores = todos_valores.replace("log10", i)

        if i=='math.e':
            todos_valores = todos_valores.replace("e", i)

        if i=='math.pow':
            todos_valores = todos_valores.replace("pow", i)

        # -------------------------------------------------

        if i=='math.pi':
            todos_valores = todos_valores.replace("pi", i)


    resultado = str(eval(todos_valores))
    texto.set(resultado)

    todos_valores = ''

# função limpar tela
def limpartela():
    global todos_valores
    todos_valores = ''
    texto.set("")



# configurando o frame tela

label_tela = Label(janela, textvariable=texto, width=16, height=2, padx=7, anchor='e', bd=0, justify=RIGHT, font=("Ivy 18"), bg=cor3, fg=cor2)
label_tela.place(x=0, y=0)

# configurando o frame cientifica

b_0 = Button(frame_cientifica, command=lambda:entra_valores('tan'), text='tan', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)

b_1 = Button(frame_cientifica, command=lambda:entra_valores('sin'), text='sin', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_1.place(x=59, y=0)

b_2 = Button(frame_cientifica, command=lambda:entra_valores('cos'), text='cos', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_2.place(x=118, y=0)

b_3 = Button(frame_cientifica, command=lambda:entra_valores('sqnt'), text='sqnt', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_3.place(x=177, y=0)


b_0 = Button(frame_cientifica, command=lambda:entra_valores('log'), text='log', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_0.place(x=0, y=29)

b_1 = Button(frame_cientifica, command=lambda:entra_valores('log10'), text='log10', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_1.place(x=59, y=29)

b_2 = Button(frame_cientifica, command=lambda:entra_valores('e'), text='e', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_2.place(x=118, y=29)

b_3 = Button(frame_cientifica, command=lambda:entra_valores('pow'), text='pow', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_3.place(x=177, y=29)


b_0 = Button(frame_cientifica, command=lambda:entra_valores('pi'), text='pi', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_0.place(x=0, y=58)

b_1 = Button(frame_cientifica, command=lambda:entra_valores(','), text=',', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_1.place(x=59, y=58)

b_2 = Button(frame_cientifica, command=lambda:entra_valores('('), text='(', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_2.place(x=118, y=58)

b_3 = Button(frame_cientifica, command=lambda:entra_valores(')'), text=')', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_3.place(x=177, y=58)


# configurando frames corpo
b_0 = Button(frame_corpo, command=limpartela, text='C', width=14, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor4, fg=cor2)
b_0.place(x=0, y=0)

b_1 = Button(frame_corpo, command=lambda:entra_valores('%'), text='%', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor4, fg=cor2)
b_1.place(x=118, y=0)

b_2 = Button(frame_corpo, command=lambda:entra_valores('/'), text='/', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor4, fg=cor2)
b_2.place(x=177, y=0)



b_0 = Button(frame_corpo, command=lambda:entra_valores('7'), text='7', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_0.place(x=0, y=29)

b_1 = Button(frame_corpo, command=lambda:entra_valores('8'), text='8', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_1.place(x=59, y=29)

b_2 = Button(frame_corpo, command=lambda:entra_valores('9'), text='9', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_2.place(x=118, y=29)

b_3 = Button(frame_corpo, command=lambda:entra_valores('*'), text='*', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor4, fg=cor2)
b_3.place(x=177, y=29)


b_0 = Button(frame_corpo, command=lambda:entra_valores('4'), text='4', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_0.place(x=0, y=58)

b_1 = Button(frame_corpo, command=lambda:entra_valores('5'), text='5', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_1.place(x=59, y=58)

b_2 = Button(frame_corpo, command=lambda:entra_valores('6'), text='6', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_2.place(x=118, y=58)

b_3 = Button(frame_corpo, command=lambda:entra_valores('-'), text='-', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor4, fg=cor2)
b_3.place(x=177, y=58)


b_0 = Button(frame_corpo, command=lambda:entra_valores('1'), text='1', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_0.place(x=0, y=87)

b_1 = Button(frame_corpo, command=lambda:entra_valores('2'), text='2', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_1.place(x=59, y=87)

b_2 = Button(frame_corpo, command=lambda:entra_valores('3'), text='3', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_2.place(x=118, y=87)

b_3 = Button(frame_corpo, command=lambda:entra_valores('+'), text='+', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor4, fg=cor2)
b_3.place(x=177, y=87) 


b_0 = Button(frame_corpo, command=lambda:entra_valores('0'), text='0', width=14, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_0.place(x=0, y=116)

b_1 = Button(frame_corpo, command=lambda:entra_valores('.'), text='.', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor1, fg=cor2)
b_1.place(x=118, y=116)

b_2 = Button(frame_corpo, command=calcular, text='=', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cor4, fg=cor2)
b_2.place(x=177, y=116)

janela.mainloop()