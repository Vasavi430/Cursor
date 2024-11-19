def conditional_probability(p_a_and_b, p_b):
  """Calculates the conditional probability of A given B.

  Args:
    p_a_and_b: Probability of both A and B occurring.
    p_b: Probability of event B.

  Returns:
    The conditional probability of A given B.
  """

  if p_b == 0:
    raise ValueError("Probability of B cannot be zero.")

  return p_a_and_b / p_b

# Example usage:
p_a_and_b = 0.2  # Probability of both A and B
p_b = 0.5  # Probability of event B

conditional_probability_a_given_b = conditional_probability(p_a_and_b, p_b)
print("P(A|B):", conditional_probability_a_given_b)