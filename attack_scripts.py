# TODO: make altered cipher file to generate a ciphertext that can be used here with only lowercase letters.
import string
import time
from itertools import combinations_with_replacement
import numpy as np
saveKeyHere = np.empty((3,3), dtype=int)
def bruteForceKeyGeneration():
    count = 0
    # test = np.array([[3,2,22],[24,6,21],[22,19,23]])
    x = np.zeros((3,3), dtype=int)
    d_msg = ""
    saveKeyHere = np.zeros((3,3), dtype=int)
    for comb in combinations_with_replacement(range(26),9):
        x = np.zeros((3,3), dtype=int)
        x.flat[:] = comb
        count += 1


        d_msg = decrypt(x,"kzaepgqvcsri")
        if d_msg == "catsaregreat":
            saveKeyHere = x
            break
        else:
            continue
    # d_msg = decrypt(test,"kzaepgqvcsri")
    print("\n\nTotal number of keys checked: {}\n\nYour plaintext is: catsaregreat\n\nYour decrypted message is: {}".format(count,d_msg))
    print(saveKeyHere)
    return saveKeyHere

def charIndex(char):
    return string.ascii_lowercase.index(char)
def indexChar(index):
    return string.ascii_lowercase[index]


def decrypt(key,msg):
    temp = np.zeros((3,1), dtype=np.int)
    decrypted_text = ''
    iter = 0
    # print("The encrypted text is: {}\n".format(msg))
    for c in msg:
        # print("Current symbol: ",c)
        if iter > 2:
            mult = np.matmul(key,temp)
            mult[0][0] = mult[0][0] % 26
            mult[1][0] = mult[1][0] % 26
            mult[2][0] = mult[2][0] % 26
            # print("0,0: {}\n1,0: {}\n2,0: {}\nData types: {}, {}, {}".format(mult[0][0],mult[1][0],mult[2][0],type(mult[0][0]),type(mult[1][0]),type(mult[2][0])))
            decrypted_text += indexChar(mult[0][0])
            decrypted_text += indexChar(mult[1][0])
            decrypted_text += indexChar(mult[2][0])
            iter = 0
        temp[iter][0] = charIndex(c)
        # print("Index of {} is {}.".format(c,charIndex(c)))
        iter += 1
    if iter > 0: #Exited loop with partially or fully filled block of three values.
        if iter == 1:
            #single value in temp
            # print("Before mult: {}".format(temp[0][0]))
            mult = np.matmul(key,temp)
            # print("After mult & before mod: {}".format(mult[0][0]))
            mult[0][0] = mult[0][0] % 26
            # print("After mult & mod: {}".format(mult[0][0]))
            decrypted_text += indexChar(mult[0][0])
        elif iter == 2:
            #two values in temp
            mult = np.matmul(key,temp)
            mult[0][0] = mult[0][0] % 26
            mult[1][0] = mult[1][0] % 26
            decrypted_text += indexChar(mult[0][0])
            decrypted_text += indexChar(mult[1][0])
        elif iter == 3:
            mult = np.matmul(key,temp)
            mult[0][0] = mult[0][0] % 26
            mult[1][0] = mult[1][0] % 26
            mult[2][0] = mult[2][0] % 26
            decrypted_text += indexChar(mult[0][0])
            decrypted_text += indexChar(mult[1][0])
            decrypted_text += indexChar(mult[2][0])
        else:
            print("Something went wrong in the decryption function.")
    # print(decrypted_text)
    return decrypted_text
