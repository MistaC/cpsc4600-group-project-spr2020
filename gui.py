from tkinter import *
from encrypt import *
import numpy as np

mainWindow = Tk()
mainWindow.geometry("500x200")
msg = Entry(mainWindow)
msg.pack()
def encryptClick():
		keyGenFile = open("key.txt", "w")
		ciphertextWriteFile = open("codedmessage.txt", "w")
		key = genKey()
		inverseKey = Matrix(key).inv_mod(100)
		inverseKey = np.array(inverseKey)
		inverseKey = inverseKey.astype(int)
		# inverseKey.tofile(keyGenFile) #Issue occurs here
		for i in range(3):
		    for j in range(3):
		        keyGenFile.write("{}:".format(inverseKey[i][j]))
		keyGenFile.close()
		cipherText = encrypt(key,msg.get())
		ciphertextWriteFile.write(cipherText)
		ciphertextWriteFile.close()
		print("---------------\nEncryption complete! Ciphertext below.\n\n{}\n---------------".format(cipherText))
		# complete = Label(mainWindow, text="Encryption complete")
		# complete.pack()
		# print(cipherText)
def decryptClick():
		readKey = open("key.txt", "r")
		readMessage = open("codedmessage.txt", "r")

		inv_key = readKey.read().split(":")
		inv_key = [x for x in inv_key if x != ":"]
		inv_key = [x for x in inv_key if x != ""]
		dec_key = [[0 for j in range(3)] for i in range(3)]
		iter = 0
		for i in range(3):
		    for j in range(3):
		        dec_key[i][j] = int(inv_key[iter])
		        iter += 1
		final_key = np.asarray(dec_key)
		# print(final_key)
		decryptedText = decrypt(final_key,readMessage.read())
		print("---------------\nDecryption complete! Plaintext below.\n\n{}\n---------------".format(decryptedText))
		# complete = Label(mainWindow, text=decryptedText)
		# complete.pack()
		readKey.close()
		readMessage.close()
encryptButton = Button(mainWindow,text="encrypt", command=encryptClick)
decryptButton = Button(mainWindow,text="decrypt", command=decryptClick)
encryptButton.pack()
decryptButton.pack()
mainWindow.mainloop()
