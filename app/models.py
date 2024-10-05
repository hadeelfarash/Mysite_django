# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Contractor(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المقاول")
    id_number = models.CharField(max_length=20, verbose_name="رقم الهوية")
    mobile_number = models.CharField(max_length=15, verbose_name="رقم الجوال")
    profession = models.CharField(max_length=100, verbose_name="المهنة")
    notes = models.TextField(blank=True, verbose_name="ملاحظات")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contractor_created_by', verbose_name="أضيف بواسطة")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contractor_updated_by', verbose_name="تم التعديل بواسطة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")

    def __str__(self):
        return self.name


class Request(models.Model):
    subscriber_name = models.CharField(max_length=100, verbose_name="اسم المشترك ")
    id_number = models.CharField(max_length=20, verbose_name="رقم الهوية")
    phone_number = models.CharField(max_length=15, verbose_name="رقم الهاتف ")
    request_number = models.CharField(max_length=20, verbose_name="رقم الطلب ")
    residence = models.CharField(max_length=200, verbose_name="مكان السكن ")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='subscriber_created_by', verbose_name="أضيف بواسطة")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='subscriber_updated_by', verbose_name="تم التعديل بواسطة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subscriber_name


class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    residence  = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    migration_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='subscriber_migration_by', verbose_name="تم الترحيل بواسطة")
    migration_at = models.DateTimeField(default=timezone.now, verbose_name="تاريخ الترحيل")
    

    def __str__(self):
        return self.name



class Objection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # الاعتراض مرتبط بالمستخدم
    note = models.TextField(blank=True, null=True)  # حقل ملاحظة نصية
    image = models.ImageField(upload_to='objections/', blank=True, null=True)  # حقل تحميل صورة
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإنشاء
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Objection_created_by', verbose_name="أضيف بواسطة")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Objection_updated_by', verbose_name="تم التعديل بواسطة")
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"اعتراض من {self.user.username}"

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # الملاحظة مرتبط بالمستخدم
    note = models.TextField(blank=True, null=True)  # حقل ملاحظة نصية
    image = models.ImageField(upload_to='notes/', blank=True, null=True)  # حقل تحميل صورة
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإنشاء
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Note_created_by', verbose_name="أضيف بواسطة")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Note_updated_by', verbose_name="تم التعديل بواسطة")
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"ملاحظة من {self.user.username}"
    
    


class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الموظف")
    id_number = models.CharField(max_length=20, verbose_name="رقم الهوية")
    mobile_number = models.CharField(max_length=15, verbose_name="رقم الجوال")
    profession = models.CharField(max_length=100, verbose_name="المهنة")
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # حقل الراتب
    notes = models.TextField(blank=True, verbose_name="ملاحظات")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Employee_created_by', verbose_name="أضيف بواسطة")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Employee_updated_by', verbose_name="تم التعديل بواسطة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")

    def __str__(self):
        return self.name



class Item(models.Model):
    item_code = models.CharField(max_length=50, unique=True)  # رمز الصنف
    description = models.CharField(max_length=255)  # وصف الصنف
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='item_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='item_updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description



class Companyorder(models.Model):
    item_code = models.CharField(max_length=100)  # Code for the item
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per unit
    quantity = models.IntegerField()  # Quantity required
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Total cost (calculated)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='companyorder_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='companyorder_updated_by')
    created_at = models.DateTimeField(auto_now_add=True)  # Date added
    updated_at = models.DateTimeField(auto_now=True)  # Date updated

    def save(self, *args, **kwargs):
        self.total_cost = self.price * self.quantity  # Calculate total cost
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.item_code} - {self.total_cost}"

