"""
These three versions represent my first attempt at solving this problem
"""

"""Version 1"""

def listgen(number, start=0, end=59):
    """Generates a list of random numbers"""
    import random
    result = []
    for i in range(number):
        a = random.randint(start, end)
        result.append(a)
    return result

def countmissing(nlist, number=60):
    """Compares a range of numbers to a list and returns the a count of missing numbers"""
    a = []
    for i in range(number):
        a.append(i)
    diff = set.difference(set(a), set(nlist))
    result = len(diff)
    return result

def bingofy(runs, repeats=100):
    """Returns the probability of bingo and the expected number of missing times"""
    bingos = 0
    sum_expect = 0    
    for i in range(repeats):
        testlist = listgen(runs)
        test_miss = countmissing(testlist)
        sum_expect += test_miss
        if test_miss == 0:
            bingos += 1
    expected = sum_expect / repeats
    bingo_prob = 100 * bingos / repeats
    return (bingo_prob, expected)

""" Version 2 """

def listlen(number, start=0, end=59):
    """Returns the number of unique elements in a randomly-generated list of a chosen length"""
    import random
    rlist = []
    for i in range(number):
        a = random.randint(start, end)
        rlist.append(a)
    slist = set(rlist)
    result = 60 - len(slist)
    return result

def bingofy2(runs, repeats=100):
    """Returns the probability of bingo and the expected number of missing times"""
    bingos = 0
    sum_expect = 0    
    for i in range(repeats):
        missing = listlen(runs)
        sum_expect += missing
        if missing == 0:
            bingos += 1
    expected = sum_expect / repeats
    bingo_prob = 100 * bingos / repeats
    return (bingo_prob, expected)    

""" Version 3 """
"""This effort uses sets from the start rather than converting a list to a set.
In theory, sets should be a bit quicker, but it isn't - perhaps this needs to be refined"""

def setLen(number, start=0, end=59):
    """Returns the number of unique elements in a randomly-generated set with values in the range 0 - 59"""
    import random
    rSet = set()
    for i in range(number):
        a = random.randint(start, end)
        rSet.add(a)
    result = 60 - len(rSet)
    return result

def bingofy3(runs, repeats=100):
    """Returns the probability of bingo and the expected number of missing times"""
    bingos = 0
    sum_expect = 0    
    for i in range(repeats):
        missing = setLen(runs)
        sum_expect += missing
        if missing == 0:
            bingos += 1
    expected = sum_expect / repeats
    bingo_prob = 100 * bingos / repeats
    return (bingo_prob, expected)    

if __name__ == "__main__":
    import sys
    from time import perf_counter as pc
    t0 = pc(); a, b = bingofy3(int(sys.argv[1]), 1000000); runtime = pc() - t0
    print("1 million iterations completed in {0:.2f} s\nResult: prob = {1:.4f}%, exp. short = {2:.3f}".format(runtime, a, b))
