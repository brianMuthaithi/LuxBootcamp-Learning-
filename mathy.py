import math

def find_roots(a, b, c):
    root1 = (-b + (math.sqrt(b*b + 4*a*c)) / (2*a))
    root2 = (-b - (math.sqrt(b*b + 4*a*c)) / (2*a))

    print(root1, root2)
    return root1, root2
find_roots(1,-3,10)
