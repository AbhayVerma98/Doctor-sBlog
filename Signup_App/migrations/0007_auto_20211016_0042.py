# Generated by Django 3.1.5 on 2021-10-16 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signup_App', '0006_blogmodel_categorymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='title',
            field=models.CharField(max_length=35),
        ),
    ]
