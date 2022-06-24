def decimalToBinary(n):
    bnr = bin(int(n)).replace('0b', '')
    x = bnr[::-1]  # this reverses an array
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr


dict0 = {"add": "10000", "sub": "10001", "mov1": "10010", "mov2": "10011", "ld": "10100", "st": "10101", "mul": "10110",
         "div": "10111", "rs": "11000", "ls": "11001", "xor": "11010", "or": "11011", "and": "11100", "not": "11101",
         "cmp": "11110", "jmp": "11111", "jlt": "01110", "jgt": "01101", "je": "01111", "hlt": "01010"
         }

reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"
       }

op1 = ["add", "sub", "mul", "xor", "or", "and"]
op2 = ["div", "not", "cmp"]
op3 = ["jmp", "jlt", "jgt", "je"]
op4 = ["rs", "ls"]
op5 = ["ld", "st"]

sen = input()
sen_list = [x for x in sen.split()]

if sen_list[0] != "mov":
    sen_list_assem = [dict0[sen_list[0]]]
else:
    if (sen_list[2] in reg):
        sen_list_assem = [dict0["mov2"]]
    else:
        sen_list_assem = [dict0["mov1"]]

if sen_list[0] in op1:
    sen_list_assem.append("00")
    for i in range(3):
        sen_list_assem.append(reg[sen_list[i + 1]])
elif sen_list[0] in op2:
    sen_list_assem.append("00000")
    for i in range(2):
        sen_list_assem.append(reg[sen_list[i + 1]])
elif sen_list[0] in op3:
    sen_list_assem.append(sen_list[1])
elif sen_list[0] in op4:
    sen_list_assem.append(reg[sen_list[1]])
    sen_list_assem.append(decimalToBinary(sen_list[2]))
elif sen_list[0] == "hlt":
    sen_list_assem.append("00000000000")
elif sen_list[0] == "mov":
    if sen_list[2] not in reg:
        sen_list_assem.append(reg[sen_list[1]])
        sen_list_assem.append(decimalToBinary(sen_list[2]))
    else:
        sen_list_assem.append("00000")
        sen_list_assem.append(reg[sen_list[1]])
        sen_list_assem.append(reg[sen_list[2]])
elif sen_list[0] in op5:
    sen_list_assem.append("000")
    sen_list_assem.append(sen_list[2])

print(*sen_list_assem, sep="")
# print(len(dict0) - len(op1 + op2 + op3 + op4+op5) - 3)
# print(1001001001100100 == 1001001001100100)
# print([x for x in dict0 if x not in op1 + op2 + op3 + op4+op5])
