def var(l):
    var_list=[]
    var_index=[]
    for i in range(0,len(l)):
        l[i]=l[i].split()
        if(l[i][0]=="var"):
            var_list.append(l[i][-1])
            var_index.append(i)
    for i in l:
        if((i[0]=="st" or i[0]=="ld") and i[-1].isalpha() and i[-1] not in var_list):
            print("variable used before reference")
            return False;
    if sorted(var_index) != list(range(0, max(var_index)+1)):
        print("Variables not declared at beginning")
        return False
    else:
        return True
