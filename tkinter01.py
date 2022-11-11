import tkinter
#import tkinter as tk
#from tkinter import*

tela_principal = tkinter.Tk()
tela_principal.title("Primeira Interface")
tela_principal.geometry('400x400')
#tela_principal.resizable(width=False, height=False)
botao1 = tkinter.Button(tela_principal,
                        text='Botão',
                        activebackground='#034078',
                        bg='#0a1128',
                        fg='#1282a2',
                        font=('arial', 18))
#botao1.grid(column=5, row=9)
#botao1.grid()
#botao1.place()
botao2 = tkinter.Button(tela_principal,
                        text='Fechar',
                        activebackground='#034078',
                        bg='#0a1128',
                        fg='#1282a2',
                        font=('arial', 10))
#botao2.grid(column=0, row=0)

botao1.place(x=165, y=10)
botao2.place(x=180, y=370)
tela_principal.mainloop()
