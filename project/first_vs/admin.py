from django.contrib import admin
from .models import Registered_user,Customer,Bills

admin.site.register(Registered_user)
admin.site.register(Customer)
admin.site.register(Bills)
