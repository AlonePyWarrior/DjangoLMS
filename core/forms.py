from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='نام',
        widget=forms.TextInput(
            attrs={
                'class': 'input input-bordered text-md',
                'placeholder': 'نام'
            }),
    )

    last_name = forms.CharField(
        label='نام خانوادگی',
        widget=forms.TextInput(
            attrs={
                'class': 'input input-bordered text-md',
                'placeholder': 'نام خانوادگی'
            }),
    )

    phone = forms.CharField(
        label='موبایل',
        widget=forms.TextInput(
            attrs={
                'class': 'input input-bordered text-md',
                'placeholder': 'موبایل'
            }),
    )

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(
            attrs={
                'class': 'input input-bordered text-md',
                'placeholder': 'ایمیل'
            }),
    )

    password1 = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'input input-bordered text-md',
                'placeholder': 'کلمه عبور'
            }),
    )

    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'input input-bordered text-md',
                'placeholder': 'تکرار رمز عبور'
            }),
    )

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'password1',
            'password2',
        )
        exclude = ('usable_password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['data-error-message'] = f"{field.label} الزامی است."


class CustomUserChangeForm(UserChangeForm):  # -> Admin
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'email', 'gender', 'profile_img')
