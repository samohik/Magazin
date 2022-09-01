import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, UpdateView, ListView

from account.forms import RegisterForm
from account.models import User
from orders.models import OrderItem

logger = logging.getLogger('main')


class RegisterView(SuccessMessageMixin, generic.CreateView):
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:login')
    form_class = RegisterForm
    success_message = "Your profile was created successfully"


class EditProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'account/edit_profile.html'
    model = User
    fields = ['first_name', 'last_name', 'phone', 'image']
    success_url = reverse_lazy('account:profile')


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


class LogOutView(LoginRequiredMixin, LogoutView):
    template_name = "account/logged_out.html"


class ProfileUser(LoginRequiredMixin, TemplateView):
    """
    Show detail data of user.
    """
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileUser, self).get_context_data(**kwargs)
        context['order'] = OrderItem.objects.select_related(
            'user', 'order', 'product',
        ).filter(user=self.request.user).first()
        return context


class OrderHistory(LoginRequiredMixin, ListView):
    template_name = 'account/order_history.html'
    model = OrderItem
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderHistory, self).get_context_data(**kwargs)
        context[self.context_object_name] = OrderItem.objects.select_related(
            'product', 'order', 'user'
        ).filter(
            user=self.request.user
        )
        return context


class ProfileExample(TemplateView):
    template_name = 'account/profile_example.html'


class Account(TemplateView):
    template_name = 'account/account.html'
