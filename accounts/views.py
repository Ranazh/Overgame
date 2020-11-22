from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from accounts import models, forms
from django.urls import reverse_lazy

# Create your views here.
from accounts.forms import EditProfileForm
from post.models import Post


def index(request):
    return render(request, 'home.html')


def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})


class ByeView(generic.TemplateView):
    template_name = 'accounts/Bye.html'


class SuccessLoginView(generic.TemplateView):
    template_name = 'accounts/success.html'


class UserCreateView(generic.CreateView):
    model = models.UserProfile
    form_class = forms.UserProfileForm
    template_name = 'accounts/register.html'
    extra_context = {'my_form': form_class}
    success_url = reverse_lazy('main')


def userprofile(request):
    user = request.user
    user_posts = Post.objects.filter(author=request.user).order_by('-date_created')
    template = 'accounts/user.html'
    return render(request, template, {'user_posts': user_posts, 'user': user})


def update_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:user')
        else:
            return redirect('accounts:editProfile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'my_form': form}
        return render(request, 'accounts/update_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:user')
        else:
            return redirect('accounts:changePassword')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

