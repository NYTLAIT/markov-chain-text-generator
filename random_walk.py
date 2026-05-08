import random

# NOTE: histogram for this project is the second order markov chain
# with the shape: {('the', 'great'): {'sea': 1, 'ice': 2}}

def weighted_random_word(histogram):
    '''
    Selects a word at random, weighted by frequency.

    Args:
        histogram (dict): A dict of {word: frequency} pairs
    Returns:
        str: A randomly selected word, weighted by frequency.
    '''
    tokens = sum(list(histogram.values()))
    dart = random.randint(1, tokens)

    border = 0
    for word in histogram:
        border += histogram[word]
        if border >= dart:
            return word