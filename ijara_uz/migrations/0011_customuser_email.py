# Generated by Django 4.2 on 2023-04-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ijara_uz', '0010_alter_apartment_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default=998909096835, max_length=254),
            preserve_default=False,
        ),
    ]
