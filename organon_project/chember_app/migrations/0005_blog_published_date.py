# Generated by Django 3.2.6 on 2021-08-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chember_app', '0004_treatment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]