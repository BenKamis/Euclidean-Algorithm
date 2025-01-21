# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:52:08 2025

Purpose: Euclidean Algorithm Analysis
"""

import itertools
import matplotlib.pyplot as plt

def main():

    # SETTING DATA RANGES
    lower_bound = 1
    upper_bound = 201
    # For larger data ranges, use a smaller size scalar: 
    size_scalar_gcd = 0.1
    size_scalar_steps = 0.05
    
    a_lst = range(lower_bound, upper_bound)
    b_lst = range(lower_bound, upper_bound)
    
    # Combining data into two lists for the x and y axis of plt.scatter
    c_lst = list(itertools.product(a_lst, b_lst))
    x = []
    y = []
    for c in c_lst:
        x.append(c[0])
        y.append(c[1])

    # Running the algorithm on all pairs of points
    gcd_sizes = []
    steps_sizes = []
    for c in c_lst:
        a = c[0]
        b = c[1]
        
        # The size of each dot is correlated to the GCD
        gcd = algorithm(a, b)[0]
        gcd_sizes.append(gcd * size_scalar_gcd)
        # The size of each dot is correlated to how many steps the algorithm
        # took to reach a remainder of 0
        number_of_steps = algorithm(a, b)[1]
        steps_sizes.append(number_of_steps * size_scalar_steps)
    
    # GCD GRAPH
    plt.title("Size ~ GCD")
    plt.xlabel("Range of a")
    plt.ylabel("Range of b")
    plt.scatter(x, y, s = gcd_sizes, c = 'b')
    plt.show()
    plt.clf()
    
    # STEPS TO TERMINATE GRAPH
    plt.title("Size ~ Number of steps to terminate algorithm")
    plt.xlabel("Range of a")
    plt.ylabel("Range of b")
    plt.scatter(x, y, s = steps_sizes, c = 'r')
    plt.show()
    plt.clf()
    
    # OVERLAID GRAPHS
    plt.title("Both Graphs")
    plt.xlabel("Range of a")
    plt.ylabel("Range of b")
    plt.scatter(x, y, s = steps_sizes, c = 'r', alpha = 0.5)
    plt.scatter(x, y, s = gcd_sizes, c = 'b', alpha = 0.5)
    plt.show()
    plt.clf()
    
def algorithm(a, b):
    
    r = 1 # arbitrary value
    steps = 0 # initialized    
        
    while r != 0:
        r = a % b
        a = b
        b = r
        steps += 1
        
    return (a, steps)

if __name__ == "__main__":
    main()