from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from core.forms import CustomUserCreationForm
from core.models import CustomUser


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')


class UserUpdateProfile(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    template_name = 'account/update.html'
    fields = ['profile_img', ]
    success_url = reverse_lazy('home')
