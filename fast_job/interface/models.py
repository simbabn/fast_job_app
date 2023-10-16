from django.db import models


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