# parkrun-bingo
Estimate the probability of getting bingo in x number of parkruns
The method used is Monte Carlo simulation
The main function returns the probability of getting bingo and the expected number of missing values
This version uses a pandas DataFrame for quicker calculations
Perf_counter is used to record how long the calculations take
The number of parkruns has to be supplied as a command line argument
The number of simulations can be supplied as an optional second argument
Usage: python3 bingo-arrays.py runs (simulations)
