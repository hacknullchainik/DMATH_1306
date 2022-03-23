# The present module works with integers instances from the 
# class integer inside of the module 'Dtypes.py' 
def alex_print_int(inst_p, inst_r,dig):
    print(*inst_p, " x ", dig , " = ", *inst_r ,sep='')


def ALEX_MUL_ND_N(num:object,num_2:int):
    list_num = num.value
    results = []
    keeper = 0
    
    for i in reversed(range(num.rank + 1)):
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
        

    

def MOD_NN_N():
    pass