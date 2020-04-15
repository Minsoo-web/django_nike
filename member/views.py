from django.shortcuts import render, redirect
from .forms import UserCreateForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .models import Profile, Order
from product.models import Cart
from django.contrib.auth.decorators import login_required
from order.models import OrderList
from product.models import Cart


def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']
            password2 = request.POST['password2']
            if password != password2:
                return render(request, 'member/signup.html', {'message': 'password not match'})
            else:
                new_user = User.objects.create_user(username, email, password)
                new_user.save()
                return redirect('/')
        except:
            return render(request, 'member/signup.html', {'message': 'member already existed'})
    else:
        form = UserCreateForm()
    return render(request, 'member/signup.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            request.session['cart_count'] = Cart.objects.filter(
                user_id=request.user.pk).count()
        else:
            return render(request, 'member/login.html', {'message': 'password not match'})
        return redirect('/')
    else:
        login_form = AuthenticationForm()

    return render(request, 'member/login.html', {'login_form': login_form})


def logout(request):
    auth_logout(request)
    return redirect('/')


def profile(request):
    my_orders = OrderList.objects.all().order_by('-id')[:4]
    my_carts = Cart.objects.all().order_by('-id')[:4]
    context = {
        'my_orders': my_orders,
        'my_carts': my_carts
    }
    return render(request, 'member/profile.html', context)


def order(request):
    my_orders = OrderList.objects.all().order_by('-id')
    context = {
        'my_orders': my_orders
    }
    return render(request, 'member/profile-orders.html', context)


@login_required
def user_info_update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(
            request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('member:profile')
    else:
        user_change_form = UserChangeForm(instance=request.user)
    return render(request, 'member/profile-update.html', {'user_change_form': user_change_form})


@login_required
def user_info_delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/')
    return render(request, 'member/profile-delete.html')


@login_required
def user_info_password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            return redirect('/')
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'member/profile-password.html', {'password_change_form':password_change_form})
