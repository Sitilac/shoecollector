# Generated by Django 3.1.1 on 2020-09-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_delete_testclean'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('top', models.CharField(max_length=50)),
                ('bottom', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='shoe',
            name='outfits',
            field=models.ManyToManyField(to='main_app.Outfit'),
        ),
    ]
