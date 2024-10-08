# Generated by Django 2.2.4 on 2024-09-27 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20240928_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة'),
        ),
        migrations.CreateModel(
            name='Objection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='objections/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Objection_created_by', to=settings.AUTH_USER_MODEL, verbose_name='أضيف بواسطة')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Objection_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='تم التعديل بواسطة')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
