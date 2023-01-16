"""vs_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from first_vs import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ,name='home'),
    path('hello/', views.hello ,name='hello'),
    path('login/',views.login,name='login'),
    path('reg/',views.reg,name='register'),
    path('empreg/',views.emp_reg,name='emp_register'),
    path('admin1/',views.admin1,name='admin1'),
    path('customer/',views.customers,name='customers'),
    path('succ/',views.succ,name='succ'),
    path('profile/',views.profile,name='profile'),
    path('customers_/',views.customer,name='custom'),
    path('emp/',views.emp_profile,name='emp_profile'),
    path('emplogin/',views.emplogin,name='emplogin'),
    path('err/',views.err,name="err"),
    path('empinf/',views.emp_tab,name="emp_tab"),
    path('delete/<int:id>',views.delete,name='delete'),
    path('upd/<int:id>',views.up,name='update'),
    path('upd/update/<int:id>',views.update,name='updater'),
    path('chpass/',views.ch_pass,name='changepassword'),
    path('edelete/<int:id>',views.e_delete,name='edelete'),
    path('eupd/<int:id>',views.e_up,name='eupdate'),
    path('eupd/eupdate/<int:id>',views.e_update,name='eupdater'),
    path('chpass/',views.ch_pass,name='changepassword'),
    path('dept/',views.dept,name='dept'),
    path('about/',views.about,name='about'),
    ]

urlpatterns += staticfiles_urlpatterns()

# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
