# Generated by Django 4.2.4 on 2023-10-22 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demoapp', '0005_alter_category_options_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_detail', models.BigIntegerField()),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(upload_to='')),
                ('user_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
