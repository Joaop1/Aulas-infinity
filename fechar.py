import tkinter
tela_01 = tkinter.Tk()
tela_01.title('Fechar')
tela_01.geometry('600x600')
tela_01.resizable(width=False, height=False)

botao_fechar = tkinter.Button(tela_01,
                              text='Fechar',
                              bg='gray',
                              fg='white',
                              font=('arial', 12),
                              command=tela_01.destroy
                              )
botao_fechar.pack(side='bottom')
label1 = tkinter.Label(tela_01, text='Olá!')

entrada01 = tkinter.Entry(tela_01)
label1.pack()
entrada01.pack()

tela_01.mainloop()

