"""Django_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include




urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^index/', views.index,name='index'),
    # url(r'^index1/', views.index1,name='index1'),
    # # name 用于找到templates models views 等中得到对应的网址，给网址取一个名字
    # path('add/',views.add,name='add'),
    # path('add2/<int:a>/<int:b>/',views.add2,name='add2'),
    # path('new_add/<int:a>/<int:b>/',views.add2,name='add2'),
    # path('re_string/',views.re_string,name='index1'),
    # url(r'^$',views.index,name='index')
    # 将blog 应用下的 urls 包含进来
    url(r'',include('blog.urls')),
    url(r'', include('comments.urls')),
]
