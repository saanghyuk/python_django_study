# Generated by Django 3.1.7 on 2021-03-04 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_fcuser_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='password',
            field=models.CharField(max_length=300, verbose_name='비밀번호'),
        ),
    ]
