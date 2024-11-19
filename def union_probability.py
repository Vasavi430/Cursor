def union_probability(p_a, p_b, p_intersection):
  """Calculates the probability of the union of two events.

  Args:
    p_a: Probability of event A.
    p_b: Probability of event B.
    p_intersection: Probability of the intersection of A and B.

  Returns:
    The probability of the union of A and B.
  """

  return p_a + p_b - p_intersection

# Example usage:
p_a = 0.4  # Probability of event A
p_b = 0.3  # Probability of event B
p_intersection = 0.15  # Probability of both A and B

probability_union = union_probability(p_a, p_b, p_intersection)
print("Probability of A union B:", probability_union)