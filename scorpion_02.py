from sys import stdin



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
    
def decimalToBinary2(n):
    bnr = bin(int(n)).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 16:
        x += '0'
    bnr = x[::-1]
    return bnr



op1_rev=['10000', '10001', '10110', '11010', '11011', '11100']
op2_rev=['10111', '11101', '11110']
op3_rev=['11111', '01100', '01101', '01111']
op4_rev=['11000', '11001']
op5_rev=['10100', '10101']

mem_adds=["0000000000000000"]*256
pC=0
reg_val={'000':0, '001':0, '010':0, '011':0, '100':0, '101':0, '110':0, "111":"0000000000000000"}
inputs=[]


for i in stdin:
    inputs.append(i)

for i in range(len(inputs)):
    mem_adds[i]=inputs[i]


def mem_dump():
    for i in mem_adds:
        print(i)


def execute(sen,pC):
    op=sen[0:5]
    if op=="10000":         #  Add
        reg_val[sen[7:10]]=reg_val[sen[10:13]]+reg_val[sen[13:16]]
        if reg_val[sen[10:13]]+reg_val[sen[13:16]]>255:
            s=list(reg_val["111"])
            s[-4]=1
            reg_val["111"]=s
    if op=="10001":         #   Sub
        reg_val[sen[7:10]]=reg_val[sen[10:13]]-reg_val[sen[13:16]]
        if reg_val[sen[10:13]]-reg_val[sen[13:16]]<0:
            s=list(reg_val["111"])
            s[-4]=1
            reg_val["111"]=s
    if op=="10110":         #   Multiply
        reg_val[sen[7:10]]=reg_val[sen[10:13]]*reg_val[sen[13:16]]
        if reg_val[sen[10:13]]*reg_val[sen[13:16]]>255:
            s=list(reg_val["111"])
            s[-4]=1
            reg_val["111"]=s
    if op=="10111":         #   Divide    
        reg_val[sen[7:10]]=int(reg_val[sen[10:13]]/reg_val[sen[13:16]])
    if op=="10011":         #   Mov reg
        reg_val[sen[10:13]]=reg_val[sen[13:16]]
    if op=="10010":         #   Mov imm
        reg_val[sen[5:8]]=binaryToDecimal(sen[8:16])
    if op=="10100":         #   Load
        reg_val[sen[5:8]]=mem_adds[binaryToDecimal(sen[8:16])]
    if op=="10101":         #   Store
        mem_adds[binaryToDecimal(sen[8:16])]=reg_val[sen[5:8]]
    if op=="11000":         #   Right Shift
        reg_val[sen[5:8]]>>binaryToDecimal(sen[8:16])
    if op=="11001":         #   Left Shift
        reg_val[sen[5:8]]<<binaryToDecimal(sen[8:16])
    if op=="11010":         #   Exclusiive Or
        reg_val[sen[7:10]]=reg_val[sen[10:13]]^reg_val[sen[13:16]]
    if op=="11011":         #   Bitwise Or
        reg_val[sen[7:10]]=reg_val[sen[10:13]]|reg_val[sen[13:16]]
    if op=="11100":         #   Bitwise And
        reg_val[sen[7:10]]=reg_val[sen[10:12]]&reg_val[sen[13:16]]
    if op=="11110":         #   Compare And Flag
        if reg_val["111"]==reg_val[sen[13:16]]:
            s=list(reg_val["111"])
            s[-1]=1
            reg_val["111"]=s
        elif reg_val["111"]>reg_val[sen[13:16]]:
            s=list(reg_val["111"])
            s[-2]=1
            reg_val["111"]=s
        elif reg_val["111"]<reg_val[sen[13:16]]:
            s=list(reg_val["111"])
            s[-3]=1
            reg_val["111"]=s
    if op=="11111":         #   Unconditional Jump
        pC=int(binaryToDecimal(sen[8:16]))
    if op=="01100":         #   Jump If  less than
        if reg_val("111")[-3]==1:
            pC=int(binaryToDecimal(sen[8:16]))
    if op=="01101":         #   Jump If greater than
        if reg_val("111")[-2]==1:
            pC=int(binaryToDecimal(sen[8:16]))
    if op=="01111":         #   Jump If  equal to
        if reg_val("111")[-1]==1:
            pC=int(binaryToDecimal(sen[8:16]))
    if op=="01010":
        pC=255

# Executing

while (pC!=len(inputs)):
    execute(mem_adds[pC],pC)
    pC+=1
    mem_dump()
    # print(mem_adds)
    print(reg_val)
