from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.db.models import Q
from django.utils import timezone


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'تم إنشاء الحساب بنجاح لـ {username}')
            return redirect('login')  # إعادة التوجيه إلى صفحة تسجيل الدخول
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('MainPage')  # إعادة التوجيه إلى الصفحة الرئيسية بعد تسجيل الدخول
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
    return render(request, 'login.html')

@login_required
def MainPage(request):
    return render(request,"MainPage.html")

def index(request):
    return render(request,"index.html")



@login_required
def contractor_list(request):
    query = request.GET.get('q')  # استلام المدخل من المستخدم
    if query:
        contractors = Contractor.objects.filter(
            Q(name__icontains=query) |  # البحث في الاسم
            Q(id_number__icontains=query) |  # البحث في رقم الهوية
            Q(mobile_number__icontains=query) |  # البحث في رقم الهاتف
            Q(profession__icontains=query)   # البحث في المهنة
        )
    else:
        contractors = Contractor.objects.all()
    return render(request, 'contractor_list.html', {'contractors': contractors})


@login_required
def contractor_create(request):
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            contractor = form.save(commit=False)
            contractor.created_by = request.user
            contractor.updated_by = request.user
            contractor.save()
            return redirect('contractor_list')
    else:
        form = ContractorForm()
    return render(request, 'contractor_form.html', {'form': form})

