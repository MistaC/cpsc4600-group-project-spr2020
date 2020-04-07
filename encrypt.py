import numpy as np
import string
from sympy import Matrix
import secrets

#This module provides both encryption and decryption functionality for the Hill cipher.
# TODO: Document usage of each function where necessary.
# TODO: Move all code into functions.
# TODO: Changeover from using the ascii values to the printable characters values.

# gives int index for letter in alphabet
def charIndex(char):
    return string.printable.index(char)
def indexChar(index):
    return string.printable[index]

# def createKey():
#     keyWord = input("Input Key: ")
#     keyIntsCollection = [letterIndex(c) for c in keyWord]
#     lengthOfKey = len(keyIntsCollection)
#     matrix = np.zeros((2, int(lengthOfKey / 2)), dtype=np.int32)
#     iterator = 0
#     for column in range(int(lengthOfKey / 2)):
#         for row in range(2):
#             matrix[row][column] = keyIntsCollection[iterator]
#             iterator += 1
#     matrix = np.array(matrix)
#     return matrix
#
# def getMatrixParameters(matrix):
#     matrixRows = matrix.shape[0]
#     matrixColumns = matrix.shape[1]
#     if matrixRows != matrixColumns:
#         raise Exception("must be a square matrix")
#     if np.linalg.det(matrix) == 0:
#         raise Exception("matrix must have an inverse")
#     return [matrixRows,matrixColumns]


#Returns cryptographically secure 3x3 square list of the cipher key. May not work on all systems.
def genKey():
    key_matrix = np.zeros((3,3),dtype=np.int)
    for row in range(3):
        for col in range(3):
            key_matrix[row][col] = 0+secrets.randbelow(100) #Addressing from 0-99 for printable characters
    return key_matrix


#Encrypts message in blocks of 3.
def encrypt(key,msg): #key is key matrix. msg is plaintext string.
    temp = np.zeros((3,1), dtype=np.int) #holds msg character ascii values
    encrypted_text = ''
    iter = 0
    print("The plaintext is: {}".format(msg))
    for c in msg: #Loop three times. Get a character ascii value each time. Do matrix mult at 3. Convert resulting values into letters and concat with text variable.
        if iter > 2: #3 ascii values already in temp
            mult = np.matmul(key,temp) #3x3 * 3x1 = 3x1
            mult[0][0] = mult[0][0] % 100
            mult[1][0] = mult[1][0] % 100
            mult[2][0] = mult[2][0] % 100
            encrypted_text += indexChar(mult[0][0])
            encrypted_text += indexChar(mult[1][0])
            encrypted_text += indexChar(mult[2][0])
            iter = 0
        temp[iter][0] = charIndex(c)
        iter += 1
    if iter > 0: #Exited loop with partially or fully filled block of three values.
        if iter == 1:
            #single value in temp
            mult = np.matmul(key,temp) #3x3 * 3x1 = 3x1
            mult[0][0] = mult[0][0] % 100
            encrypted_text += indexChar(mult[0][0])
        elif iter == 2:
            #two values in temp
            mult = np.matmul(key,temp) #3x3 * 3x1 = 3x1
            mult[0][0] = mult[0][0] % 100
            mult[1][0] = mult[1][0] % 100
            encrypted_text += indexChar(mult[0][0])
            encrypted_text += indexChar(mult[1][0])
        elif iter == 3:
            mult = np.matmul(key,temp) #3x3 * 3x1 = 3x1
            mult[0][0] = mult[0][0] % 100
            mult[1][0] = mult[1][0] % 100
            mult[2][0] = mult[2][0] % 100
            encrypted_text += indexChar(mult[0][0])
            encrypted_text += indexChar(mult[1][0])
            encrypted_text += indexChar(mult[2][0])
        else:
            print("Something went wrong in the encryption function.")
    return encrypted_text


# TODO: FINISH DECRYPTION FUNCTION
#Decrypts message in blocks of 3.
def decrypt(key,msg):
    pass


# TODO: Rewrite as two functions, one for encryption and decryption. Both take a text file object, but decryption also takes a key file object.
def main():
    with open('test.txt') as f:
        msg = f.read().strip()
    # print(genKey())
    key = genKey()
    ciphertext = encrypt(key,msg)
    print(ciphertext)
    # everything = string.printable
    # for symbol in everything:
    #     print("{}: {}".format(everything.index(symbol),symbol))
#main()



# plainMsg = input("Input plaintext: ")
# message = []
# for i in range(0, len(plainMsg)):
#     current = plainMsg[i:i+1].lower()
#     if current != ' ':
#         index = letterIndex(current)
#         message.append(index)
# key = createKey()
# if len(message) % getMatrixParameters(key)[0] !=0:
#     for i in range(0, len(message)):
#         message.append(message[i])
#         if len(message) % getMatrixParameters(key)[0] == 0:
#             break
# message = np.array(message)
# messageLength = message.shape[0]
# message.resize(int(messageLength/(getMatrixParameters(key)[0])), (getMatrixParameters(key)[1]))
# print(message)
#
# encryption = np.matmul(message,key)
# encryption = np.remainder(encryption, 26)
# print('\n',encryption)
#
# inverseKey = Matrix(key).inv_mod(26)
# inverseKey = np.array(inverseKey)
# inverseKey = inverseKey.astype(int)
# print('\n',inverseKey)
#
# decryption = np.matmul(encryption,inverseKey)
# decryption = np.remainder(decryption,26).flatten()
# def getDecrypt(decryption):
#     decrypt= ""
#     for i in range(0,len(decryption)):
#         letterNum = int(decryption[i])
#         letter = indexLetter(decryption[i])
#         decrypt = decrypt + letter
#     return decrypt
# print('\n',getDecrypt(decryption))
