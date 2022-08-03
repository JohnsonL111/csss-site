# Generated by Django 2.2.27 on 2022-07-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_auto_20220723_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officeremaillistandpositionmapping',
            name='executive_position',
        ),
        migrations.AddField(
            model_name='officeremaillistandpositionmapping',
            name='discord_manager',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='officeremaillistandpositionmapping',
            name='discord_role_name',
            field=models.CharField(default='NA', max_length=140),
        ),
        migrations.AddField(
            model_name='officeremaillistandpositionmapping',
            name='election_officer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='officeremaillistandpositionmapping',
            name='executive_officer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='officeremaillistandpositionmapping',
            name='frosh_week_chair',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='officeremaillistandpositionmapping',
            name='sfss_council_rep',
            field=models.BooleanField(default=True),
        ),
    ]