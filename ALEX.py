# The present module works with Integer, RNumber, Polynomial, NNumber instances
# The module providing those classes is 'Dtypes.py'

from NIKITAT import DIV_ZZ_Z
from Dtypes import Integer, NNumber, Integer, RNumber, Polynomial
import Naturals, Integers, Rationals

def MUL_ND_N(num: Naturals, num_2: int):
    # local variables storing the value from arugments
    # avoiding changes to the original data
    list_num = num.get_num()
    length = num.get_rank()

    # 'results' will store the end result provided by the current function
    # 'keeper' is used to store the first digit if during the multiplication of two digits the product is a two digit number.
    results = []
    keeper = 0

    for i in range(length + 1):
        # 'value' stores the result of multiplication between 1 digit contained in the list and the chosen digit by the user.
        value = list_num[i] * num_2
        # When value is greater or equal to 10 it means that it contains a two digit number.
        if value < 10:
            if keeper == 0:
                results.insert(0, value)
            else:
                # the first digit of the resulting number of the multilpication is stored inside keeper
                # the value of keeper is then added to the result of the next multiplication
                value = value + keeper
                if value < 10:
                    results.insert(0, value)
                else:
                    results.insert(0,value%10)
                    results.insert(0,value//10)
                keeper = 0
        elif keeper != 0:
            # in case the next resulting number of the multiplication also exceeds or is equal to 10
            results.insert(0, (value + keeper) % 10)
            keeper = (value+keeper) // 10
            if i == length:
                results.insert(0, keeper)
        else:
            # the second digit of the resulting number of the multiplication is stored inside of the list results
            keeper = value // 10
            results.insert(0, value % 10)
            if (length + 1) == 1:
                results.insert(0,keeper)
            elif length == i:
                results.insert(0,keeper)

    new_obj = NNumber(results)

    return new_obj


# The set of natural numbers is from 1 to infinity and does not include decimals.
# The set of integer numbers is from 0 to positive infinity as well as from 0 to negative infity.
# Therefore, any conversion of natural numbers to integer numbers will be done on the sign(positive or negative)
# depending on the user preference.
def TRANS_N_Z(num:NNumber):
    return Integer(num.get_num(), False)


#The function looks for the remainder of a division between two integers 
def MOD_ZZ_Z(num:Integer, num_2:Integer):
    #'a' stores the value of the dividend.
    #'b' stores the value of the divisor.
    #'q' stores the value of the quotient.
    #'r' stores the value of the remainder.
    
    a = Integer(num.get_num()[::-1],num.get_sign())
    b = Integer(num_2.get_num()[::-1],num_2.get_sign())
    
    # DIV_ZZ_Z FROM NIKITAT.PY
    # Finding the quotient from the division of an integer by an integer
    q = DIV_ZZ_Z(a,b)

    # MUL_ZZ_Z FROM SASHAP.PY
    # Storing the value of the divisor multiplied by the quotient
    a_1 = Integers.MUL_ZZ_Z(b,q)

    # SUB_ZZ_Z() -> pending from Nastia <-
    # Substructing the value of the divident multiplied by the quotient from the dividend
    r = Integers.SUB_ZZ_Z(a,a_1)

    # MUL_ZM_Z FROM NIKITAT.PY
    # Putting the right sign the resulting integer.
    if a.get_sign() and b.get_sign():
        pass
    else:
        r = Integers.MUL_ZM_Z(r)

    return r

#Substructing function(between two rational numbers)
def SUB_QQ_Q(num_1: RNumber, num_2: RNumber):
    #Finding the common divider that will allow the substruction 
    comon_divider = Naturals.LCM_NN_N(num_1.get_den(), num_2.get_den())

    #Checking if the common diviser is equal to the denominator of num_1
    #If the they are equal then the numerator will not be affected
    if comon_divider == num_1.get_den():
        new_num_1 = Integer(str(num_1.get_num()),False)
    else:
        temp_var = Integer(str(num_1.get_den()), num_1.get_sign())
        temp_var_1 = Integer(str(num_1.get_num()), num_1.get_sign())
        temp_var_2 = Integer(comon_divider.get_num()[::-1],False)
        temp_var_3 = Integer(DIV_ZZ_Z(temp_var_2,temp_var).get_num(),DIV_ZZ_Z(temp_var_2,temp_var).get_sign())

        new_num_1 = Integers.MUL_ZZ_Z(temp_var_1,temp_var_3)
        
    #Checking if the common diviser is equal to the denominator of the of num_2
    #If the they are equal then the numerator will not be affected
    if comon_divider == num_2.get_den():
        new_num_2 = Integer(str(num_2.get_num()),False)
    else:
        temp_var = Integer(str(num_2.get_den()),num_2.get_sign())
        temp_var_1 = Integer(str(num_2.get_num()), num_2.get_sign())
        temp_var_2 = Integer(comon_divider.get_num()[::-1],False)
        temp_var_3 = Integer(DIV_ZZ_Z(temp_var_2,temp_var).get_num(),DIV_ZZ_Z(temp_var_2,temp_var).get_sign())

        new_num_2 = Integers.MUL_ZZ_Z(temp_var_1,temp_var_3)

    #Substracting the two resulting numerator 
    final_num = Integers.SUB_ZZ_Z(new_num_1,new_num_2)
    res = RNumber(final_num,comon_divider)

    return res

#The function multiplies x^k to a polynomial
#'poly_2' should only be x^k not x^k1 + x^k2 ...
def MUL_Pxk_P(poly_1: Polynomial, poly_2: Polynomial):

    p_1 = ''
    p_2_cof = 0

    #This loop looks for the coefficient of the x^k that will be multiplied to poly_1.
    for i in poly_2.get_coefs():
        if i.get_num() != 0:
            p_2_cof = i

    #Multiplying each coefficient to one another.    
    for i in poly_1.get_coefs()[::-1]:
        p_1 += str(Rationals.MUL_QQ_Q(i,p_2_cof))
        p_1 += ' '
    p_1 = p_1[:-1]
   
   #Increasing the value of the exponents of our polynomial by k.
    for i in range(poly_2.get_exp()):
        p_1 += ' 0'
    
    return Polynomial(p_1)
