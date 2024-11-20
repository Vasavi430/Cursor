import random

def bernoulli_trial(p):
    return 1 if random.random() < p else 0