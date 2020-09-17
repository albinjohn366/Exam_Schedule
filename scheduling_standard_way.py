"""
Student Subject
1       A, B, C
2       B, G, A
3       C, D, E
4       c, D, F
5       E, F, G
"""

# Defining the subjects
subjects = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Defining the constraints from the knowledge
constraints = [('A', 'B', 'C'), ('B', 'G', 'A'), ('C', 'D', 'E'),
               ('C', 'D', 'F'), ('B', 'F', 'C')]

# Setting Domains
domain = dict()
days = {'Monday', 'Tuesday', 'Wednesday'}
for subject in subjects:
    domain[subject] = days

# Iteration for assigning values and backtracking
assignment = dict()


def least_domain_length_variable(courses):
    # If there are values inside the assignment list
    if assignment.keys():
        for key in assignment.keys():
            # Taking only unassigned courses
            if key in courses:
                courses.remove(key)

    variable = []
    smallest_length = len(domain[courses[0]])
    # Iterating over each course
    for course in courses:
        # If length is less than the smallest length
        if len(domain[course]) < smallest_length:
            smallest_length = len(domain[course])
            variable.clear()
            variable.append(course)
        # If there are different variables with same domain length
        elif len(domain[course]) == smallest_length:
            variable.append(course)
    return variable


def variable_with_most_connections(variables):
    max_number = 0
    right_variable = variables[0]
    # Iterating over each variable in variables
    for variable in variables:
        count = 0
        # Checking if variable is in each element of the constraints
        for item in constraints:
            if variable in item:
                count += 1
        # Finding the variable with most connections
        if count > max_number:
            right_variable = variable
            max_number = count
    return right_variable


def constraint_check(dictionary):
    # Iterating over days and finding exams on each day
    for day in days:
        slot = []
        for key in dictionary:
            if dictionary[key] == day:
                slot.append(key)

        # Checking if the exams on each day contradicts the constraints
        for constraint in constraints:
            count = 0
            for item in constraint:
                if item in slot:
                    count += 1
                if count > 1:
                    return False
    return True


def backtrack():
    # Checking if goal is reached
    if len(assignment.keys()) == len(subjects):
        return True

    best_variable = least_domain_length_variable(subjects.copy())
    # If there are multiple best variables
    if len(best_variable) != 1:
        best_variable = variable_with_most_connections(best_variable)
    else:
        best_variable = best_variable[0]

    # Assigning days present in domain
    for day in domain[best_variable]:
        assignment[best_variable] = day

        # If constraints are not satisfied
        if not constraint_check(assignment):
            del assignment[best_variable]
            continue
        if backtrack():
            return True
        else:
            del assignment[best_variable]
    return False


if backtrack():
    for num, constraint in enumerate(constraints):
        print('Student {}:'.format(num + 1))
        for subject in constraint:
            print('Subject {}: {}'.format(subject, assignment[subject]))
        print('-'*20)
else:
    print('No solution')
