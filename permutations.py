import itertools

def generate_permutations(lst):
 return list(itertools.permutations(lst))
my_list = [1, 2, 3]
permutations = generate_permutations(my_list)
print(permutations)