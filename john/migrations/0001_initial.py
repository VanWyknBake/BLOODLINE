# Generated by Django 3.1.7 on 2021-07-21 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('career', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('profile_img', models.ImageField(upload_to='profile/')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('greetings_1', models.CharField(max_length=5)),
                ('greetings_2', models.CharField(max_length=5)),
                ('picture', models.ImageField(upload_to='picture/')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Streamers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tourn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tp', models.CharField(default='Tournament / Scrim', max_length=100)),
                ('host', models.CharField(max_length=50)),
                ('macth', models.CharField(max_length=20)),
                ('details', models.TextField()),
                ('room', models.CharField(blank=True, max_length=500, null=True)),
                ('when', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='john.category')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(default='WIN 5-0', max_length=100)),
                ('when', models.DateTimeField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='john.tourn')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=10)),
                ('link', models.URLField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='john.about')),
            ],
        ),
    ]
