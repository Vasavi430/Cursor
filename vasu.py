import random

num_flips = 5
heads = 0
tails = 0

for _ in range(num_flips):
    if random.randint(0, 1)==0:
        heads +=1
    else:
        tails += 1

print(f'Results after {num_flips} flips: {{Heads: {heads}, Tails: {tails}}}')

