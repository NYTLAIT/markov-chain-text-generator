import random

def weighted_random_word(histogram):
    tokens = sum(list(histogram.values()))
    dart = random.randint(1, tokens)

    border = 0
    for word in histogram:
        border += histogram[word]
        if border >= dart:
            return word