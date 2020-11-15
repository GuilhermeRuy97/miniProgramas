import onetimepad
from tkinter import *

root = Tk()
root.title("CRYPTOGRAPHY")
root.geometry("420x100")

#Função para criptografar mensagem
def encryptMessage():
        pt = e1.get()

        ct = onetimepad.encrypt(pt, 'random')
        e2.insert(0, ct)

#Função para descriptografar uma mensagem
def decryptMessage():
        ct1 = e3.get()

        pt1 = onetimepad.decrypt(ct1, 'random')
        e4.insert(0, pt1)

#Criando labels e posicionando-as no grid
label1 = Label(root, text = 'plain text')
label1.grid(row = 10, column = 1)
label2 = Label(root, text = 'encrypted text')
label2.grid(row = 11, column = 1)
label3 = Label(root, text = 'plain text')
label3.grid(row = 10, column = 10)
label4 = Label(root, text = 'plain text')
label4.grid(row = 11, column = 10)

#Criando entradas e colocando-as no grid
e1 = Entry(root)
e1.grid(row = 10, column = 2)
e2 = Entry(root)
e2.grid(row = 11, column = 2)
e3 = Entry(root)
e3.grid(row = 10, column = 11)
e4 = Entry(root)
e4.grid(row = 11, column = 11)

#Criar botão de encriptografar
ent = Button(root, text = "encrypt", bg = "red",
             fg = "white", command = encryptMessage)
ent.grid(row = 13,column = 2)

#Criar botão de descriptografar
b2 = Button(root, text = "decrypt", bg = "green",
            fg = "white", command = decryptMessage)
b2.grid(row = 13, column = 11)

root.mainloop()