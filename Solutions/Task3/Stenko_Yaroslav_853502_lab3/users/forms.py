from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import Patient
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'patronymic', 'date_of_birth')

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password dont match")
        return password2

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user_qs = User.objects.filter(
            Q(email__iexact=email)
        )
        if not user_qs.exists() and user_qs.count() != 1:
            raise forms.ValidationError('Invalid credentials - user does not exist')
        user_obj = user_qs.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError("Credentials are not correct!")
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
                                         help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password "
                                                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = User
        fields = ()

    def clean_password(self):
        return self.initial["password"]


class PatientSignUp(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('address',)
