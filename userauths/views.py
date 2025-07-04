from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.views import View
from django.contrib import auth

from userauths.models import User



# Create your views here.

class LoginView(View):
    def get(self, request):

        if request.user.is_authenticated:
            messages.warning(request, "انت مسجل دخول بالفعل")
            return redirect ("/")
        else :
            return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST['username'].lower()
        password = request.POST['password']

        next_url = request.POST.get('next')
        
        if username and password :
            
            user=auth.authenticate(username=username, password=password)
            if user :
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, f'مرحبا {user.full_name} تم تسجيل الدخول بنجاح')
                    return redirect(next_url)

                messages.error(request, 'تم ايقاف الحساب .. يرجي مراجعة الادارة')
                return render(request, 'login.html')

            messages.error(request, 'بيانات الدخول غير صحيحة ... حاول مره اخري')
            return render(request, 'login.html')
        
        messages.error(request, 'من فضلك املا جميع الحقول')
        return render(request, 'login.html')
    


class LogoutView(View):
    def post (self, request):
        auth.logout(request)
        messages.success(request, 'تم تسجيل الخروج من البرنامج')
        return redirect('/')




@login_required
@permission_required('userauths.view_user', raise_exception=True)
def show_users (request):
    # users = User.objects.filter(is_superuser = False)
    users = User.objects.all()
    

    context = {
        'users' : users,
        
    }
    return render (request, 'users-list.html', context)



@login_required
@permission_required('userauths.add_user', raise_exception=True)
def add_user (request):
    
    departments = Department.objects.all()
    groups = Group.objects.all()

    context = {
        'departments' : departments,
        'groups' : groups,
    }
    return render (request, 'add-user.html', context)


@login_required
@permission_required('userauths.add_user', raise_exception=True)
def save_user (request):
    
    if request.method=='POST' :
        
        full_name = request.POST.get('full_name')
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        active = request.POST.get('active')
        department_id = request.POST.get('department_id')
        job = request.POST.get('job')
        details = request.POST.get('details')
        group_id = request.POST.get('group_id')

        
        if not User.objects.filter(username=username).exists():
            
            if not User.objects.filter(email=email).exists():
                if password1 != password2 or len(password1) < 6 or len(password2) < 6 :
                    messages.error(request,'Passwords Not Same Or Less than 6 Charecters')
                    return redirect("userauths:add-user")
                
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    full_name=full_name,
                    job=job,
                    phone=phone,
                    details=details,
                    is_active=active,
                    is_staff=active,
                    department_id=department_id,
                )
                user.set_password(password1)
                user.save()

                if group_id:
                    my_group = Group.objects.get(id=group_id)
                    my_group.user_set.add(user)
                    

                
                messages.success(request, 'Used Added Successfuly')
                return redirect("userauths:users")
        
            else :
                messages.error(request, 'Email Used Before ... Try again')
                return redirect("userauths:users")
        else :
            messages.error(request, 'Username Used Before ... Try again')
            return redirect("userauths:users")
    
    return redirect('userauths:users')