@login_required
def contractor_update(request, pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    if request.method == 'POST':
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            contractor = form.save(commit=False)
            contractor.updated_by = request.user
            contractor.save()
            return redirect('contractor_list')
    else:
        form = ContractorForm(instance=contractor)
    return render(request, 'contractor_form.html', {'form': form})

@login_required
def contractor_delete(request, pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    if request.method == 'POST':
        contractor.delete()
        return redirect('contractor_list')
    return render(request, 'contractor_confirm_delete.html', {'contractor': contractor})



@login_required
def requests_list(request):
    query = request.GET.get('q')  # استلام المدخل من المستخدم
    if query:
        requests = Request.objects.filter(
            Q(subscriber_name__icontains=query) |  # البحث في الاسم
            Q(id_number__icontains=query) |  # البحث في رقم الهوية
            Q(phone_number__icontains=query) |  # البحث في رقم الهاتف
            Q(request_number__icontains=query) |  # البحث في المهنة
            Q(residence__icontains=query) |  #هن

            Q(notes__icontains=query)   # 

        )
    else:
        
        requests = Request.objects.all()
    return render(request, 'requests.html', {'requests': requests})

@login_required
def migrate_to_subscriber(request, request_id):
    # جلب الطلب بناءً على request_id
    request_obj = get_object_or_404(Request,pk=request_id)
    
    new_subscriber = Subscriber(
        name=request_obj.subscriber_name,
        id_number=request_obj.id_number,
        phone_number=request_obj.phone_number,
        residence=request_obj.residence,
        notes=request_obj.notes,
        migration_by=request.user,  # الشخص الذي يقوم بالترحيل هو المستخدم الحالي
        migration_at=timezone.now()  # تاريخ الترحيل الحالي
    )
    new_subscriber.save()

    # حذف الطلب من جدول الطلبات بعد الترحيل
    request_obj.delete()


    return redirect('subscribers_list')


@login_required
def subscribers_list(request):
    query = request.GET.get('q')
    if query:
        subscribers = Subscriber.objects.filter(
            Q(name__icontains=query) |
            Q(id_number__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(residence__icontains=query) |  # البحث في الإقامة
            Q(notes__icontains=query)  # البحث في الملاحظات
        )
    else:
        subscribers = Subscriber.objects.all()
    return render(request, 'subscribers_list.html', {'subscribers': subscribers})

  


@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            requests = form.save(commit=False)
            requests.created_by = request.user
            requests.updated_by = request.user
            form.save()  # حفظ الطلب الجديد في قاعدة البيانات
            messages.success(request, 'تم إضافة الطلب بنجاح!')
            return redirect('requests_list')  # إعادة التوجيه إلى قائمة الطلبات
    else:
        form = RequestForm()
    
    return render(request, 'create_request.html', {'form': form})


@login_required
def update_request(request, pk):
    request_obj = get_object_or_404(Request, pk=pk)
    if request.method == 'POST':
        form = RequestForm(request.POST, instance=request_obj)
        if form.is_valid():
            form.save()
            return redirect('requests_list')  # إعادة التوجيه إلى قائمة الطلبات بعد التحديث
    else:
        form = RequestForm(instance=request_obj)
    
    return render(request, 'update_request.html', {'form': form})


@login_required
def delete_request(request, pk):
    request_obj = get_object_or_404(Request, pk=pk)
    request_obj.delete()
    return redirect('requests_list')  # إعادة التوجيه إلى قائمة الطلبات بعد الحذف


from .models import Objection,Note
from .forms import ObjectionForm,NoteForm

@login_required
def add_objection(request):
    if request.method == 'POST':
        form = ObjectionForm(request.POST, request.FILES)
        if form.is_valid():
            objection = form.save(commit=False)
            objection.user = request.user
            objection.created_by = request.user
            objection.save()
            return redirect('objection_list')
    else:
        form = ObjectionForm()
    return render(request, 'objection_form.html', {'form': form})

# views.py
@login_required
def objection_list(request):
    objections = Objection.objects.all()
    return render(request, 'objection_list.html', {'objections': objections})



@login_required
def objection_delete(request, objection_id):
    objection = get_object_or_404(Objection, id=objection_id)
    if request.user == objection.created_by:
        objection.delete()
    return redirect('objection_list')  # إعادة التوجيه إلى قائمة الاعتراضات



@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.created_by = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes_form.html', {'form': form})

# views.py
@login_required
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes_list.html', {'notes': notes})



@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.user == note.created_by:
        note.delete()
    return redirect('note_list')  # 






@login_required
def employee_list(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(
            Q(name__icontains=query) |
            Q(id_number__icontains=query) |
            Q(mobile_number__icontains=query)|
            Q( profession__icontains=query) |
            Q(salary__icontains=query) |
            Q(notes__icontains=query)
        )
    else:
        employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.created_by = request.user
            employee.updated_by = request.user
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.updated_by = request.user
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})

@login_required
def item_list(request):
    query = request.GET.get('q')
    if query:
        items = Item.objects.filter(
            Q(item_code__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})



@login_required
def item_create(request):
    if request.method == 'POST':
        item_code = request.POST.get('item_code')
        description = request.POST.get('description')
        item = Item(item_code=item_code, description=description, created_by=request.user)
        item.save()
        return redirect('item_list')
    return render(request, 'item_create.html')

@login_required
def item_update(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.item_code = request.POST.get('item_code')
        item.description = request.POST.get('description')
        item.updated_by = request.user
        item.save()
        return redirect('item_list')
    return render(request, 'item_update.html', {'item': item})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.contrib.auth.decorators import login_required




@login_required
def item_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('item_list')



@login_required
def order_list(request):
    query = request.GET.get('q')
    if query:
        orders = Companyorder.objects.filter(
            Q(item_code__icontains=query) |
            Q(price__icontains=query) 

        )
    else:
        orders = Companyorder.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


@login_required
def order_create(request):
    if request.method == 'POST':
        form = CompanyorderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user  # Assign the current user as the creator
            order.save()
            return redirect('order_list')
    else:
        form = CompanyorderForm()
    return render(request, 'order_form.html', {'form': form})

@login_required
def order_update(request, order_id):
    order = Companyorder.objects.get(id=order_id)
    if request.method == 'POST':
        form = CompanyorderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.updated_by = request.user  # Assign the current user as the one who updated the record
            order.save()
            return redirect('order_list')
    else:
        form = CompanyorderForm(instance=order)
    return render(request, 'order_form.html', {'form': form})

@login_required
def order_delete(request, order_id):
    order = get_object_or_404(Companyorder, id=order_id)
    
    # تأكد من أن المستخدم الذي يطلب الحذف هو من قام بإضافة أو تعديل الحساب أو لديه صلاحية الحذف
    if request.method == 'POST':
        order.delete()  # احذف الحساب
        return redirect('order_list')  # بعد الحذف، إعادة توجيه إلى قائمة الحسابات
    
    return render(request, 'order_confirm_delete.html', {'order': order})




def contractor_detail(request, contractor_id):
    contractor = get_object_or_404(Contractor, id=contractor_id)  # استرداد المقاول بناءً على المعرف
    return render(request, 'contractor_detail.html', {'contractor': contractor})  # تمرير المقاول إلى القالب

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)  # استرداد المقاول بناءً على المعرف
    return render(request, 'employee_detail.html', {'employee': employee})  # تمرير المقاول إلى القالب

def subscribers_detail(request, subscribers_id):
    subscriber= get_object_or_404(Subscriber, id=subscribers_id)  # استرداد المقاول بناءً على المعرف
    return render(request, 'subscribers_detail.html', {'subscriber': subscriber})  # تمرير المقاول إلى القالب
