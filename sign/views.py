#coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from sign.models import Event,Guest
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # 登录
            request.session['user'] = username # 将 session 信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html', {'error': '注意：账号或密码错误！'})

# 发布会管理
@login_required
def event_manage(request):
    username = request.session.get('user', '')
    event_list = Event.objects.all()
    paginator = Paginator(event_list, 3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,"event_manage.html",{"user": username,"events":contacts})

# 签到页面
@login_required
def sign_index(request, event_id):
    no_sign_guest = Guest.objects.filter(event_id=event_id,sign=0)
    has_sign_guest = Guest.objects.filter(event_id=event_id,sign=1)
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event,'no_sign_guest':no_sign_guest,'has_sign_guest':has_sign_guest})

# 签到动作
@login_required
def sign_index_action(request,event_id):
    event = get_object_or_404(Event, id=event_id)
    no_sign_guest = Guest.objects.filter(event_id=event_id,sign=0)
    has_sign_guest = Guest.objects.filter(event_id=event_id,sign=1)
    phone = request.POST.get('phone','')
    result = Guest.objects.filter(phone = phone)

    if not result:
        return render(request, 'sign_index.html', {'event': event,'no_sign_guest':no_sign_guest,'has_sign_guest':has_sign_guest,'hint': '没有该手机号码对应的嘉宾.'})

    result = Guest.objects.filter(phone=phone,event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event,'no_sign_guest':no_sign_guest,'has_sign_guest':has_sign_guest,'hint': '签到的嘉宾不是该发布会的嘉宾.'})

    result = Guest.objects.get(phone=phone,event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event,'no_sign_guest':no_sign_guest,'has_sign_guest':has_sign_guest,'hint': "该嘉宾已签到过."})
    else:
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign = '1')
        return render(request, 'sign_index.html', {'event': event,'no_sign_guest':no_sign_guest,'has_sign_guest':has_sign_guest,'hint':'签到成功!','guest': result})

#按发布会名称搜索
@login_required
def search_event_name(request):
    username = request.session.get('user', '')
    search_event_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_event_name)
    return render(request, "event_manage.html", {"user": username,"events": event_list})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username,"guests": contacts})


# 按嘉宾姓名搜索
@login_required
def search_guest_name(request):
    username = request.session.get('user', '')
    search_guest_name = request.GET.get("realname", "")
    guest_list = Guest.objects.filter(realname__contains=search_guest_name)
    return render(request, "guest_manage.html", {"user": username,"guests":guest_list})


#主页
def index(request):
    return render(request,"index.html")

#退出登录
@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/accounts/login/')
    return response