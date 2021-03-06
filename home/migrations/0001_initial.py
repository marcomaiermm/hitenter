# Generated by Django 3.0.8 on 2020-07-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('Source', models.CharField(blank=True, max_length=200, null=True)),
                ('Image', models.ImageField(default='default.jpg', upload_to='banner')),
            ],
        ),
    ]
