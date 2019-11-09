"""atheletics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from index import views as index_views
from adm import views as adm_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_views.index, name="index"),
    path('dashboard/',adm_views.adm, name="dashboard"),
    path('add_stud/',adm_views.add_stu, name="add_stu"),
    path('up_details/',adm_views.up_details, name="up_details"),
    path('up_points/',adm_views.up_points, name="up_points"),
    path('up_event/',adm_views.up_event, name="up_event"),
    path('login/',index_views.login_view, name="u_login"),
    path('logout/',index_views.logout_view, name="u_logout"),

]
