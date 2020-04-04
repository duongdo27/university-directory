# Generated by Django 3.0.5 on 2020-04-04 14:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='phone',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number')]),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.Professor')),
            ],
        ),
    ]
