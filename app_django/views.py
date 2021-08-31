from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm
from .models import Ressource


def index(request):
    ressource_list = Ressource.objects.all()
    return render(request, 'ressources/index.html', {'ressource_list': ressource_list})


def detail(request, res_id):
    ressource = get_object_or_404(Ressource, pk=res_id)
    return render(request, 'ressources/detail.html', {'ressource': ressource})


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('django_app:index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "Succès connexion ! O/")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('django_app:profile'))
            else:
                login_form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'login_form': login_form})


def register(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('django_app:index'))

    if request.method == "POST":
        registration_form = UserRegisterForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Vous avez bien été inscrit")
            else:
                messages.error(request, "Impossible de vous inscrire, veuillez réessayer ultérieurement")
    else:
        registration_form = UserRegisterForm
    return render(request, 'accounts/register.html', {
        "register_form": registration_form})


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "Déconnexion réussie")
    return redirect(reverse('django_app:index'))


def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'accounts/profile.html', {"profile": user})


def booking_add(request):
    """Add booking for one user"""

    if request.user.is_authenticated:
        return render(request, 'bookings/booking_add.html')
    else:
        return redirect(reverse('django_app:login'))


