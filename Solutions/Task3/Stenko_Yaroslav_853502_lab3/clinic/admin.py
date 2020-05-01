from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Schedule, Comment

admin.site.register(Schedule)
admin.site.register(Comment)
