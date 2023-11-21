from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect,  get_object_or_404
from .forms import SignUpForm, OffreEmploiFilterForm, UserProfileForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView,PasswordChangeView, PasswordResetConfirmView, PasswordResetCompleteView
from .models import OffreEmploi, UserProfile
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic import DetailView


from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

def account_created(request):
    return render(request, 'account_created.html')

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
    all_offreemploi = OffreEmploi.objects.all()[:9]
    print(all_offreemploi)
    return render(request, 'home_non_connecte.html', {'offres_emplois': all_offreemploi})


def home_connecte(request):
    # Récupérez toutes les offres d'emploi
    all_offreemploi = OffreEmploi.objects.all()

    # Créez un objet Paginator
    paginator = Paginator(all_offreemploi, 9)

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

    # Copiez la requête GET dans un QueryDict
    get_data = request.GET.copy()

    # Initialisation du formulaire de recherche et de filtrage
    filter_form = OffreEmploiFilterForm(get_data)

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
                Q(appellationlibelle__icontains=keywords) |
                Q(intitule__icontains=keywords) |
                Q(description__icontains=keywords)
            )
        if type_contrat:
            filtered_offreemploi = filtered_offreemploi.filter(typeContrat__icontains=type_contrat)
        if lieu_travail:
            filtered_offreemploi = filtered_offreemploi.filter(lieuTravail_libelle__icontains=lieu_travail)
        if duree_contrat:
            filtered_offreemploi = filtered_offreemploi.filter(dureeTravailLibelle__icontains=duree_contrat)
        if alternance:
            if alternance == 'Oui':
                filtered_offreemploi = filtered_offreemploi.filter(alternance=True)
            elif alternance == 'Non':
                filtered_offreemploi = filtered_offreemploi.filter(alternance=False)

        # Remplacez les paramètres de recherche par les valeurs filtrées
        get_data['keywords'] = keywords
        get_data['type_contrat'] = type_contrat
        get_data['lieu_travail'] = lieu_travail
        get_data['duree_contrat'] = duree_contrat
        get_data['alternance'] = alternance
        # Autres paramètres de filtre

    else:
        filtered_offreemploi = all_offreemploi

    # Créez un objet Paginator avec 10 offres par page
    paginator = Paginator(filtered_offreemploi, 12)
    page = request.GET.get('page')

    try:
        interface_offreemploi = paginator.page(page)
    except PageNotAnInteger:
        interface_offreemploi = paginator.page(1)
    except EmptyPage:
        interface_offreemploi = paginator.page(paginator.num_pages)

    return render(request, 'home_connecte.html', {
        'offres_emplois': interface_offreemploi,
        'filter_form': filter_form,
        'get_params': get_data.urlencode(),
    })


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
            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('account_created')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def liste_offres_emploi(request):
    offres = OffreEmploi.objects.all()
    return render(request, 'offres_enregistrees.html', {'offres': offres})


@login_required
def enregistrer_offre_emploi(request, offre_id):
    user_profile = request.user.userprofile  # Récupérer le profil de l'utilisateur connecté
    offre_emploi = OffreEmploi.objects.get(pk=offre_id)

    # Vérifiez si l'offre d'emploi est déjà enregistrée par l'utilisateur
    if offre_emploi in user_profile.offres_enregistrees.all():
        user_profile.offres_enregistrees.remove(offre_emploi)
        message = "Offre d'emploi retirée de vos enregistrements."
    else:
        user_profile.offres_enregistrees.add(offre_emploi)
        message = "Offre d'emploi ajoutée à vos enregistrements."

    return JsonResponse({'message': message})


@login_required
def offres_enregistrees(request):
    offres_enregistrees = OffreEnregistree.objects.filter(utilisateur=request.user)
    return render(request, 'offres_enregistrees.html', {'offres_enregistrees': offres_enregistrees})


def offre_detail(request, offre_id):
    offre = get_object_or_404(OffreEmploi, id=offre_id)
    return render(request, 'offre_detail.html', {'offre': offre})

def liste_offres(request):
    offres = OffreEmploi.objects.all()
    return render(request, 'liste_offres.html', context={'offres': offres})


@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        # Récupérez les informations sur l'utilisateur connecté si nécessaire
        context = {
            'user': request.user,
            # Autres données à envoyer au modèle
        }
        return render(request, self.template_name, context)


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès.')
            return redirect('user_profile')
        else:
            messages.error(request, 'Erreur lors de la mise à jour du profil. Veuillez corriger les erreurs.')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

@method_decorator(login_required, name='dispatch')
class EditUserProfileView(View):
    template_name = 'edit_user_profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        form = UserProfileForm(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user = request.user
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_profile')
        return render(request, self.template_name, {'form': form})


def edit_profile(request):
    # Logique pour afficher le formulaire de modification du profil
    return render(request, 'profile_form.html')

def view_profile(request):
    # Logique pour afficher les informations du profil
    return render(request, 'profile.html')

def qui_sommes_nous_view(request):
    return render(request, 'qui_sommes_nous.html')


@login_required
def linkedin_profile(request):
    user = request.user
    linkedin_social = user.social_auth.get(provider='linkedin-oauth2')
    linkedin_data = linkedin_social.extra_data

    return render(request, 'linkedin_profile.html', {'linkedin_data': linkedin_data})

@login_required
def delete_user(request):
    if request.method == 'POST':
        # Supprimer l'utilisateur
        user = request.user
        user.delete()
        
        # Se déconnecter
        logout(request)
        messages.success(request, "Votre compte a été supprimé avec succès.")
        
        # Rediriger vers la page d'accueil
        return redirect('home')

    return render(request, 'confirmation_delete.html')  # Créez un template pour confirmer la suppression si nécessaire

def update_user(request, pk):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)

        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('user_profile')
        else:
            form = UserProfileForm(instance=user_profile)

        return render(request, 'profile_update.html', {'form': form})
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas authentifié
        return redirect('login')



class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

###### Mot de passe 

class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('user_profile') 
    
    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'custom_reset_password.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = '/reset_password_complete/'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'