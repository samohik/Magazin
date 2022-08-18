import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, FormView

from account.forms import RegisterForm, EditUserForm

logger = logging.getLogger('main')


class RegisterView(SuccessMessageMixin, generic.CreateView):
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:login')
    form_class = RegisterForm
    success_message = "Your profile was created successfully"


class EditProfileView(FormView):
    template_name = 'account/edit_profile.html'
    form_class = EditUserForm
    success_url = reverse_lazy('account:edit_profile')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return
        else:
            context = {'form': self.form_class(instance=request.user)}
            return render(request, self.template_name, context)


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('account:profile')


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


class AuthenticateView(LoginView):
    template_name = "account/login.html"

    def form_valid(self, form):
        return super(AuthenticateView, self).form_valid(form)


class LogOutView(LogoutView):
    template_name = "account/logged_out.html"


class ProfileUser(LoginRequiredMixin, TemplateView):
    """
    Show detail data of user.
    """
    template_name = 'account/profile.html'


class ProfileExample(TemplateView):
    template_name = 'account/profile_example.html'


class Account(TemplateView):
    template_name = 'account/account.html'
