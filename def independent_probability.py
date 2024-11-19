def independent_probability(p_a, p_b):
  """Calculates the probability of two independent events.

  Args:
    p_a: Probability of event A.
    p_b: Probability of event B.

  Returns:
    The probability of both A and B occurring.
  """

  return p_a * p_b

# Example usage:
p_a = 0.6  # Probability of event A
p_b = 0.4  # Probability of event B

probability_both = independent_probability(p_a, p_b)
print("Probability of both A and B:", probability_both)