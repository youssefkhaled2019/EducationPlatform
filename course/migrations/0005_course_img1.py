# Generated by Django 5.2 on 2025-06-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_num_enroll'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='img1',
            field=models.ImageField(blank=True, default='course.svg', null=True, upload_to='course_img/%y/%m/%d'),
        ),
    ]
