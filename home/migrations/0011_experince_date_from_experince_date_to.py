# Generated by Django 4.2.4 on 2024-06-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_experince'),
    ]

    operations = [
        migrations.AddField(
            model_name='experince',
            name='date_From',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='experince',
            name='date_To',
            field=models.DateField(auto_now=True),
        ),
    ]
