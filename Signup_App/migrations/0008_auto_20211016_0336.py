# Generated by Django 3.1.5 on 2021-10-16 03:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Signup_App', '0007_auto_20211016_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
