# Generated by Django 3.1.5 on 2021-10-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signup_App', '0008_auto_20211016_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
