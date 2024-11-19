import itertools

def generate_combinations(lst, r):
  
  return list(itertools.combinations(lst, r))

my_list = [1, 2, 3, 4]
r = 2  # Choose combinations of length 2
combinations = generate_combinations(my_list, r)
print(combinations)