from email import message
from django.shortcuts import render, redirect
from accounts.models import User, UserProfile
from .forms import UserForm
from vendor.forms import VendorForm
from django.contrib import messages
# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.role = User.CUSTOMER
            user.set_password(password)
            user.save()
            messages.success(request, 'Your account has been registered successfully')
            return redirect('registerUser')
        else:
            # messages.error(request, form.errors)
            pass
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/registerUser.html', context)


def registerVendor(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        vendor_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and vendor_form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.role = User.VENDOR
            user.set_password(password)
            user.save()

            vendor = vendor_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()

            messages.success(request, 'Your account has been registered successfully! Please wait for our approval.')
            return redirect('registerVendor')
        else:
            # messages.error(request, form.errors)
            pass
    else:    
        form = UserForm()
        vendor_form = VendorForm()

    context = {
        'form': form,
        'vendor_form': vendor_form
    }

    return render(request, 'accounts/registerVendor.html', context)


