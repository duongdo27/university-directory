"""
Collections of all forms used in the university directory app
"""
# pylint: disable=too-few-public-methods

from django import forms

from directory.models import Department
from directory.models import Course
from directory.models import Student
from directory.models import Grade
from directory.models import Professor


class DepartmentForm(forms.ModelForm):
    """
    Form to create new department
    """
    class Meta:
        """
        Meta data for department
        """
        model = Department
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'uk-input'


class ProfessorForm(forms.ModelForm):
    """
    Form to create new professor
    """
    class Meta:
        """
        Meta data for professor
        """
        model = Professor
        fields = ['first_name', 'last_name', 'email', 'phone', 'department']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'uk-input'
        self.fields['last_name'].widget.attrs['class'] = 'uk-input'
        self.fields['email'].widget.attrs['class'] = 'uk-input'
        self.fields['phone'].widget.attrs['class'] = 'uk-input'
        self.fields['department'].widget.attrs['class'] = 'uk-select'


class CourseForm(forms.ModelForm):
    """
    Form to create new course
    """
    class Meta:
        """
        Meta data for course
        """
        model = Course
        fields = ['name', 'description', 'professor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'uk-input'
        self.fields['description'].widget.attrs['class'] = 'uk-input'
        self.fields['professor'].widget.attrs['class'] = 'uk-select'


class StudentForm(forms.ModelForm):
    """
    Form to create new student
    """
    class Meta:
        """
        Meta data for student
        """
        model = Student
        fields = ['first_name', 'last_name', 'email', 'year']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'uk-input'
        self.fields['last_name'].widget.attrs['class'] = 'uk-input'
        self.fields['email'].widget.attrs['class'] = 'uk-input'
        self.fields['year'].widget.attrs['class'] = 'uk-select'


class GradeCreateForm(forms.ModelForm):
    """
    Form to create new grade
    """
    class Meta:
        """
        Meta data for grade
        """
        model = Grade
        fields = ['grade', 'student', 'course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].widget.attrs['class'] = 'uk-input'
        self.fields['course'].widget.attrs['class'] = 'uk-select'
        self.fields['student'].widget = forms.HiddenInput()


class GradeUpdateForm(forms.ModelForm):
    """
    Form to update the grade
    """
    class Meta:
        """
        Meta data for grade
        """
        model = Grade
        fields = ['grade', 'student', 'course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].widget.attrs['class'] = 'uk-input'
        self.fields['student'].widget.attrs['class'] = 'uk-select'
        self.fields['course'].widget.attrs['class'] = 'uk-select'
        self.fields['student'].disabled = True
        self.fields['course'].disabled = True
