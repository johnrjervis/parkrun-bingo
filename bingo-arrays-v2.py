"""
This is attempt #4, which is based on Pandas Dataframes (again)
Typical time to solve 1 million iterations of 146 results: ~35 s
This time, I'm only storing one iteration (instead of all - e.g. 1 million - iterations)
This is quicker than any previous version - more than twice as fast as the previous pandas version (v2)
It also does not get killed when run with 10 million iterations (time taken ~342 s)
"""

import numpy as np

def bingo_array(runs, samples = 1000000):
    """Uses Monte Carlo simulation to calculate the probability of getting bingo in *runs number of parkruns"""
    """
    bingo = having all 60 possible seconds values amongst your set of finishing times
    E.g. a finishing times of 29:14 & 30:04 means you have 'got' 4 & 15 seconds
    If these were your only times, you would have 58 more to get to achieve bingo
    """

    bingos = 0
    total = 0

    for i in range(samples):
        iteration = np.random.randint(0, 60, size = runs, dtype = 'int8')
        uniqueCount = len(np.unique(iteration))

        total += uniqueCount
        if uniqueCount == 60:
            bingos += 1
   
    bingoProb = bingos / samples * 100
    averageMisses = 60 - (total / samples)

    return (bingoProb, averageMisses)

if __name__ == "__main__":
    import sys
    from time import perf_counter as pc

    _, runs, *args = sys.argv

    if args:
        t0 = pc(); prob, short = bingo_array(int(runs), int(args[0])); runtime = pc() - t0
    else:
        t0 = pc(); prob, short = bingo_array(int(runs)); runtime = pc() - t0

    print("Time taken: {0:.3f} s\nResults: probability = {1:.4f}%, expected short = {2:.3f}".format(runtime, prob, short))
