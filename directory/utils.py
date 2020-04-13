"""
Contains all utility functions
"""
# pylint: disable=inconsistent-return-statements

GPA = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}


def calculate_gpa(letter_grades):
    """
    :param letter_grades: Given list of letter grade
    :return: gpa
    """
    number_grades = [GPA.get(x, 0) for x in letter_grades]
    if len(number_grades) == 0:
        return

    gpa = sum(number_grades) / len(number_grades)
    return round(gpa, 2)
