from django.urls import path     
from . import views
urlpatterns = [
    path('',views.index),
    path('main/',views.MainPage,name='MainPage'),
    path('login/', views.login_view, name='login'),  # صفحة تسجيل الدخول
    path('register/', views.register, name='register'),  # صفحة التسجيل
    
    path('contractors/', views.contractor_list, name='contractor_list'),  # عرض قائمة المقاولين
    path('contractors/create/', views.contractor_create, name='contractor_create'),  # إضافة مقاول جديد
    path('contractors/update/<int:pk>/', views.contractor_update, name='contractor_update'),  # تعديل المقاول
    path('contractors/delete/<int:pk>/', views.contractor_delete, name='contractor_delete'),  # حذف المقاول  
    
    path('requests/', views.requests_list, name='requests_list'),
    path('requests/create/', views.create_request, name='create_request'),
    path('requests/update/<int:pk>/', views.update_request, name='request_update'),
    path('requests/migrate/<int:request_id>/', views.migrate_to_subscriber, name='migrate_request'),
    
    path('subscribers/', views.subscribers_list, name='subscribers_list'),
    path('requests/delete/<int:pk>/', views.delete_request, name='request_delete'),
    
    path('objections/add/', views.add_objection, name='add_objection'),
    path('objections/', views.objection_list, name='objection_list'),
    path('objections/delete/<int:objection_id>/', views.objection_delete, name='objection_delete'),
    
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/delete/<int:note_id>/', views.note_delete, name='note_delete'),

    path('employee/', views.employee_list, name='employee_list'),
    path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/update/<int:pk>/', views.employee_update, name='employee_update'),
    path('employee/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    
    
    path('items/', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    path('items/update/<int:item_id>/', views.item_update, name='item_update'),
    path('items/delete/<int:item_id>/', views.item_delete, name='item_delete'),
    
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/update/<int:order_id>/', views.order_update, name='order_update'),
    path('orders/delete/<int:order_id>/', views.order_delete, name='order_delete'),

]