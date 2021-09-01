from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm, Add_bookingForm
from .models import Ressource, Booking


def index(request):
    ressource_list = Ressource.objects.all()
    return render(request, 'ressources/index.html', {'ressource_list': ressource_list})


def detail(request, res_id):
    ressource = get_object_or_404(Ressource, pk=res_id)
    return render(request, 'ressources/detail.html', {'ressource': ressource})


def login(request):
    """Return a login page"""

    # If someone is already logged
    if request.user.is_authenticated:
        return redirect(reverse('django_app:index'))
    # Take all data of the form
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

    # Take all data of the form
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


@login_required
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    bookings = Booking.objects.filter(user_id=user.id)
    return render(request, 'accounts/profile.html', {"profile": user, 'bookings': bookings})


@login_required
def booking_add(request, res_id):
    """Add booking for one user"""

    # Concerned ressource of the booking
    ressource = Ressource.objects.get(id=res_id)

    # Take all data of the form
    if request.method == "POST":
        add_booking_form = Add_bookingForm(request.POST)

        if add_booking_form.is_valid():
            booking = add_booking_form.save(commit=False)
            booking.ressource_id = res_id
            booking.user_id = request.user.id  # Needs to know who add booking
            booking.save()
            return redirect('django_app:profile')

    else:
        add_booking_form = Add_bookingForm
        messages.error(request, "Réservation impossible")

    if request.user.is_authenticated:
        return render(request, 'bookings/booking_add.html', {
            "add_booking_form": add_booking_form,
            'ressource': ressource})
    else:
        return redirect(reverse('django_app:login'))


@login_required
def delete_booking(request, booking_id):
    """Delete booking selected by connected user"""
    booking_to_delete = Booking.objects.get(id=booking_id)
    booking_to_delete.delete()
    return redirect(reverse('django_app:profile'))


@login_required
def modify_booking(request, booking_id):
    """Modify booking selected by connected user"""

    booking = Booking.objects.get(id=booking_id)

    # Take all data of the form
    if request.method == "POST":
        modify_booking_form = Add_bookingForm(request.POST)

        if modify_booking_form.is_valid():

            """JE NE SAIS PAS ENCORE FAIRE POUR METTRE A JOUR..."""

            return redirect('django_app:profile')

    else:
        modify_booking_form = Add_bookingForm
        messages.error(request, "Réservation impossible")

    return render(request, 'bookings/modify_booking.html',
                  {'booking': booking, 'modify_booking_form': modify_booking_form})
