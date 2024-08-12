# Generated by Django 5.1 on 2024-08-12 08:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_director_name_alter_movie_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.PositiveIntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
