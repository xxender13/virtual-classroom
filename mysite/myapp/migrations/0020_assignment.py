# Generated by Django 3.0 on 2021-11-15 11:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20211114_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignmentId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('assignmentHeading', models.CharField(max_length=50)),
                ('assignmentDescription', models.TextField()),
                ('assignmentCreationTime', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('assignmentDueTime', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('assignmentLink', models.TextField(blank=True, null=True)),
                ('assignmentSubmission', models.TextField(blank=True, default='{}', null=True)),
                ('classId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ClassRoom')),
            ],
        ),
    ]
