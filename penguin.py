from sys import stdin

# Changes an integer into 8 bit binary and returns the value as a string
def decimalToBinary(n):
    assert n[0]=="$"," Error! ,integer not declared with a '$' sign" 
    n = int(str(n)[1::])
    bnr = bin(int(n)).replace('0b', '')
    x = bnr[::-1]  # this reverses the  array
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr
def decimalToBinary2(n):
    bnr = bin(int(n)).replace('0b', '')
    x = bnr[::-1]  # this reverses an array
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr

#   Checks if all the variables are declared at the begining and if they are not being used before declaration
def check_var(inp_lists):
    var_list=[]
    var_index=[]
    for i in range(0,len(inp_lists)):
        inp_lists[i]=inp_lists[i].split()
        if(inp_lists[i][0]=="var"):
            var_list.append(inp_lists[i][-1])
            var_index.append(i)
    for i in inp_lists:
        if((i[0]=="st" or i[0]=="ld") and i[-1].isalpha() and i[-1] not in var_list):
            assert False,"variable used before reference"
    if sorted(var_index) != list(range(0, max(var_index)+1)):
        assert False,"Variables not declared at beginning"
    else:
        return True
def check_hlt(inp_lists):
    assert (inp_lists[-1]!="hlt"),"hlt not in the last line"
    for i in  range(len(inp_lists)):
        if inp_lists[i]=="hlt" and i!=len(inp_lists):
            assert False,"hlt declared before the last line"
            
# Dictionary of operands , registers, and variables
dict0 = {"add": "10000", "sub": "10001", "ld": "10100", "st": "10101", "mul": "10110",
         "div": "10111", "rs": "11000", "ls": "11001", "xor": "11010", "or": "11011", "and": "11100", "not": "11101",
         "cmp": "11110", "jmp": "11111", "jlt": "01110", "jgt": "01101", "je": "01111", "hlt": "01010",
         "mov":"erprev"
         }
reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"
       }
labels={}
# Initialising some objects
list_inputs=[]
sen="hihihihi"
variables = {}
mem_adrr={}
outputs=[]
mem1=0


# Dividing the operations into 5 basic categeries on basis of different things
op1 = ["add", "sub", "mul", "xor", "or", "and"]
op2 = ["div", "not", "cmp"]
op3 = ["jmp", "jlt", "jgt", "je"]
op4 = ["rs", "ls"]
op5 = ["ld", "st"]


# This function  converts a proper instruction into 16-bit binary assembly code
def convert(sen):
    sen_list = [x for x in sen.split()]
    assert sen_list[0] in dict0 , "Syntax Error! Operator not present in ISO"
    if sen_list[0] != "mov":
        sen_list_assem = [dict0[sen_list[0]]]
    else:
        if sen_list[2] in reg:
            sen_list_assem = ["10010"]
        else:
            sen_list_assem = ["10011"]
    if sen_list[0] in op1:
        sen_list_assem.append("00")
        for i in range(3):
            assert sen_list[i+1] in reg, "Syntax Error! register not present in ISO"
            sen_list_assem.append(reg[sen_list[i + 1]])
    elif sen_list[0] in op2:
        sen_list_assem.append("00000")
        for i in range(2):
            assert sen_list[i+1] in reg, "Syntax Error! register not present in ISO"
            sen_list_assem.append(reg[sen_list[i + 1]])
    elif sen_list[0] in op3:
        # assert sen_list[1] in mem_adrr,"Error!,wrong value for  not label"
        assert sen_list[0] not in labels,"Error!,wrong name for  not label"
        sen_list_assem.append("000")
        # sen_list_assem.append(str(sen_list[1]))
        sen_list_assem.append(labels[sen_list[1]])
    elif sen_list[0] in op4:
        assert sen_list[1] in reg, "Syntax Error! register not present in ISO"
        sen_list_assem.append(reg[sen_list[1]])
        assert  0<int(sen_list[2][1::])<256,"Error! , the illiegal immideate value"
        sen_list_assem.append(decimalToBinary(sen_list[2]))
    elif sen_list[0] in op5:
        assert sen_list[1] in reg, "Syntax Error! register not present in ISO"
        sen_list_assem.append(reg[sen_list[1]])
        assert sen_list[2] in variables,"Error!, Variable not declared"
        sen_list_assem.append(variables[sen_list[2]])
    elif sen_list[0] == "hlt":
        sen_list_assem.append("00000000000")
    elif sen_list[0] == "mov":
        if sen_list[2] not in reg:
            assert sen_list[1] in reg, "Syntax Error! register not present in ISO"
            sen_list_assem.append(reg[sen_list[1]])
            assert  0<int(sen_list[2][1::])<256,"Error! , the illiegal immideate value"
            sen_list_assem.append(decimalToBinary(sen_list[2]))
        else:
            sen_list_assem.append("00000")
            assert sen_list[1] in reg, "Syntax Error! register not present in ISO"
            sen_list_assem.append(reg[sen_list[1]])
            assert sen_list[2] in reg, "Syntax Error! register not present in ISO"
            sen_list_assem.append(reg[sen_list[2]])
    outputs.append("".join(sen_list_assem))

# Taking inputs in loops and saving them in list_inputs
for line in stdin:
    if line!="":
        list_inputs.append(line)
# while(sen!="hlt"):
#     sen=input()
#     if sen!="":
#         list_inputs.append(sen)

list_inputs_check=list_inputs.copy()
list_inputs_check_2=list_inputs.copy()
check_var(list_inputs_check)
check_hlt(list_inputs_check_2)

# Converting the inputs and printting them
for sen in list_inputs:
    if sen.split()[0] != "var":
        if sen.split()[0][-1]==':':
            labels[sen.split()[0][0:-1]]=decimalToBinary2(mem1)
            mem1+=1
        else:    
            mem_adrr[sen]=decimalToBinary2(mem1)
            mem1+=1
for sen in list_inputs:
    if sen.split()[0] == "var":
        assert sen.split()[1] not in variables,"Variable redeclaration error"
        variables[sen.split()[1]]=decimalToBinary2(mem1)
        mem1+=1
assert mem1<257,"Memory overflow Error! , too many instructions for the ISO to handle"
for sen in list_inputs:
    if sen.split()[0] != "var" and sen.split()[0][0:-1] not in labels:
        convert(sen)
    elif sen.split()[0][::-1][0]==":":
        label_inp=sen.split()
        label_inp.pop(0)
        r=" ".join(label_inp)
        convert(r)

# # Printing the output
for x in outputs:
    print(x)
