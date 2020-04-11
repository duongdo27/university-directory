"""
Test all utility function
"""
# pylint: disable=no-member

from django.test import TestCase

from directory.utils import calculate_gpa


class DepartmentTest(TestCase):
    """
    Test calculate gpa
    """
    letter_grades = ['A', 'C', 'B', 'D']
    assertEquals = (calculate_gpa(letter_grades), 2.5)
