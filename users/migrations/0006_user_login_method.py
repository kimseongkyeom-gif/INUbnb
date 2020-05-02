# Generated by Django 2.2.5 on 2020-02-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200203_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('kakao', 'Kakao')], default='email', max_length=50),
        ),
    ]
