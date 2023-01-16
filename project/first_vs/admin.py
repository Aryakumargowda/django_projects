from django.contrib import admin
from .models import Registered_user,Customer,Bills,Employees,Department

admin.site.register(Registered_user)
admin.site.register(Customer)
admin.site.register(Bills)
admin.site.register(Employees)
admin.site.register(Department)