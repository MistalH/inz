# Generated by Django 4.2.4 on 2023-11-20 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gory', '0011_zgloszenie_oddzial_ratowniczy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='zgloszenie',
            name='historia_oddzialow',
            field=models.ManyToManyField(blank=True, related_name='historia_zgloszen', to='Gory.oddzialratowniczy'),
        ),
        migrations.AlterField(
            model_name='zgloszenie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zgloszenia', to=settings.AUTH_USER_MODEL),
        ),
    ]
