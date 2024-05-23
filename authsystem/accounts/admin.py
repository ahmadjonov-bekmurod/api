from django.contrib import admin
from .models import UserAccount, ToDo

# admin.site.register(UserAccountManager)
admin.site.register(UserAccount)
admin.site.register(ToDo)
