from sys import flags, stdin

def decimalToBinary(n):
    bnr = bin(int(n)).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr

def binaryToDecimal(binary):
    binary=int(binary)
    decimal=0
    i = 0
    while(binary != 0):
        dec = binary % 10
        decimal+=dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal 
    


op1_rev=['10000', '10001', '10110', '11010', '11011', '11100']
op2_rev=['10111', '11101', '11110']
op3_rev=['11111', '01100', '01101', '01111']
op4_rev=['11000', '11001']
op5_rev=['10100', '10101']

mem_adds=["00000000"]*256
pC=0
reg_val={'000':0, '001':0, '010':0, '011':0, '100':0, '101':0, '110':0, "111":0}
inputs=[]


for i in stdin:
    inputs.append(i)

def mem_dump():
    for i in mem_adds:
        print(i)


def execute(sen):
    op=sen[0:4]
    if op=="10000":         #  Add
        reg_val[sen[7:9]]=reg_val[sen[10:12]]+reg_val[sen[13:15]]
    if op=="10001":         #   Sub
        reg_val[sen[7:9]]=reg_val[sen[10:12]]-reg_val[sen[13:15]]
    if op=="10110":         #   Multiply
        reg_val[sen[7:9]]=reg_val[sen[10:12]]*reg_val[sen[13:15]]
    if op=="10111":         #   Divide    
        reg_val[sen[7:9]]=int(reg_val[sen[10:12]]/reg_val[sen[13:15]])
    if op=="10011":         #   Mov reg
        reg_val[sen[10:12]]=reg_val[sen[13:15]]
    if op=="10010":         #   Mov imm
        reg_val[sen[5:7]]=decimalToBinary(sen[8:15])
    if op=="10100":         #   Load





