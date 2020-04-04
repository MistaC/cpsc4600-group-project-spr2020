import numpy as np
import string
from sympy import Matrix
import secrets

#This module provides both encryption and decryption functionality for the Hill cipher.
# TODO: Simplify code to streamline understanding of functions and reduce non-built-in dependencies.
# TODO: Document usage of each function where necessary.
# TODO: Move all code into functions.

# gives int index for letter in alphabet
def letterIndex(letter):
    return string.ascii_lowercase.index(letter)
def indexLetter(index):
    return chr(int(index) +97 )

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


#Returns cryptographically secure square list of the cipher key. May not work on all systems. Argument from argv.
def genKey(msg_height):
    key_matrix = [msg_height][msg_height]
    for row in key_matrix:
        for column in key_matrix:
            key_matrix[row][column] = 97+secrets.randbelow(25) #get value of an ascii lowercase alphabet symbol
    return key_matrix
def encrypt(key,msg):
    pass
def decrypt(key,msg):
    pass

def main():
    # with open('test.txt') as f:
    #     t = f.read()
    # print(t.strip())
    with open('test.txt') as f:
        msg = f.read().strip()
        msg_list = [][]
        for k,v in msg:
            if v != ' ':
                msg_list[k][0] = v #expansion of rows, not columns
    msg_height = len(msg_list) #gets number of rows
    key = genKey(msg_height)
main()



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
