from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def currentauth_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        else:
            return view_func(request, *args, **kwargs)        
    return wrapper_func

def allowed_users (allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return  render(request, '403.html')
        return wrapper_func
    return decorator

# def admindashaccess(view_func):
#     def wrapper_func(request, *args, **kwargs):
        # if request.user.is_superuser:            
        #     # return redirect('adminpage')
        #     return view_func(request, *args, **kwargs)               
        # else:
        #     return  render(request, '403.html')
    #     pass
                 
    # return wrapper_func


def superuser_member_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                          login_url='accounts:login'):
    """
    Decorator for views that checks that the user is logged in and is a staff
    member, redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator