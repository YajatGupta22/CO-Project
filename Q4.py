# importing the required module
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from scipy.stats import expon

mem_acc=[]

import sys

memory = {}


def bit_16(n):
    return '{0:016b}'.format(n)


def bit_8(n):
    return '{0:08b}'.format(n)


def binaryToDecimal(x):
    return int(x, 2)


reg_val = {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, "111": 0}

pc = 0


def dump():
    for reg in reg_val.keys():
        print(bit_16(reg_val[reg]), end=" ")


def flag_reset():
    reg_val["111"] = 0

# inputs=["1001000100000100","1001001000000100","1111000000001010","1001100000111011","1001010000000001","1111000000011100","0110100000000111","0101000000000000"]
inputs=[]

for line in sys.stdin:
    if line!="" and line!="\n":
        inputs.append(line.strip())

while (inputs[pc] != "0101000000000000"):
    # print(bit_8(pc), end=" ")
    inst = inputs[pc]
    mem_acc.append(bit_8(pc))
    op_code = inst[:5]
    reg1 = inst[7:10]
    reg2 = inst[10:13]
    reg3 = inst[13:]
    if (op_code == "10000"):  # add
        reg_val[reg1] = reg_val[reg2] + reg_val[reg3]
        if reg_val[reg1] > 65535:
            reg_val[reg1] = reg_val[reg1] % 65536
            reg_val["111"] = 8
        else:
            flag_reset()
        pc += 1
    if (op_code == "10001"):  # sub
        reg_val[reg1] = reg_val[reg2] - reg_val[reg3]
        if reg_val[reg1] < 0:
            reg_val[reg1] = 0
            reg_val["111"] = 8
        else:
            flag_reset()
        pc += 1
    if (op_code == "10110"):  # mul
        reg_val[reg1] = reg_val[reg2] * reg_val[reg3]
        if reg_val[reg1] > 65535:
            reg_val[reg1] = reg_val[reg1] % 65536
            reg_val["111"] = 8
        else:
            flag_reset()
        pc += 1
    if (op_code == "11010"):  # xor
        reg_val[reg1] = reg_val[reg2] ^ reg_val[reg3]
        flag_reset()
        pc += 1
    if (op_code == "11011"):  # or
        reg_val[reg1] = reg_val[reg2] or reg_val[reg3]
        flag_reset()
        pc += 1
    if (op_code == "11100"):  # and
        reg_val[reg1] = reg_val[reg2] and reg_val[reg3]
        flag_reset()
        pc += 1
    reg = inst[5:8]
    imm = binaryToDecimal(inst[8:])
    if (op_code == "10010"):  # movi
        reg_val[reg] = imm
        flag_reset()
        pc += 1
    if (op_code == "11000"):  # rs
        reg_val[reg] = reg_val[reg] >> imm
        flag_reset()
        pc += 1
    if (op_code == "11001"):  # ls
        reg_val[reg] = reg_val[reg] << imm
        if reg_val[reg] > 65535:
            reg_val[reg] = reg_val[reg] % 65536
            reg_val["111"] = 8
        else:
            flag_reset()
        pc += 1
    reg1 = inst[10:13]
    reg2 = inst[13:]
    if (op_code == "10011"):  # movr
        reg_val[reg2] = reg_val[reg1]
        flag_reset()
        pc += 1
    if (op_code == "10111"):  # divide
        reg_val["000"] = reg_val[reg1] // reg_val[reg2]
        reg_val["001"] = reg_val[reg1] % reg_val[reg2]
        flag_reset()
        pc += 1
    if (op_code == "11101"):  # invert
        reg_val[reg2] = 65535 - reg_val[reg1]
        flag_reset()
        pc += 1
    if (op_code == "11110"):  # compare
        if (reg_val[reg1] > reg_val[reg2]):
            reg_val["111"] = 2
        if (reg_val[reg1] < reg_val[reg2]):
            reg_val["111"] = 4
        if (reg_val[reg1] == reg_val[reg2]):
            reg_val["111"] = 1
        pc += 1
    reg = inst[5:8]
    mem = inst[8:]
    if (op_code == "10100"):  # load
        if (mem not in memory.keys()):
            memory[mem] = 0
        reg_val[reg] = memory[mem]
        flag_reset()
        pc += 1
    if (op_code == "10101"):  # store
        memory[mem] = reg_val[reg]
        flag_reset()
        pc += 1
    mem = binaryToDecimal(inst[8:])
    if op_code == "11111":  # jmp
        flag_reset()
        pc = mem

    if op_code == "01100":  # jlt
        if (reg_val["111"] == 4):
            pc = mem
        else:
            pc += 1
        flag_reset()
    if op_code == "01101":  # jgt
        if (reg_val["111"] == 2):
            pc = mem
        else:
            pc += 1
        flag_reset()
    if op_code == "01111":  # je
        if (reg_val["111"] == 1):
            pc = mem
        else:
            pc += 1
        flag_reset()
    # dump()
    # print()

flag_reset()
# print(bit_8(pc), end=" ")
# dump()
# print()
# for i in range(0, 256):
#     if (i < len(inputs)):
#         print(inputs[i])
#     else:
#         # print("0000000000000000")

plt.scatter( range(1,(len(mem_acc))+1),mem_acc) 
plt.show() 
