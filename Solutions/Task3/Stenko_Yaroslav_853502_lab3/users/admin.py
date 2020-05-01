from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Doctor, Patient
from clinic.models import Comment
from .forms import UserSignUpForm, UserChangeForm


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class DoctorComment(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]


class CustomUserAdmin(UserAdmin):
    add_form = UserSignUpForm
    form = UserChangeForm

    list_display = ['first_name', 'last_name', 'patronymic', 'date_of_birth', 'email', 'is_admin']
    list_filter = ("is_patient", 'is_doctor')

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'patronymic', 'date_of_birth', 'email', 'password')}),
        ("Permissions", {'fields': ('is_staff', 'is_admin', 'is_patient', 'is_doctor')})
    )

    add_fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'patronymic', 'date_of_birth', 'email', 'password1', 'password2')}),
        ("Permissions", {'fields': ('is_staff', 'is_admin', 'is_patient', 'is_doctor')})
    )

    search_fields = ('email', 'is_doctor', 'is_patient')
    ordering = ('email',)

    filter_horizontal = ()


admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Doctor, DoctorComment)
