from django import forms

from directory.models import Department
from directory.models import Professor


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'uk-input'


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['first_name', 'last_name', 'email', 'phone', 'department']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'uk-input'
        self.fields['last_name'].widget.attrs['class'] = 'uk-input'
        self.fields['email'].widget.attrs['class'] = 'uk-input'
        self.fields['phone'].widget.attrs['class'] = 'uk-input'
        self.fields['department'].widget.attrs['class'] = 'uk-select'