start2 = time.time()
bruteForceKeyGeneration()
end2 = time.time()
print("Total execution time: {} seconds".format(end2-start2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# import sys
# from itertools import permutations
# from sympy.utilities.iterables import multiset_permutations
# from numpy.lib import recfunctions as rfn
# #http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/
# #All values found in abouve link
# bigramFrequencies = np.array([
#    #A 0
#     [1721143, 8775582, 17904683, 14877234, 815963, 5702567, 8809266, 2225270, 13974919, 870262, 5137311, 38211584, 15975981, 69775179, 749566, 8553911, 315068, 42353262, 37773878, 48274564, 4884168, 8288885, 3918960, 660826, 11523416, 768359],
#     #B 1
#     [8867461,689158, 320380, 141752, 19468489, 75352, 40516, 154489, 4356462, 282608, 26993, 6941044, 191807, 106125, 8172395, 115161, 5513, 4621080, 1409672, 428276, 8113271, 120081, 140189, 3021, 5232074, 8132],
#     #C 2
#     [19930754, 298053, 3026492, 358435, 19803619, 267630, 181590, 20132750, 8446084, 41526, 7205091, 5683204, 285942, 188046, 26737101, 382923, 157546, 5514347, 1381608, 11888752, 4604045, 94224, 257253, 5300, 1145316, 57914],
#     #D 3
#     [17584055, 6106719, 3782481, 4001275, 27029835, 4033878, 2442139, 4585765, 21673998, 799366, 525744, 3050945, 3544905, 2840522, 13120322, 3145043, 283314, 5701879, 10429887, 15759673, 5861311, 1238565, 4906814, 27413, 2218040, 98038],
#     #E 4
#     [43329810, 9738798, 25775798, 46647960, 18497942, 13252227, 8286463, 7559141, 16026915, 1256993, 2411639, 23092248, 18145294, 48991276, 13524186, 14024377, 1461436, 77134382, 57070453, 32872552, 3674130, 10574011, 14776406, 5649363, 7528342, 465466],
#     #F 5
#     [8357929, 888155, 1570791, 748027, 8529289, 6085519, 637758, 1507604, 11993833, 269865, 228905, 2890839, 1251312, 534362, 18923772, 1199845, 47504, 8339376, 2047416, 13696078, 3138900, 244685, 1005903, 19313, 789961, 31186],
#     #G 6
#     [11239788, 1184377, 1299541, 879792, 14425023, 1465290, 1468286, 9880399, 7103140, 176947, 163830, 2576787, 1178511, 2426429, 8188708, 1215204, 59750, 6989963, 3920675, 7347990, 3768430, 186777, 1567991, 14778, 979804, 28514],
#     #H 7
#     [35971841, 1014004, 1441057, 828755, 100689263, 834284, 429607, 1329998, 27495342, 189906, 210385, 1169468, 1353001, 1383958, 19729026, 978649, 101241, 3843001, 2462026, 8351551, 2771830, 197539, 1403223, 7526, 1446451, 37066],
#     #I 8
#     [10002012, 2598444, 21468412, 12896787, 12505546, 5740414, 9530574, 610683, 607124, 219128, 2585124, 17877600, 10544422, 87674002, 21210160, 3348621, 291635, 11681353, 37349981, 37938534, 576683, 9129232, 922059, 879360, 98361, 1865802],
#     #J 9
#     [1712763, 19380, 24770, 21903, 1487348, 12640, 12023, 20960, 357577, 16085, 13967, 12149, 22338, 14452, 2721345, 34520, 722, 80471, 39326, 20408, 2924815, 8925, 16083, 747, 5723, 2859],
#     #K 10
#     [2833038, 457860, 420017, 277982, 10650670, 537342, 209266, 650095, 5814357, 76816, 118811, 846309, 485617, 1903836, 1758001, 375653, 13905, 507020, 3227333, 1443985, 506618, 73184, 719633, 5083, 553296, 11192],
#     #L 11
#     [23178317, 2463693, 2328063, 10245579, 30383262, 2702522, 926472, 1274048, 23291169, 218362, 1164186, 24636875, 2216514, 752316, 15596310, 2543957, 77148, 1505092, 8675452, 6817273, 4402940, 1238287, 1836811, 15467, 13742031, 57314],
#     #M 12
#     [21828378, 4121764, 1101727, 481126, 27237733, 715087, 285133, 710864, 12168944, 134263, 111041, 478528, 3730508, 558397, 12950768, 7835172, 21358, 660619, 3922855, 3055946, 3755834, 136314, 937621, 14250, 1949129, 18271],
#     #N 13
#     [23547524, 3602692, 15214623, 46194306, 27331675, 4950333, 38567365, 3915410, 17452104, 1342735, 3043200, 3692985, 3796928, 5180899, 18894111, 2968126, 217422, 2393580, 21306421, 50701084, 3732602, 2194534, 4215967, 74844, 4343290, 266461],
#     #O 14
#     [6554221, 6212512, 7646952, 7610214, 2616308, 30540904, 4163126, 3254659, 5336616, 661082, 3397570, 13726491, 21066156, 56915252, 10168856, 10459455, 122677, 45725191, 13596265, 20088048, 31112284, 7350014, 14610429, 650078, 1932892, 228556],
#     #P 15
#     [12068709, 369336, 400308, 273162, 15573318, 418168, 211133, 2825344, 5559210, 47043, 83017, 9812226, 931225, 131645, 11917535, 4873393, 18607, 13191182, 2377036, 3812475, 3858148, 48105, 530411, 6814, 396147, 9697],
#     #Q 16
#     [73527, 27307, 10667, 8678, 6020, 8778, 2567, 12273, 73387, 1342, 2023, 9603, 12315, 3808, 9394, 6062, 2499, 5975, 20847, 16914, 4169424, 4212, 34669, 765, 4557, 280],
#     #R 17
#     [28645577, 3346212, 6974063, 9025637, 60923600, 3436232, 4645938, 2968706, 27634643, 518157, 4491400, 4803246, 7377989, 7064635, 29230770, 3588188, 156933, 5896212, 21237259, 21456059, 5330557, 2692445, 3348005, 38654, 8788539, 113432],
#     #S 18
#     [30080131, 5553684, 10800636, 3842250, 31532272, 6073995, 2043770, 16773127, 25758841, 704442, 2321888, 4965012, 5580755, 4157990, 23903631, 10570626, 800346, 3513808, 18915696, 54018399, 10031005, 882083, 8673234, 50975, 2214270, 79840],
#     #T 19
#     [26147593, 3815459, 5196817, 2346516, 42295813, 3368452, 1530045, 116997844, 42888666, 559473, 610333, 5403137, 3759861, 1782119, 46115188, 3070427, 159111, 15821226, 18922522, 19367472, 8477495, 698150, 8910254, 28156, 8008918, 280007],
#     #U 20
#     [4589997, 2990868, 5742385, 3499535, 4927837, 701892, 4832325, 339341, 3481482, 88168, 514873, 10173468, 4389720, 15237699, 649906, 5306948, 23386, 17341717, 15699353, 15137169, 63043, 212051, 352732, 144814, 531960, 153736],
#     #V 21
#     [4111375, 29192, 59024, 85611, 29320973, 28090, 25585, 30203, 9380037, 11432, 11469, 49032, 35024, 33082, 2253292, 62577, 1488, 96416, 204093, 62912, 82830, 22329, 45608, 3192, 233082, 2633],
#     #W 22
#     [16838794, 394820, 448394, 432646, 13185116, 336213, 139890, 11852909, 15213018, 99435, 148964, 657782, 505687, 3649615, 9106647, 321746, 16245, 1226755, 1988727, 1301293, 180884, 63930, 674610, 4678, 553647, 52836],
#     #X 23
#     [904148, 94041, 697995, 60101, 653947, 113031, 39289, 166599, 1024736, 10629, 13651, 59585, 127492, 34734, 211173, 1840696, 5416, 90046, 154347, 1509969, 147533, 31117, 119322, 35052, 94329, 2082],
#     #Y 24
#     [7239548, 2696786, 3128053, 2122337, 6499305, 2305244, 1049082, 2291273, 4461214, 378679, 391953, 2013939, 2516273, 1485655, 9088497, 2581863, 87953, 2021939, 7539621, 6714151, 695512, 411487, 3379064, 16945, 332973, 78281],
#     #Z 25
#     [929119, 50652, 41037, 32906, 1709871, 28658, 26369, 107639, 644035, 7167, 24262, 80039, 46034, 24241, 424016, 30389, 5773, 32685, 94993, 56955, 113538, 14339, 68865, 2463, 105871, 221275]
#     ])
# #Gives every possible mapping for letters
# # for perrmuntated array the possition of the value represents the original letter, and the value represents the current test value
# # for example if the first value is 5, that means postion 0 value 5 or A is now mapped to F
#
# def permutateAlphabet():
#     normalAlphabet = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22, 23,24,25])
#     count = 0
#     for e in multiset_permutations(normalAlphabet):
#         e
#         count = count + 1
# #Tester for permutateAlphabet() for quicker run times
# def randompermutateAlphabet():
#     return np.random.permutation(26)
# realPlaintext = ''
# saveBigSum = 0
# def breakString(ciphertext, fistChar, secChar):
#     val1 = 0
#     val2 = 0
#     val3 = 0
#     bigSum = 0
#     rA = randompermutateAlphabet()
#     char1 = 'a'
#     char2 = 'a'
#     plaintext = ''
#     newChar = ''
#     newCharVal = 0
#     newCount = 0
#     while (secChar <= len(ciphertext)):
#         r1 = rA[val1]
#         r2 = rA[val2]
#         if (" " not in ciphertext[fistChar:secChar]):
#             #print ciphertext[fistChar:secChar]
#             if (ciphertext[fistChar] == "a"):
#                 val1 = 0
#             if (ciphertext[fistChar] == "b"):
#                 val1 = 1
#             if (ciphertext[fistChar] == "c"):
#                 val1 = 2
#             if (ciphertext[fistChar] == "d"):
#                 val1 = 3
#             if (ciphertext[fistChar] == "e"):
#                 val1 = 4
#             if (ciphertext[fistChar] == "f"):
#                 val1 = 5
#             if (ciphertext[fistChar] == "g"):
#                 val1 = 6
#             if (ciphertext[fistChar] == "h"):
#                 val1 = 7
#             if (ciphertext[fistChar] == "i"):
#                 val1 = 8
#             if (ciphertext[fistChar] == "j"):
#                 val1 = 9
#             if (ciphertext[fistChar] == "k"):
#                 val1 = 10
#             if (ciphertext[fistChar] == "l"):
#                 val1 = 11
#             if (ciphertext[fistChar] == "m"):
#                 val1 = 12
#             if (ciphertext[fistChar] == "n"):
#                 val1 = 13
#             if (ciphertext[fistChar] == "o"):
#                 val1 = 14
#             if (ciphertext[fistChar] == "p"):
#                 val1 = 15
#             if (ciphertext[fistChar] == "q"):
#                 val1 = 16
#             if (ciphertext[fistChar] == "r"):
#                 val1 = 17
#             if (ciphertext[fistChar] == "s"):
#                 val1 = 18
#             if (ciphertext[fistChar] == "t"):
#                 val1 = 19
#             if (ciphertext[fistChar] == "u"):
#                 val1 = 20
#             if (ciphertext[fistChar] == "v"):
#                 val1 = 21
#             if (ciphertext[fistChar] == "w"):
#                 val1 = 22
#             if (ciphertext[fistChar] == "x"):
#                 val1 = 23
#             if (ciphertext[fistChar] == "y"):
#                 val1 = 24
#             if (ciphertext[fistChar] == "z"):
#                 val1 = 25
#             if (ciphertext[secChar -1] == "a"):
#                 val1 = 0
#             if (ciphertext[secChar-1] == "b"):
#                 val2 = 1
#             if (ciphertext[secChar-1] == "c"):
#                 val2 = 2
#             if (ciphertext[secChar-1] == "d"):
#                 val2 = 3
#             if (ciphertext[secChar-1] == "e"):
#                 val2 = 4
#             if (ciphertext[secChar-1] == "f"):
#                 val2 = 5
#             if (ciphertext[secChar-1] == "g"):
#                 val2 = 6
#             if (ciphertext[secChar-1] == "h"):
#                 val2 = 7
#             if (ciphertext[secChar-1] == "i"):
#                 val2 = 8
#             if (ciphertext[secChar-1] == "j"):
#                 val2 = 9
#             if (ciphertext[secChar-1] == "k"):
#                 val2 = 10
#             if (ciphertext[secChar-1] == "l"):
#                 val2 = 11
#             if (ciphertext[secChar-1] == "m"):
#                 val2 = 12
#             if (ciphertext[secChar-1] == "n"):
#                 val2 = 13
#             if (ciphertext[secChar-1] == "o"):
#                 val2 = 14
#             if (ciphertext[secChar-1] == "p"):
#                 val2 = 15
#             if (ciphertext[secChar-1] == "q"):
#                 val2 = 16
#             if (ciphertext[secChar-1] == "r"):
#                 val2 = 17
#             if (ciphertext[secChar-1] == "s"):
#                 val2 = 18
#             if (ciphertext[secChar-1] == "t"):
#                 val2 = 19
#             if (ciphertext[secChar-1] == "u"):
#                 val2 = 20
#             if (ciphertext[secChar-1] == "v"):
#                 val2 = 21
#             if (ciphertext[secChar-1] == "w"):
#                 val2 = 22
#             if (ciphertext[secChar-1] == "x"):
#                 val2 = 23
#             if (ciphertext[secChar-1] == "y"):
#                 val2 = 24
#             if (ciphertext[secChar-1] == "z"):
#                 val2 = 25
#             #print(str(val1) + " " + str(val2))
#             #print bigramFrequencies[val1][val2]
#
#             #print("chars: " + str(char1) + str(char2))
#             bigSum = bigSum + bigramFrequencies[rA[val1]][rA[val2]]
#             for c in ciphertext:
#                 if(c == 'a'):
#                     val3 = 0
#                 if(c == 'b'):
#                     val3 = 1
#                 if(c == 'c'):
#                     val3 = 2
#                 if(c == 'd'):
#                     val3 = 3
#                 if(c == 'e'):
#                     val3 = 4
#                 if(c == 'f'):
#                     val3 = 5
#                 if(c == 'g'):
#                     val3 = 6
#                 if(c == 'h'):
#                     val3 = 7
#                 if(c == 'i'):
#                     val3 = 8
#                 if(c == 'j'):
#                     val3 = 9
#                 if(c == 'k'):
#                     val3 = 10
#                 if(c == 'l'):
#                     val3 = 11
#                 if(c == 'm'):
#                     val3 = 12
#                 if(c == 'n'):
#                     val3 = 13
#                 if(c == 'o'):
#                     val3 = 14
#                 if(c == 'p'):
#                     val3 = 15
#                 if(c == 'q'):
#                     val3 = 16
#                 if(c == 'r'):
#                     val3 = 17
#                 if(c == 's'):
#                     val3 = 18
#                 if(c == 't'):
#                     val3 = 19
#                 if(c == 'u'):
#                     val3 = 20
#                 if(c == 'v'):
#                     val3 = 21
#                 if(c == 'w'):
#                     val3 = 22
#                 if(c == 'x'):
#                     val3 = 23
#                 if(c == 'y'):
#                     val3 = 24
#                 if(c == 'z'):
#                     val3 = 25
#                 newCharVal = rA[val3]
#                 #print newCharVal
#                 if(newCharVal == 0):
#                     newChar = 'a'
#                 if(newCharVal == 1):
#                     newChar = 'b'
#                 if(newCharVal == 2):
#                     newChar = 'c'
#                 if(newCharVal == 3):
#                     newChar = 'd'
#                 if(newCharVal == 4):
#                     newChar = 'e'
#                 if(newCharVal == 5):
#                     newChar = 'f'
#                 if(newCharVal == 6):
#                     newChar = 'g'
#                 if(newCharVal == 7):
#                     newChar = 'h'
#                 if(newCharVal == 8):
#                     newChar = 'i'
#                 if(newCharVal == 9):
#                     newChar = 'j'
#                 if(newCharVal == 10):
#                     newChar = 'k'
#                 if(newCharVal == 11):
#                     newChar = 'l'
#                 if(newCharVal == 12):
#                     newChar = 'm'
#                 if(newCharVal == 13):
#                     newChar = 'n'
#                 if(newCharVal == 14):
#                     newChar = 'o'
#                 if(newCharVal == 15):
#                     newChar = 'p'
#                 if(newCharVal == 16):
#                     newChar = 'q'
#                 if(newCharVal == 17):
#                     newChar = 'r'
#                 if(newCharVal == 18):
#                     newChar = 's'
#                 if(newCharVal == 19):
#                     newChar = 't'
#                 if(newCharVal == 20):
#                     newChar = 'u'
#                 if(newCharVal == 21):
#                     newChar = 'v'
#                 if(newCharVal == 22):
#                     newChar = 'w'
#                 if(newCharVal == 23):
#                     newChar = 'x'
#                 if(newCharVal == 24):
#                     newChar = 'y'
#                 if(newCharVal == 25):
#                     newChar = 'z'
#                 plaintext = plaintext + str(newChar)
#         fistChar = fistChar + 1
#         secChar = secChar + 1
#     print(plaintext[:len(ciphertext)])
#     realPlaintext = plaintext[:len(ciphertext)]
#     print(bigSum)
#     saveBigSum = bigSum
#
#
# #TODO
# #Add storge place for bigSum and realPlaintext
# #print the highest 5? b values of bigSum with coresponding realPlaintext
#
# ciphertext = "this word"
# fistChar = 0
# secChar = 2
# j = 0
# while (j <= 10):
#     breakString(ciphertext, fistChar, secChar)
#     j = j + 1
