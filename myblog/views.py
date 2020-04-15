# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .forms import loginForm,RegForm
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import get_seven_days_read_data,get_today_hot_data,get_yesterday_hot_data
from blog.models import Blog

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)
    today_hot_data = get_today_hot_data(blog_content_type)
    yesterday_hot_data = get_yesterday_hot_data(blog_content_type)

    context={}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = today_hot_data
    context['yesterday_hot_data'] = yesterday_hot_data
    return render(request,'home.html',context)


def login(request):
    '''
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user = auth.authenticate(request,username=username,password=password)
    referer = request.META.get('HTTP_REFERER','home')
    if user is not None:
        auth.login(request,user)
        #跳转到成功页面
        return redirect(referer)
    else:
        return render(request,'error.html',{'message':'用户名或密码不正确','redirect_to':referer})
    '''
    if request.method == 'POST': #POST类型说明从login页面请求
        login_form = loginForm(request.POST) #request.POST提供username，password等信息
        if login_form.is_valid(): #如果输入格式有效
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from',reverse('home')))# 跳转到成功页面
    else: #GET类型时说明从别的网页request跳转到login页面
        login_form = loginForm()

    context = {}
    context['login_form']=login_form
    return render(request, 'login.html', context)

def register(request):
    if request.method=='POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            #创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            #登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()
    context = {}
    context['reg_form']=reg_form
    return render(request, 'register.html', context)

def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))

def user_info(request):
    context={}
    return render(request,'user_info.html',context)