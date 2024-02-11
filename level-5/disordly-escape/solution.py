from math import factorial
from collections import Counter

def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

# Function to calculate the number of cycles in a configuration
def calc_cycle_count(cycle, num_elements):
    cycle_count = factorial(num_elements)
    
    for cycle_size, cycle_num in Counter(cycle).items():
        cycle_count //= (cycle_size ** cycle_num) * factorial(cycle_num)
    return cycle_count

# Function to generate all possible partitions of a number into cycles
def cycle_partitions(num, i=1):
    yield [num]
    
    for i in range(i, num // 2 + 1):
        for partition in cycle_partitions(num - i, i):
            yield [i] + partition

# This is used to count the number of equivalent configurations for a given cycle structure
def burnside_lemma(cpw, cph, s, w, h):
    # Calculate the contribution of each configuration
    m = calc_cycle_count(cpw, w) * calc_cycle_count(cph, h)
    return m * (s ** sum([sum([gcd(i, j) for i in cpw]) for j in cph]))


def solution(w, h, s):    
    grid = 0
    # Iterate through cycle partitions for both width and height
    for cpw in cycle_partitions(w):
        for cph in cycle_partitions(h):
            # Apply Burnside's Lemma to calculate the number of equivalent configurations for the current cycle structure
            grid += burnside_lemma(cpw, cph, s, w, h)

    # Return the total number of unique, non-equivalent configurations
    return str(grid // (factorial(w) * factorial(h)))


if __name__ == "__main__":
    print(solution(2, 3, 4))
    print(solution(2, 2, 2))