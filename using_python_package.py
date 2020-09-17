from constraint import *

problem = Problem()

# Adding variables
problem.addVariables(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    ['Monday', 'Tuesday', 'Wednesday']
)

# Defining constraints
constraints = [('A', 'B', 'C'), ('B', 'G', 'A'), ('C', 'D', 'E'),
               ('C', 'D', 'F'), ('B', 'F', 'C')]

# Adding constraints
for x, y, z in constraints:
    problem.addConstraint(lambda x, y, z: (x != y) and (y != z) and (x != z),
                          (x, y, z))

# Printing solution
for solution in problem.getSolutions():
    print(solution)
    print('-' * 20)