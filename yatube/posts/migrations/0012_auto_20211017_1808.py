# Generated by Django 2.2.16 on 2021-10-17 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20211003_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created'], 'verbose_name': 'Дата', 'verbose_name_plural': ('Даты',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Дата', 'verbose_name_plural': ('Даты',)},
        ),
    ]
