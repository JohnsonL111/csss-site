# Generated by Django 2.2.27 on 2022-03-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_auto_20220307_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='officeremaillistandpositionmapping',
            name='executive_position',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='officeremaillistandpositionmapping',
            name='number_of_terms',
            field=models.IntegerField(choices=[(None, 'None'), (1, '1'), (2, '2'), (3, '3')], default=3, null=True),
        ),
        migrations.AddField(
            model_name='officeremaillistandpositionmapping',
            name='starting_month',
            field=models.IntegerField(choices=[(None, 'None'), (1, 'Spring'), (2, 'Summer'), (3, 'Fall')], default=3, null=True),
        ),
    ]