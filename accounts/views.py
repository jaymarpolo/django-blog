from django.db.models import fields
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from post.models import Profile
from .forms import *


class ProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["profile"] = profile
        return context


class CreateProfileView(generic.CreateView):
    model = Profile
    fields = ['bio', 'pic', 'link']
    template_name = 'registration/create-profile.html'
    success_url = reverse_lazy('post:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class InfoEditView(generic.UpdateView):
    model = Profile
    fields = ['bio', 'pic', 'link']
    template_name = 'registration/edit-info.html'
    success_url = reverse_lazy('post:home')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit-profile.html'
    success_url = reverse_lazy('post:home')

    def get_object(self):
        return self.request.user


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

        

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change-password.html'
    success_message = "Password was changed successfully"
    success_url = reverse_lazy('post:home')
