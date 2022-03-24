# The present module works with Integer, RNumber, Polynomial, NNumber instances 
# The module providing those classes is 'Dtypes.py' 

#Function fro the printingout of the result after the function completed requested operations
def print_int(inst_p, inst_r,dig):
    #'val' stores the reversed list of numbers contained in the object
    # this is done because at the instanciation level the number are reversed
    val =  inst_p[::-1]
    print(*val, " x ", dig , " = ", *inst_r ,sep='')


def MUL_ND_N(num:object,num_2:int):
    #local variables storing the value from arugments
    #avoiding changes to the original data
    list_num = num.get_num()
    length = num.get_rank()

    #'results' will store the end result provided by the current function
    #'keeper' is used to store the first digit if during the multiplication of two digits the product is a two digit number.
    results = []
    keeper = 0

    for i in range(length + 1):
        #'value' stores the result of multiplication between 1 digit contained in the list and the chosen digit by the user.
        value = list_num[i] * num_2
        #When value is greater or equal to 10 it means that it contains a two digit number.
        if value < 10:
            if keeper == 0:
                results.insert(0,value)
            else:
                #the first digit of the resulting number of the multilpication is stored inside keeper
                #the value of keeper is then added to the result of the next multiplication
                value = value + keeper
                results.insert(0,value)
                keeper = 0
        else:
            #the second digit of the resulting number of the multiplication is stored inside of the list results
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
