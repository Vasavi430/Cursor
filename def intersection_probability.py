def conditional_probability(p_intersection, p_b):
  """Calculates the conditional probability of A given B.

  Args:
    p_intersection: Probability of the intersection of A and B.
    p_b: Probability of event B.

  Returns:
    The conditional probability of A given B.
  """

  if p_b == 0:
    raise ValueError("Probability of B cannot be zero.")

  return p_intersection / p_b

# Example usage:
p_intersection = 0.2  # Probability of both A and B
p_b = 0.5  # Probability of event B

conditional_probability_a_given_b = conditional_probability(p_intersection, p_b)
print("P(A|B):", conditional_probability_a_given_b)