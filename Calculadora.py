from tkinter import *
from functools import partial
root = Tk()
root.title('Calculadora')


#Função Botão Igual
def click_igual():
    segundo_numero = visor.get()
    visor.delete(0, END)
    if matematica == 'soma':
        visor.insert(0, p_numero + float(segundo_numero))
    if matematica == 'subtracao':
        visor.insert(0, p_numero - float(segundo_numero))
    if matematica == 'multiplicacao':
        visor.insert(0, p_numero * float(segundo_numero))
    if matematica == 'divisao':
        visor.insert(0, p_numero / float(segundo_numero))

#Função Soma
def click_soma():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'soma'
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

#Função Subtração
def click_subtracao():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'subtracao'
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

#Função Divisão
def click_divisao():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'divisao'
    p_numero = float(primeiro_numero)
    visor.delete(0, END)


#Função Multiplicação
def click_multiplicacao():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'multiplicacao'
    p_numero = float(primeiro_numero)
    visor.delete(0, END)



#Função Botão CE
def deletar():
    visor.delete(0, END)


#Função Botão Ponto
def click_ponto():
    visor.insert(END, '.')



#Função Botões números
def click_button(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual) + str(numero))



#Visor:
lb1 = Label(root, text='CALCULADORA', font=('Time news roman', 15, 'bold'), pady=10)
lb1.pack()


visor = Entry(root, bg='gray90')
visor.pack()


#linha 1 de botões:
bt1 = Button(root, text='1', bg ='gray50', pady=14, padx=14, bd=4, command= lambda: click_button(1))
bt1.place(x=10, y=100)

bt2 = Button(root, text='2', bg='gray50', pady=14, padx=14, bd=4, command= lambda: click_button(2))
bt2.place(x=10, y=155)

bt3 = Button(root, text='3', bg='gray50', pady=14, padx=14, bd=4, command= lambda: click_button(3))
bt3.place(x=10, y=210)

bt0 = Button(root, text='0', bg='gray50', pady=14, padx=14, bd=4, command= lambda: click_button(0))
bt0.place(x=10, y=265)

#Linha 2 de botões:
bt4 = Button(root, text='4', bg='gray50', pady=14, padx=14, bd=4, command= lambda: click_button(4))
bt4.place(x=60, y=100)

bt5 = Button(root, text='5', bg='gray50', pady=14, padx=14, bd=4, command= lambda: click_button(5))
bt5.place(x=60, y=155)

bt6 = Button(root, text='6', bg='gray50', pady=14, padx=14, bd=4, command= lambda: click_button(6))
bt6.place(x=60, y=210)

btPonto = Button(root, text='.', bg='gray50', padx=44, pady=14, command= click_ponto)
btPonto.place(x=60, y=267)

#Linha 3 de botões
bt7 = Button(root, text='7', bg='gray50', pady=14, padx=14, bd=4, command= lambda: click_button(7))
bt7.place(x=110, y=100)

bt8 = Button(root, text='8', bg='gray50', pady=14, padx=14, bd=4, command= lambda: click_button(8))
bt8.place(x=110, y=155)

bt9 = Button(root, text='9', bg='gray50', pady=14, padx=14, bd=4, command= lambda: click_button(9))
bt9.place(x=110, y=210)

#Linha 4 de botôes:
btSoma = Button(root, text='+', bg='gray50', pady=14, padx=14, bd=4, command=click_soma)
btSoma.place(x=160, y=100)

btSubtracao = Button(root, text='-', bg='gray50', pady=14, padx=14, bd=4, command=click_subtracao)
btSubtracao.place(x=160, y=155)

btMultiplicacao = Button(root, text='*', bg='gray50', pady=14, padx=14, bd=4, command=click_multiplicacao)
btMultiplicacao.place(x=160, y=210)

btDivisao = Button(root, text='/', bg='gray50', pady=14, padx=14, bd=4, command=click_divisao)
btDivisao.place(x=160, y=265)

#Botão CE:
btCe = Button(root, text='CE', bg='gray50', pady=119, padx=14, bd=4, command=deletar)
btCe.place(x=210, y=100)

#Botão de igual:
btIgual = Button(root, text='=', bg='gray50', pady=14, padx=119, bd=4, command=click_igual)
btIgual.place(x=10, y=320)

root.resizable(False, False)
root.geometry('280x380')
root.mainloop()


root.resizable(False, False)
root.geometry('280x380')
root.mainloop()