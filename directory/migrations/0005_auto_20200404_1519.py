# Generated by Django 2.2.4 on 2020-04-04 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(choices=[(4, 'A'), (3, 'B'), (2, 'C'), (1, 'D'), (0, 'F')])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.Student')),
            ],
        ),
        migrations.AddConstraint(
            model_name='grade',
            constraint=models.UniqueConstraint(fields=('student', 'course'), name='unique_student_course'),
        ),
    ]
