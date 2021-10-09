from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import FeedBack, Issues, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
# for online offline
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Has Been created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Has Been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'u_form': u_form,
    'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):
    user.profile.is_online = True
    user.profile.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):
    user.profile.is_online = False
    user.profile.save()

class FeedBackCreateView(LoginRequiredMixin, CreateView):
    model = FeedBack
    fields = ['feedBack', ]
    template_name = 'users/feedBack.html'
    success_url = reverse_lazy('main-home')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IssuesCreateView(LoginRequiredMixin, CreateView):
    model = Issues
    fields = ['type', 'issue', ]
    template_name = 'users/issue.html'
    success_url = reverse_lazy('main-home')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
