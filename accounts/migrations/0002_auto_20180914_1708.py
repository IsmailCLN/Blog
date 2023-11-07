# Generated by Django 2.0.6 on 2018-09-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='userFollow', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]