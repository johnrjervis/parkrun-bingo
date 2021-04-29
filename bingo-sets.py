"""
This is attempt #3, which is based on setcomps
Here, I want to see whether using sets with minimal storage of data in memory is quicker than using large dataframes
The result is the same as v1: time is ~140-150 s for 1 million x 146 calculations
Unlike the pandas version, the program can be run for any number of iterations without being killed
"""

# IMPORTANT NOTE!
# np.random.randint(min, max) returns values in the range min <= x < max
# But random.randint(min, max) returns values in the range min <= x <= max

import random

def bingo_sets(runs, samples = 1000000):

    bingos = 0
    total = 0

    for i in range(samples):
        result = len({random.randint(0, 59) for i in range(runs)})
        total += result
        if result == 60:
            bingos += 1

    bingoProb = bingos / samples * 100
    average = 60 - (total / samples)

    return (bingoProb, average)

if __name__ == "__main__":
    import sys
    from time import perf_counter as pc

    _, runs, *args = sys.argv

    if args:
        t0 = pc(); prob, short = bingo_sets(int(runs), int(args[0])); runtime = pc() - t0
    else:
        t0 = pc(); prob, short = bingo_sets(int(runs)); runtime = pc() - t0

    print("Time taken: {0:.3f} s\nResults: probability = {1:.4f}%, expected short = {2:.3f}".format(runtime, prob, short))
