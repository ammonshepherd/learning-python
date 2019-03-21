# function to generate the number of solutions and the solutions to three given
# values
# Input: three values, A, B, C
# Output: 1) number of solutions 2) first solution 3) second solution
from math import sqrt

def quadratic_solution(A, B, C):
    solutions = 0
    solution1 = 0
    solution2 = 0
    # no solutions
    if ( (B**2 - 4*A*C) < 0 ):
        solutions = 0

    # one solution
    elif ( (B**2 - 4*A*C) == 0 ):
        solutions = 1

        x = (-B/(2*A))
        solution1 = x

    elif A == 0:
        solutions = 1

        x = (-C/B)
        solution1 = x

    elif A == 0 and B ==0:
        solutions = 0

    #two solutions
    else:
        solutions = 2

        x1 = ( (-B - sqrt(B**2 - 4*A*C)) / (2*A) )
        solution1 = x1

        x2 = ( (-B + sqrt(B**2 - 4*A*C)) / (2*A) )
        solution2 = x2

    return solutions, solution1, solution2

if __name__ == '__main__':
    print("Solving the quadratic equation for A = 7, B = 10, C = 3")
    numSolutions, solOne, solTwo = quadratic_solution(7, 10, 3)
    print("Number of solutions: {}".format(numSolutions))
    print("First solution: {}".format(solOne))
    print("Second solution: {}".format(solTwo))
