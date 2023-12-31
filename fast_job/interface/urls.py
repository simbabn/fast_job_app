from django.urls import path
from . import views
from .views import offre_detail, liste_offres, UserProfileView, EditUserProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('enregistrer-offre/<int:offre_id>/', views.enregistrer_offre_emploi, name='enregistrer_offre_emploi'),
    path('offres-enregistrees/', views.offres_enregistrees, name='offres_enregistrees'),
    path('offre/<str:offre_id>/', offre_detail, name='offre_detail'),
    path('liste_offres/', liste_offres, name='liste_offres'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/edit/', EditUserProfileView.as_view(), name='edit_user_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view_profile/', views.view_profile, name='view_profile'),
    # path('offres_enregistrees/', views.offres_enregistrees, name='offres_enregistrees'),
    # path('enregistrer_offre/', views.enregistrer_offre, name='enregistrer_offre'),

]