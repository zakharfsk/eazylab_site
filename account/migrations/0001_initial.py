# Generated by Django 4.1 on 2022-09-02 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('telegram', models.CharField(blank=True, max_length=50, null=True)),
                ('educational_institution', models.CharField(blank=True, max_length=300, null=True)),
                ('faculty', models.CharField(blank=True, max_length=250, null=True)),
                ('speciality', models.CharField(blank=True, max_length=250, null=True)),
                ('course', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]