from tkinter import *
from tkinter import ttk

cor_preto = "#1d1f21"
cor_branco = "#fafbfc"
cor_azul = "#2179d1"
cor_cinza = "#bfbbbb"
cor_laranja = "#cc7606"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(background=cor_preto)

#frames
frame_tela = Frame(janela, width=235,height=50, bg=cor_preto)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#lógica com matemática

#variavel global para receber os valores
todos_valores = ''

def inserir(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    
    #mostrando valor
    valor_texto.set(todos_valores)


def calculo():
    global todos_valores
    reusltado = eval(todos_valores)
    
    valor_texto.set(str(reusltado))



def limpa_tela ():

    global todos_valores

    todos_valores = ''
    valor_texto.set("")

#labels

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor_preto, fg=cor_branco)
app_label.place(x = 0, y=0)

#botões

#fila 1

b_1 = Button(frame_corpo, command= limpa_tela, text="C", width=11, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command=lambda: inserir('%'), text="%", width=5, height=2, bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, command=lambda: inserir('/'), text="/", width=5, height=2,bg = cor_laranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

#fila 2

b_4 = Button(frame_corpo, command=lambda: inserir('7'), text="7", width=5, height=2, bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo,command= lambda: inserir('8'), text="8", width=5, height=2,bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command=lambda: inserir('9'), text="9", width=5, height=2,bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command= lambda: inserir('*'), text="*", width=5, height=2,bg = cor_laranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)


#fila 2

b_8 = Button(frame_corpo, command=lambda: inserir('4'), text="4", width=5, height=2, bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command=lambda: inserir('5'), text="5", width=5, height=2,bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command=lambda: inserir('6'), text="6", width=5, height=2,bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command=lambda: inserir('-'), text="-", width=5, height=2,bg = cor_laranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

#fila 3

b_12 = Button(frame_corpo, command=lambda: inserir('1'),text="1", width=5, height=2, bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command=lambda: inserir('2'), text="2", width=5, height=2,bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command=lambda: inserir('3'), text="3", width=5, height=2,bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command=lambda: inserir('+'), text="+", width=5, height=2,bg = cor_laranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

#fila 4

b_16 = Button(frame_corpo, command=lambda: inserir('0'), text="0", width=11, height=2, bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command=lambda: inserir('.'), text=".", width=5, height=2,bg = cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, command= calculo, text="=", width=5, height=2,bg = cor_laranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)

#calculando


janela.mainloop()
