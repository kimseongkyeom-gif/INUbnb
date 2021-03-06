# Generated by Django 2.2.5 on 2020-04-22 16:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20200310_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='accuracy',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, message='1~5 사이의 수를 입력하세요'), django.core.validators.MinValueValidator(1, message='1~5 사이의 수를 입력하세요')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='check_in',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, message='1~5 사이의 수를 입력하세요'), django.core.validators.MinValueValidator(1, message='1~5 사이의 수를 입력하세요')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='cleanliness',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, message='1~5 사이의 수를 입력하세요'), django.core.validators.MinValueValidator(1, message='1~5 사이의 수를 입력하세요')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='communication',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, message='1~5 사이의 수를 입력하세요'), django.core.validators.MinValueValidator(1, message='1~5 사이의 수를 입력하세요')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='location',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, message='1~5 사이의 수를 입력하세요'), django.core.validators.MinValueValidator(1, message='1~5 사이의 수를 입력하세요')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, message='1~5 사이의 수를 입력하세요'), django.core.validators.MinValueValidator(1, message='1~5 사이의 수를 입력하세요')]),
        ),
    ]
