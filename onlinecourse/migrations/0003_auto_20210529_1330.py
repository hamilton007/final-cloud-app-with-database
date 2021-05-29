# Generated by Django 3.1.3 on 2021-05-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='chocies',
            new_name='choices',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='course',
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(),
        ),
    ]
