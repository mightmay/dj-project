# Generated by Django 2.1.7 on 2019-02-13 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190213_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsmodel',
            name='student_identification_string',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
