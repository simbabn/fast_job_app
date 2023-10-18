from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import SignUpForm, OffreEmploiFilterForm
from .models import OffreEmploi, UserProfile

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.error(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('login')
    return render(request, 'login.html')

def home_non_connecte(request):
    # Récupérez les 10 premières offres d'emploi
    all_offreemploi = OffreEmploi.objects.all()[:10]
    print(all_offreemploi)
    return render(request, 'home_non_connecte.html', {'offres_emplois': all_offreemploi})


def home_connecte(request):
    # Récupérez toutes les offres d'emploi
    all_offreemploi = OffreEmploi.objects.all()

    # Créez un objet Paginator
    paginator = Paginator(all_offreemploi, 10)

    # Récupérez le numéro de page à partir de la requête GET
    page = request.GET.get('page')

    try:
        interface_offreemploi = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, affichez la première page
        interface_offreemploi = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée, affichez la dernière page
        interface_offreemploi = paginator.page(paginator.num_pages)

    return render(request, 'home_connecte.html', {'offres_emplois': interface_offreemploi})



def home(request):
    # Vérifie si l'utilisateur est connecté
    if not request.user.is_authenticated:
        return home_non_connecte(request)

    # Récupérez toutes les offres d'emploi
    all_offreemploi = OffreEmploi.objects.all()

    # Initialisation du formulaire de recherche et de filtrage
    filter_form = OffreEmploiFilterForm(request.GET)

    if filter_form.is_valid():
        # Traitez les données du formulaire de filtrage
        keywords = filter_form.cleaned_data.get('keywords')
        type_contrat = filter_form.cleaned_data.get('type_contrat')
        lieu_travail = filter_form.cleaned_data.get('lieu_travail')
        duree_contrat = filter_form.cleaned_data.get('duree_contrat')
        alternance = filter_form.cleaned_data.get('alternance')

        # Filtrez les offres d'emploi en fonction des critères de recherche
        filtered_offreemploi = all_offreemploi
        if keywords:
            # Recherche dans les champs pertinents (ajoutez d'autres champs si nécessaire)
            filtered_offreemploi = filtered_offreemploi.filter(
                Q(intitule__icontains=keywords) |
                Q(description__icontains=keywords)
            )
        if type_contrat:
            filtered_offreemploi = filtered_offreemploi.filter(typeContratLibelle__icontains=type_contrat)
        if lieu_travail:
            filtered_offreemploi = filtered_offreemploi.filter(lieuTravail__icontains=lieu_travail)
        if duree_contrat:
            filtered_offreemploi = filtered_offreemploi.filter(dureeTravailLibelle__icontains=duree_contrat)
        if alternance:
            if alternance == 'Oui':
                filtered_offreemploi = filtered_offreemploi.filter(alternance=True)
            elif alternance == 'Non':
                filtered_offreemploi = filtered_offreemploi.filter(alternance=False)

    else:
        filtered_offreemploi = all_offreemploi

    # Créez un objet Paginator avec 10 offres par page
    paginator = Paginator(filtered_offreemploi, 10)
    page = request.GET.get('page')

    try:
        interface_offreemploi = paginator.page(page)
    except PageNotAnInteger:
        interface_offreemploi = paginator.page(1)
    except EmptyPage:
        interface_offreemploi = paginator.page(paginator.num_pages)

    return render(request, 'home_connecte.html', {'offres_emplois': interface_offreemploi, 'filter_form': filter_form})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.userprofile.first_name = form.cleaned_data['first_name']
            user.userprofile.last_name = form.cleaned_data['last_name']
            user.userprofile.email = form.cleaned_data['email']
            user.userprofile.ville = form.cleaned_data['ville']
            user.userprofile.age = form.cleaned_data['age']
            user.userprofile.experiences = form.cleaned_data['experiences']
            user.userprofile.formations = form.cleaned_data['formations']
            user.userprofile.metiers_recherches = form.cleaned_data['metiers_recherches']
            user.userprofile.compte_linkedin = form.cleaned_data['compte_linkedin']
            user.userprofile.compte_twitter = form.cleaned_data['compte_twitter']
            user.userprofile.compte_github = form.cleaned_data['compte_github']
            user.userprofile.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def liste_offres_emploi(request):
    offres = OffreEmploi.objects.all()
    return render(request, 'offres_enregistrees.html', {'offres': offres})
