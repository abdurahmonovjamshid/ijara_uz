# Generated by Django 4.2 on 2023-04-05 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ijara_uz', '0005_customuser_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
