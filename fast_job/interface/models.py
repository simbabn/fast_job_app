from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render


class Record(models.Model):
    intitule = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    entreprise = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    lieu = models.CharField(max_length=100)
    type_contrat = models.CharField(max_length=5)
    experience = models.CharField(max_length=100)
    exigences = models.TextField()
    qualification = models.CharField(max_length=100)
    qualites_pro = models.TextField()
    formations = models.CharField(max_length=100)
    langues = models.CharField(max_length=100)
    salaire = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

	
    def __str__(self):
        return(f"{self.intitule} {self.entreprise}")
    
class OffreEmploi(models.Model):
    id = models.AutoField(primary_key=True)
    intitule = models.TextField()
    description = models.TextField()
    dateCreation = models.TextField()
    dateActualisation = models.TextField()
    romeCode = models.TextField()
    romeLibelle = models.TextField()
    appellationlibelle = models.TextField()
    typeContrat = models.TextField()
    typeContratLibelle = models.TextField()
    natureContrat = models.TextField()
    experienceExige = models.BooleanField(null=True)
    experienceLibelle = models.TextField()
    dureeTravailLibelle = models.TextField()
    dureeTravailLibelleConverti = models.TextField()
    alternance = models.BooleanField(null=True)
    nombrePostes = models.BigIntegerField(null=True)
    accessibleTH = models.BooleanField(null=True)
    qualificationCode = models.BigIntegerField(null=True)
    qualificationLibelle = models.TextField()
    codeNAF = models.TextField()
    secteurActivite = models.BigIntegerField(null=True)
    secteurActiviteLibelle = models.TextField()
    offresManqueCandidats = models.BooleanField(null=True)
    deplacementCode = models.FloatField(null=True)
    deplacementLibelle = models.TextField()
    agence = models.TextField()
    complementExercice = models.TextField()
    experienceCommentaire = models.TextField()
    conditionExercice = models.TextField()
    lieuTravail_libelle = models.TextField()
    lieuTravail_latitude = models.FloatField(null=True)
    lieuTravail_longitude = models.FloatField(null=True)
    lieuTravail_codePostal = models.FloatField(null=True)
    lieuTravail_commune = models.TextField()
    entreprise_nom = models.TextField()
    entreprise_entrepriseAdaptee = models.BooleanField(null=True)
    entreprise_description = models.TextField()
    entreprise_logo = models.TextField()
    entreprise_url = models.TextField()
    salaire_libelle = models.TextField()
    salaire_complement1 = models.TextField()
    salaire_complement2 = models.TextField()
    salaire_commentaire = models.TextField()
    contact_coordonnees1 = models.TextField()
    contact_urlPostulation = models.TextField()
    contact_nom = models.TextField()
    contact_courriel = models.TextField()
    contact_coordonnees2 = models.TextField()
    contact_coordonnees3 = models.TextField()
    contact_telephone = models.FloatField(null=True)
    origineOffre_origine = models.BigIntegerField()
    origineOffre_urlOrigine = models.TextField()
    class Meta:
        db_table = 'offres_emplois'
        
    def __str__(self):
        return self.intitule 
    
    @property
    def alternance_display(self):
        return "Non" if self.alternance else "Oui"
        

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    ville = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    experiences = models.TextField(max_length=1000, blank=True)
    formations = models.TextField(max_length=1000, blank=True)
    metiers_recherches = models.CharField(max_length=100, blank=True)
    compte_linkedin = models.URLField(blank=True)
    compte_twitter = models.CharField(max_length=100, blank=True)
    compte_github = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user'
        

