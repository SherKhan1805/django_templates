# Generated by Django 5.0.1 on 2024-01-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='Контент')),
                ('image', models.ImageField(upload_to='material/', verbose_name='изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'карта',
                'verbose_name_plural': 'карты',
                'ordering': ('title',),
            },
        ),
    ]