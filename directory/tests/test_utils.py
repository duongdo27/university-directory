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
    def test_values(self):
        """
        Test calculate gpa
        """
        letter_grades = ['A', 'C', 'B', 'D']
        self.assertEquals(calculate_gpa(letter_grades), 2.5)

    def test_empty(self):
        """
        Test calculate gpa with empty list
        """
        letter_grades = []
        self.assertIsNone(calculate_gpa(letter_grades))
