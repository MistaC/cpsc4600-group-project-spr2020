from tkinter import *
from encrypt import *
import numpy as np
import time

mainWindow = Tk()
def encryptClick():
	start = time.time()
	with open('message.txt') as f:
		msg = f.read().strip()
	ciphertextWriteFile = open("codedmessage.txt", "w")
	key = genKey()
	inverseKey = Matrix(key).inv_mod(100)
	inverseKey = np.array(inverseKey)
	inverseKey = inverseKey.astype(int)
	np.save("key",inverseKey)
	cipherText = encrypt(key,msg)
	ciphertextWriteFile.write(cipherText)
	ciphertextWriteFile.close()
	end = time.time()
	print("---------------\nEncryption complete! Ciphertext below.\n\n{}\n---------------\nTotal execution time: {} seconds".format(cipherText,end-start))
	# complete = Label(mainWindow, text="Encryption complete")
	# complete.pack()
	# print(cipherText)
def decryptClick():
	start = time.time()
	inv_key = np.load("key.npy")
	readMessage = open("codedmessage.txt", "r")

	# inv_key = readKey.read().split(":")
	# inv_key = [x for x in inv_key if x != ":"]
	# inv_key = [x for x in inv_key if x != ""]
	# dec_key = [[0 for j in range(3)] for i in range(3)]
	# iter = 0
	# for i in range(3):
	# 	for j in range(3):
	# 		dec_key[i][j] = int(inv_key[iter])
	# 		iter += 1
	# final_key = np.asarray(dec_key)
	# print(final_key)
	decryptedText = decrypt(inv_key,readMessage.read())
	end = time.time()
	print("---------------\nDecryption complete! Plaintext below.\n\n{}\n---------------\nTotal execution time: {} seconds".format(decryptedText,end-start))
	output = open("decrypted_message.txt","w")
	output.write(decryptedText)
	output.close()
	readMessage.close()
encryptButton = Button(mainWindow,text="encrypt", command=encryptClick)
decryptButton = Button(mainWindow,text="decrypt", command=decryptClick)
encryptButton.pack()
decryptButton.pack()
mainWindow.mainloop()
