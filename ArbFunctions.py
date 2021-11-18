# Function that takes two odds, and returns if the bet is profitable or not.
# If it is profitable, return the two bet amounts.

def IsProfitable_2(O1, O2):
    return [
        round(O1, 3),
        round(O1**2/O2, 3),
        round((1/(O1**-1 + O2**-1)-1)*100, 3)
    ]


def IsProfitable_3(O1, O2, O3):
    return [
        round(1/(1+(O1/O2)+(O1/O3)), 3),
        round(1/(1+(O2/O1)+(O2/O3)), 3),
        round(1/(1+(O3/O1)+(O3/O2)), 3),
        round((1/(O1**-1 + O2**-1 + O3**-1)-1)*100, 3)
    ]


if __name__ == '__main__':
    print(IsProfitable_2(2, 2.45))
    print(IsProfitable_3(2, 5, 4))
