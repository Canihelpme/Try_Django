# Generated by Django 3.0.6 on 2020-06-01 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
