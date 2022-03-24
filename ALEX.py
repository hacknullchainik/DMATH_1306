# The present module works with integers instances from the 
# class integer inside of the module 'Dtypes.py' 


def print_int(inst_p, inst_r,dig):
    val =  inst_p[::-1]
    print("ALEX : ",*val, " x ", dig , " = ", *inst_r ,sep='')


def MUL_ND_N(num:object,num_2:int):

    list_num = num.get_num()
    length = num.get_rank()

    results = []
    keeper = 0

    for i in range(length + 1):
        value = list_num[i] * num_2
        if value < 10:
            if keeper == 0:
                results.insert(0,value)
            else:
                value = value + keeper
                results.insert(0,value)
                keeper = 0
        else:
            keeper = value // 10
            results.insert(0,value % 10)
    
    return results
        

 #not ready yet   
def MOD_NN_N(num:object,num_2:int):

    list_num = num.get_num()
    length = num.get_rank()

    mod = 0
    list_num_str = ""
    for i in list_num[::-1]: 
        list_num_str += str(list_num)

    for i in range(0,length,1):

        digit = ord(list_num_str[i]) - ord(list_num_str[length])
        mod = mod * 10 + digit
        mod = mod % num_2

    print(mod)
    return mod