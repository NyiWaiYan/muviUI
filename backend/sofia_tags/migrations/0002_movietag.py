# Generated by Django 4.1.9 on 2023-05-09 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sofia_movie', '0001_initial'),
        ('sofia_tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sofia_movie.movie')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sofia_tags.tag')),
            ],
        ),
    ]