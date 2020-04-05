# Generated by Django 2.2.4 on 2020-04-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0005_auto_20200404_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior')], max_length=20),
        ),
    ]
