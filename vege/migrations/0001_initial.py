# Generated by Django 5.0 on 2024-08-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reciepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reciepe_name', models.CharField(max_length=100)),
                ('Reciepe_desc', models.TextField()),
                ('Reciepe_image', models.ImageField(upload_to='reciepe')),
            ],
        ),
    ]
