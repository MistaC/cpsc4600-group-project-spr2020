import numpy as np
import string
from sympy import Matrix
import secrets


# This module provides both encryption and decryption functionality for the Hill cipher.
# Contributors:  Chase Carroll, Cole Robinson
# Team Members:  Chase Carroll, Cole Robinson, Justin Joseph, Fatima Ejaz, and Chance Walmsley
# Date:          April 2020

def charIndex(char):
    return string.printable.index(char)


def indexChar(index):
    return string.printable[index]


# Returns cryptographically secure 3x3 square list of the cipher key. May not work on all systems.
def genKey():
    key_matrix = np.zeros((3, 3), dtype=np.int)
    while True:
        try:
            for row in range(3):
                for col in range(3):
                    key_matrix[row][col] = 0 + secrets.randbelow(100)  # Addressing from 0-99 for printable characters
            inverse_key = Matrix(key_matrix).inv_mod(100)
            inverse_key = np.array(inverse_key)
            inverse_key = inverse_key.astype(int)
            break
        except ValueError:
            print("Key is not invertible. Trying another...")
    return key_matrix


# Encrypts message in blocks of 3.
def encrypt(key, msg):  # key is key matrix. msg is plaintext string.
    temp = np.zeros((3, 1), dtype=np.int)  # holds msg character ascii values
    encrypted_text = ''
    iter = 0
    for c in msg:  # Loop three times. Get a character ascii value each time. Do matrix mult at 3. Convert resulting values into letters and concat with text variable.
        if iter > 2:  # 3 ascii values already in temp
            mult = np.matmul(key, temp)  # 3x3 * 3x1 = 3x1
            mult[0][0] = mult[0][0] % 100
            mult[1][0] = mult[1][0] % 100
            mult[2][0] = mult[2][0] % 100
            encrypted_text += indexChar(mult[0][0])
            encrypted_text += indexChar(mult[1][0])
            encrypted_text += indexChar(mult[2][0])
            temp = np.zeros((3, 1), dtype=np.int)
            iter = 0
        temp[iter][0] = charIndex(c)
        iter += 1
    if iter > 0:  # Exited loop with partially or fully filled block of three values. Do padding where necessary with space character.
        if iter == 1:
            # single value in temp
            temp[1][0] = charIndex(" ")
            temp[2][0] = charIndex(" ")
            mult = np.matmul(key, temp)  # 3x3 * 3x1 = 3x1
            mult[0][0] = mult[0][0] % 100
            mult[1][0] = mult[1][0] % 100
            mult[2][0] = mult[2][0] % 100
            encrypted_text += indexChar(mult[0][0])
            encrypted_text += indexChar(mult[1][0])
            encrypted_text += indexChar(mult[2][0])
        elif iter == 2:
            # two values in temp
            temp[2][0] = charIndex(" ")
            mult = np.matmul(key, temp)  # 3x3 * 3x1 = 3x1
            mult[0][0] = mult[0][0] % 100
            mult[1][0] = mult[1][0] % 100
            mult[2][0] = mult[2][0] % 100
            encrypted_text += indexChar(mult[0][0])
            encrypted_text += indexChar(mult[1][0])
            encrypted_text += indexChar(mult[2][0])
        elif iter == 3:
            mult = np.matmul(key, temp)  # 3x3 * 3x1 = 3x1
            mult[0][0] = mult[0][0] % 100
            mult[1][0] = mult[1][0] % 100
            mult[2][0] = mult[2][0] % 100
            encrypted_text += indexChar(mult[0][0])
            encrypted_text += indexChar(mult[1][0])
            encrypted_text += indexChar(mult[2][0])
        else:
            print("Something went wrong in the encryption function.")
    return encrypted_text


# Decrypts message in blocks of 3.
def decrypt(key, msg):
    temp = np.zeros((3, 1), dtype=np.int)
    decrypted_text = ''
    iter = 0
    # print("The encrypted text is: {}\n".format(msg))
    for c in msg:
        # print("Current symbol: ",c)
        if iter > 2:
            mult = np.matmul(key, temp)
            mult[0][0] = mult[0][0] % 100
            mult[1][0] = mult[1][0] % 100
            mult[2][0] = mult[2][0] % 100
            # print("0,0: {}\n1,0: {}\n2,0: {}\nData types: {}, {}, {}".format(mult[0][0],mult[1][0],mult[2][0],type(mult[0][0]),type(mult[1][0]),type(mult[2][0])))
            decrypted_text += indexChar(mult[0][0])
            decrypted_text += indexChar(mult[1][0])
            decrypted_text += indexChar(mult[2][0])
            iter = 0
        temp[iter][0] = charIndex(c)
        # print("Index of {} is {}.".format(c,charIndex(c)))
        iter += 1
    if iter > 0:  # Exited loop with partially or fully filled block of three values.
        if iter == 1:
            # single value in temp
            # print("Before mult: {}".format(temp[0][0]))
            mult = np.matmul(key, temp)
            # print("After mult & before mod: {}".format(mult[0][0]))
            mult[0][0] = mult[0][0] % 100
            # print("After mult & mod: {}".format(mult[0][0]))
            decrypted_text += indexChar(mult[0][0])
        elif iter == 2:
            # two values in temp
            mult = np.matmul(key, temp)
            mult[0][0] = mult[0][0] % 100
            mult[1][0] = mult[1][0] % 100
            decrypted_text += indexChar(mult[0][0])
            decrypted_text += indexChar(mult[1][0])
        elif iter == 3:
            mult = np.matmul(key, temp)
            mult[0][0] = mult[0][0] % 100
            mult[1][0] = mult[1][0] % 100
            mult[2][0] = mult[2][0] % 100
            decrypted_text += indexChar(mult[0][0])
            decrypted_text += indexChar(mult[1][0])
            decrypted_text += indexChar(mult[2][0])
        else:
            print("Something went wrong in the decryption function.")
    return decrypted_text


def main():  # for testing only. Will be removed in the final cipher file, as the GUI will do all the function calling.
    with open('test.txt') as f:
        msg = f.read().strip()

    key = genKey()
    # print("Original key matrix:\n",key)
    # print("Bad inverse with numpy:\n",np.linalg.inv(key))
    inverse_key = Matrix(key).inv_mod(100)
    inverse_key = np.array(inverse_key)
    inverse_key = inverse_key.astype(int)
    # print("The better inverse:\n",inverse_key)

    print("-------------------\nPlaintext length:\t{}\n".format(len(msg)))
    print("The plaintext is:\t{}\n".format(msg))
    ciphertext = encrypt(key, msg)
    print("Ciphertext:\t\t{}\n".format(ciphertext))

    decrypted_text = decrypt(inverse_key, ciphertext)
    print("Decrypted text:\t\t{}\n-------------------".format(decrypted_text))

    print(inverse_key)
    # for c in string.printable:
    #     print("{}: {}".format(string.printable.index(c),c))


#main()
