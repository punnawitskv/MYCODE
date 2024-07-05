import math

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def magnitude(v):
    return math.sqrt(sum(x ** 2 for x in v))

def angle_between_vectors(a, b):
    dot_prod = dot_product(a, b)
    magnitude_a = magnitude(a)
    magnitude_b = magnitude(b)
    cos_theta = dot_prod / (magnitude_a * magnitude_b)
    theta_radians = math.acos(cos_theta)
    theta_degrees = math.degrees(theta_radians)
    return theta_degrees

vector_a = [-2, 4, -1, 3, 6]
vector_b = [-1, 5, 0, 0, 0]
angle = angle_between_vectors(vector_a, vector_b)
print(f'The angle between the vectors is {angle:.2f} degrees')
