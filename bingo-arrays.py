"""
This is attempt #2, which is based on Pandas Dataframes
Typical time to solve 1 million iterations of 146 results: ~80 s
Using DF is quicker (1st - procedural - solution typically took ~140 s to complete 1 million x 146)
Issues: running with 10 million iterations results in the program being "killed" - caused by high memory usage of the 10000000 x 146 array?
Hence attempt to redue memory use by using dtype = int8
"""

import numpy as np
import pandas as pd

count_uniques = lambda series: len(series.unique())

def calc_bingo(runs, samples = 1000000):
    """Uses Monte Carlo simulation to calculate the probability of getting bingo in *runs number of parkruns"""
    """bingo = having all 60 possible seconds values amongst your set of finishing times"""
    """E.g. a finishing time of 30:15 means you have 'got' 15 seconds"""

    data = pd.DataFrame(np.random.randint(0, 60, size = (runs, samples), dtype = 'int8'))
    uniqueTotals = data.apply(count_uniques)
   
    # misses: average number of values short of a full house
    misses = 60 - uniqueTotals.mean()

    # bingoProb: percent probability of getting a full house
    bingoProb = uniqueTotals[uniqueTotals == 60].count() * 100 / samples

    return(bingoProb, misses)

if __name__ == "__main__":
    import sys
    from time import perf_counter as pc

    _, runs, *args = sys.argv

    if args:
        t0 = pc(); prob, short = calc_bingo(int(runs), int(args[0])); runtime = pc() - t0
    else:
        t0 = pc(); prob, short = calc_bingo(int(runs)); runtime = pc() - t0

    print("Time taken: {0:.3f}\nResults: probability = {1:.4f}, expected short = {2:.3f}".format(runtime, prob, short))
