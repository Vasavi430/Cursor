def complement_probability(p_a):
  """Calculates the probability of the complement of an event.

  Args:
    p_a: Probability of event A.

  Returns:
    The probability of the complement of A.
  """

  return 1 - p_a

# Example usage:
p_a = 0.7  # Probability of event A

probability_complement = complement_probability(p_a)
print("Probability of A' (complement of A):", probability_complement)