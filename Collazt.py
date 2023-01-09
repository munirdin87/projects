
'''
The collatz conjecture is a simple algorithm can take any postive natural number and always restul back to  ... 4, 2, 1.
Some claims that tthe collatz conjecture is simplest unsovable problem, because until now nobody can prove it is True or False.
Here how it works:
collatz conjecture starts with any positive integer, if the number is even, then it will be divided by two. if it is odd
then it will be multiplied by 3 and add one, as n *3 + 1.
If this sequence is continued, the result is always back to as .... 4, 2, 1.
function descrption:
the function collatz take any posive interger and return all siquences of collatiz conjecture as result.
the plot_collatz function take n as input and looping the numbers from 1  to n and calculate collatz conjecture.
finally, it will plot the all output into a line graph.
'''

# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# calculating the Collazt sequence numbers
def collatz(n):
    result = []
    while n > 1:
        if (n % 2):
            # n is odd
            n = 3 * n + 1
            result.append(n)
        else:
            # n is even
            n = n // 2
            result.append(n)
    return result


def plot_collatz(n):
# generate output for all numbers from 1 to n
    full = []
    for i in range(1, n):
        full.append(collatz(i))
# plotting all ouputs in a graph
    for i in full:
        plt.plot(i)
    return plt.show()



# test the function for 1 to 100.
plot_collatz(100)
