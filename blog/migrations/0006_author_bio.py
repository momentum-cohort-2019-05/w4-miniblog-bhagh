# Generated by Django 2.2.2 on 2019-06-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190622_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(help_text='Enter your bio here.', max_length=300, null=True),
        ),
    ]
