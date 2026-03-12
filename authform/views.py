from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Users.models import RegisterUser
from django.contrib.auth.hashers import make_password, check_password


def register_view(request):
    if request.method == 'POST':
        register_user = request.POST
        FullName = register_user.get('fullname')
        DateOfBirth = register_user.get('dob')
        Gender = register_user.get('gender')
        Email = register_user.get('email')
        Phone = register_user.get('phone')
        Address = register_user.get('address')
        Username = register_user.get('username')
        Password = register_user.get('password')
        ConfirmPassword = register_user.get('confirm_password')

        if Password != ConfirmPassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('user-register')

        # Here, you would typically save the user data to the database

        hash_Password = make_password(Password)


        new_user = RegisterUser(
            FullName=FullName,
            DateOfBirth=DateOfBirth,
            Gender = Gender,
            Email=Email,
            PhoneNumber=Phone,
            Address=Address,
            username=Username,
            password=hash_Password,
        )
        new_user.save()
        messages.success(request, 'User registered successfully.')
        return redirect('user-login')
    return render(request, 'user_registration.html')

        


def userlogin(request):
    if request.method == 'POST':
        login_user = request.POST
        username = login_user.get('username')
        password = login_user.get('password')

        try:
            user = RegisterUser.objects.get(username=username)
            if check_password(password, user.password):
                messages.success(request, 'Login successful.')
                return redirect('thank-you')
            else:
                messages.error(request, 'Invalid password.')
        except RegisterUser.DoesNotExist:
            messages.error(request, 'User does not exist.')
    return render(request,'user_login.html')


def updatepasswd(request):
    if request.method == 'POST':
        update_user = request.POST
        username = update_user.get('username')
        old_password = update_user.get('current_password')
        new_password = update_user.get('new_password')

        try:
            user = RegisterUser.objects.get(username=username)
            if check_password(old_password, user.password):
                user.password = make_password(new_password)
                user.save()
                messages.success(request, 'Password updated successfully.')
                return redirect('user-login')
            else:
                messages.error(request, 'Old password is incorrect.')
        except RegisterUser.DoesNotExist:
            messages.error(request, 'User does not exist.')
    return render(request, 'user_passwd_update.html')


def thankyou(request):
    return render(request, 'thank.html')
        