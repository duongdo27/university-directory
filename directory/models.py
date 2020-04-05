from django.db import models
from django.core.validators import RegexValidator


class Department(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.name)



class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    phone = models.CharField(max_length=10, unique=True, validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number')])
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(str(self.last_name), str(self.first_name))


class Course(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    
    @property
    def grades(self):
        return Grade.objects.filter(course=self)


STUDENT_YEARS = (
    ("Freshman", "Freshman"),
    ("Sophomore", "Sophomore"),
    ("Junior", "Junior"),
    ("Senior", "Senior"),
)


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    year = models.CharField(max_length=20, choices=STUDENT_YEARS)

    def __str__(self):
        return "{}, {}".format(str(self.last_name), str(self.first_name))


LETTER_GRADES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("F", "F"),
)


class Grade(models.Model):
    grade = models.CharField(max_length=2, choices=LETTER_GRADES)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course'],
                name='unique_student_course',
            )
        ]

    def __str__(self):
        return self.grade
