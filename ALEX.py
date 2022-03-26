# The present module works with Integer, RNumber, Polynomial, NNumber instances
# The module providing those classes is 'Dtypes.py'
from Dtypes import Integer, NNumber


def MUL_ND_N(num: object, num_2: int):
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
                results.insert(0, value)
                keeper = 0
        elif keeper != 0:
            # in case the next resulting number of the multiplication also exceeds or is equal to 10
            results.insert(0, (value + keeper) % 10)
            keeper = value // 10
            if i == length:
                results.insert(0, keeper)
        else:
            # the second digit of the resulting number of the multiplication is stored inside of the list results
            keeper = value // 10
            results.insert(0, value % 10)

    new_obj = NNumber(results)

    return new_obj


# The set of natural numbers is from 1 to infinity and does not include decimals.
# The set of integer numbers is from 0 to positive infinity as well as from 0 to negative infity.
# Therefore, any conversion of natural numbers to integer numbers will be done on the sign(positive or negative)
# depending on the user preference.
def TRANS_N_Z(num:NNumber):
    return Integer(num.get_num(), False)
