from tkinter import *
from playsound import playsound
from gtts import *
import os

# Iniciando Interface

root = Tk()
root.title('Conversor de Texto para fala')
root.geometry('1600x900')
root.maxsize(1600, 900)
root.minsize(500, 420)
root.configure(bg='black')


# definindo Margem para colocar entre os quadros de textos
def margem(altura):
    tela = Canvas(root,
                  width=500,
                  height=altura,
                  bg='black',
                  bd=0,
                  highlightthickness=0,
                  relief='ridge')
    tela.pack()


margem(20)

# Definindo quadros de texto

titulo = Label(root,
               bg='black',
               fg='white',
               font=('Montserrat', 18, 'bold'),
               text='Conversor de texto para fala')

titulo.pack()  # ao terminar de definir o quadro faça ".pack" para renderizar

margem(20)

insere_texto = Label(root,
                     bg='black',
                     fg='white',
                     font=('Montserrat', 18, 'bold'),
                     text='Insira o seu texto:',
                     anchor='w')  # anchor é para alinhar o quadro para algum canto da interface, nesse caso a esquerda

insere_texto.pack()

root.mainloop()
