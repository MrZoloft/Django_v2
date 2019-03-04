from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
# Create your views here.

# 模拟数据库 定义一个数据列表
list = [{"name":'good','password':'python'},{'name':'learning','password':'django'}]


# 直接返回前端页面字符串
def index(request):
    return HttpResponse("Hello World!")


def index1(request):
    # 通过render 将index1.html 返回给前端并且 返回一个 form 变量
    name = request.POST.get('name',None)
    password = request.POST.get('password',None)

    data = {'name':name,'password':password}

    list.append(data)
    return render(request,'index1.html',{'form':list})


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))


def add2(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))


def old_add_redirect(request,a,b):
    return HttpResponseRedirect(
        reversed('add2',args=(a,b))
    )


def re_string(request):
    string = "werewrrrrrdsfdff"
    return render(request,'index1.html',{'string':string})