from django.contrib import admin

from .models import Contractor,Request ,Companyorder # تأكد من استيراد النموذج الخاص بك

admin.site.register(Contractor)  # تسجيل النموذج في لوحة الإدارة
admin.site.register(Request)
admin.site.register(Companyorder)
