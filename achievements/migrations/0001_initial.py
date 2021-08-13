# Generated by Django 3.2.6 on 2021-08-13 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
        ('habits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='achievement name')),
                ('description', models.TextField(verbose_name='achievement description')),
                ('level', models.CharField(choices=[('WOODEN', 'WOODEN'), ('BRONZE', 'BRONZE'), ('SILVER', 'SILVER'), ('GOLD', 'GOLD'), ('PLATINUM', 'PLATINUM')], max_length=30, verbose_name='achievement level')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.image')),
            ],
            options={
                'verbose_name': 'achievement',
                'verbose_name_plural': 'achievement',
            },
        ),
        migrations.CreateModel(
            name='AchievementUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('achievements', models.ManyToManyField(blank=True, to='achievements.Achievement')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
