from tkinter import *
from encrypt import *

mainWindow = Tk()
msg = Entry(mainWindow)
msg.pack()
def encryptClick():
		keyGenFile = open("key.txt", "w")
		ciphertextWriteFile = open("codedmessage.txt", "w")
		key = genKey()
		inverseKey = Matrix(key).inv_mod(100)
		inverseKey = np.array(inverseKey)
		inverseKey = inverseKey.astype(int)
		inverseKey.tofile(keyGenFile)
		keyGenFile.close()
		cipherText = encrypt(key,msg.get())
		ciphertextWriteFile.write(cipherText)
		ciphertextWriteFile.close()
		complete = Label(mainWindow, text="Encryption complete")
		complete.pack()
		print(cipherText)
def decryptClick():
		readKey = open("key.txt", "r")
		readMessage = open("codedmessage.txt", "r")

		decryptedText = decrypt(readKey.read(),readMessage.read())
		complete = Label(mainWindow, text=decryptedText)
		complete.pack()
		readKey.close()
		readMessage.close()
encryptButton = Button(mainWindow,text="encrypt", command=encryptClick)
decryptButton = Button(mainWindow,text="decrypt", command=decryptClick)
encryptButton.pack()
decryptButton.pack()
mainWindow.mainloop()








