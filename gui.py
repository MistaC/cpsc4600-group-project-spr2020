from tkinter import *
from encrypt import *
keyFile = open("key.txt", "w")
window = Tk()
msg = Entry(window, width=30)
msg.pack()

def clickButton():
	key = genKey()
	ciphertext = encrypt(key,msg.get())
	key.tofile(keyFile)
	cipherLabel = Label(window, text=ciphertext)
	cipherLabel.pack()
button = Button(window, text="Click after message is entered", command=clickButton)
button.pack()

window.mainloop()
keyFile.close()
keyRead = open("key.txt", "r")
print(np.fromfile(keyRead))
keyRead.close()





