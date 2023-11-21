from django.urls import path, include
from . import views
from .views import qui_sommes_nous_view,account_created,  offre_detail,update_user, delete_user, liste_offres,ProfileView, UserProfileView,ChangePasswordView,PasswordResetDoneView, EditUserProfileView, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/created/', account_created, name='account_created'),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('delete_user/', delete_user, name='delete_user'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('enregistrer-offre/<int:offre_id>/', views.enregistrer_offre_emploi, name='enregistrer_offre_emploi'),
    path('offres-enregistrees/', views.offres_enregistrees, name='offres_enregistrees'),
    path('offre/<str:offre_id>/', offre_detail, name='offre_detail'),
    path('liste_offres/', liste_offres, name='liste_offres'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditUserProfileView.as_view(), name='edit_user_profile'),
    path('update_user/<int:pk>/', update_user, name='update_user'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('qui-sommes-nous/', qui_sommes_nous_view, name='qui_sommes_nous'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
         name='password_reset'), # Assurez-vous que le nom est 'password_reset'
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('reset_password_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done')
    # path('offres_enregistrees/', views.offres_enregistrees, name='offres_enregistrees'),
    # path('enregistrer_offre/', views.enregistrer_offre, name='enregistrer_offre'),

]