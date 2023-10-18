from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register')
    # path('offres_enregistrees/', views.offres_enregistrees, name='offres_enregistrees'),
    # path('enregistrer_offre/', views.enregistrer_offre, name='enregistrer_offre'),

]