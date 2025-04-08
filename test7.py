#Task: In this task, we are going to write a program test7.py that finds the roots of cubic polynomials listed in the file poly.txt using goalSeek function.

import shelve

# Use goalSeek function to find the roots of the polynomials P1, P2, and P3 listed in the introduction. 
# The expected answers are: 3, 1.5, and -4.2. Choose the limits to contain the roots you are looking for 
# (-5 and 5 would suffice for these three polynomials). Confirm that your program is finding correct roots.

def goalSeek(function, lo, hi, target, maxError=0.0001):
    while True:
        guess = (lo + hi) / 2
        result = function(guess)
        error = abs(result - target)
        if error <= maxError:
            return guess
        if result < target:
            lo = guess
        else:
            hi = guess

#Write a function makePoly that can generate a Python function representation of a cubic polynomial from its coefficients A, B, C, D
def makePoly(A, B, C, D):
    def poly(x):
        return A*x*x*x + B*x*x + C*x + D
    return poly

# Read the file poly.txt. For each polynomial you read from the file, use makePoly to generate its Python function representation. 
# Run goalSeek on this function with given Lo and Hi limits to find the root. You can use WolframAlpha to check that the roots are correct.
# After that, for each polynomial, print out its coefficients A, B, C, D followed by the root your found. 
# Format the output nicely making sure the columns line up (we also added -> to clearly separate the root from the coefficients)
with open("poly.txt") as file:
    for line in file:
        if line[0] != '#':
            items = line.split()
            A = float(items[0])
            B = float(items[1])
            C = float(items[2])
            D = float(items[3])
            lo = float(items[4])
            hi = float(items[5])

            P = makePoly(A, B, C, D)
            root = goalSeek(P, lo, hi, 0)

            # Format output: 8-character wide, 2 decimal float
            print("{0:8.2f}{1:9.2f}{2:9.2f}{3:9.2f}  ->{4:10.2f}".format(A, B, C, D, root))
