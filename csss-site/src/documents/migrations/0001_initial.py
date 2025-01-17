# Generated by Django 2.2.9 on 2020-02-01 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('date', models.DateField(help_text='Date', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='only relevant if each album has a specific theme', max_length=1000, verbose_name='Name of Album')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_name', models.CharField(max_length=140, primary_key=True, serialize=False, verbose_name='Event Type')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='File name to Display', max_length=140, verbose_name='Name')),
                ('album_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Album')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('absolute_file_path', models.CharField(help_text='Location of File on Server', max_length=1000, verbose_name='File Path')),
                ('static_path', models.CharField(help_text='Directory that will be used for static serving of the media', max_length=2000, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('name', models.CharField(default='', help_text='Name of repository', max_length=50)),
                ('url', models.CharField(default='', help_text='URL for repository', max_length=2000)),
                ('absolute_path', models.CharField(default='', help_text='Directory where repository is cloned to', max_length=2000, primary_key=True, serialize=False)),
                ('static_path', models.CharField(blank=True, default='', help_text='Directory that will be used for static serving of the media', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('youtube_link', models.CharField(default='', max_length=500, primary_key=True, serialize=False, verbose_name='YouTube Link')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.BigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Media')),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Picture'),
        ),
        migrations.AddField(
            model_name='media',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Video'),
        ),
        migrations.AddField(
            model_name='album',
            name='album_thumbnail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Media'),
        ),
        migrations.AddField(
            model_name='album',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Event'),
        ),
    ]
