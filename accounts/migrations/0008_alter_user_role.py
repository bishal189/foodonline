# Generated by Django 4.1.6 on 2023-02-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'customer'), (1, 'vendor')], null=True),
        ),
    ]