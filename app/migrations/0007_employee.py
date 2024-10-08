# Generated by Django 2.2.4 on 2024-09-27 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم الموظف')),
                ('id_number', models.CharField(max_length=20, verbose_name='رقم الهوية')),
                ('mobile_number', models.CharField(max_length=15, verbose_name='رقم الجوال')),
                ('profession', models.CharField(max_length=100, verbose_name='المهنة')),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('notes', models.TextField(blank=True, verbose_name='ملاحظات')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Employee_created_by', to=settings.AUTH_USER_MODEL, verbose_name='أضيف بواسطة')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Employee_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='تم التعديل بواسطة')),
            ],
        ),
    ]
