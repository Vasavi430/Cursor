import random

def simulate_coin_flips(n, p):
    heads = 0
    for _ in range(n):
        if random.random() < p:
            heads += 1
    return heads
num_heads = simulate_coin_flips(10, 0.5)
print("Number of heads:", num_heads)