# Generated by Django 4.2.4 on 2024-06-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_experince_date_from_alter_experince_date_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=300)),
                ('cv', models.FileField(upload_to='upload/')),
            ],
        ),
    ]
