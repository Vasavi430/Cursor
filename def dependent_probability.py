def dependent_probability(p_a, p_b_given_a):
  """Calculates the probability of two dependent events.

  Args:
    p_a: Probability of event A.
    p_b_given_a: Conditional probability of B given A.

  Returns:
    The probability of both A and B occurring.
  """

  return p_a * p_b_given_a

# Example usage:
p_a = 0.6  # Probability of event A
p_b_given_a = 0.4  # Probability of B given A

probability_both = dependent_probability(p_a, p_b_given_a)
print("Probability of both A and B:", probability_both)