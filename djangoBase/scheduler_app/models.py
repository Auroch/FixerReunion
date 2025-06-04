from django.db import models
from django.contrib.auth.models import User

class Lieu(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Presence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} @ {self.lieu} on {self.date}"

class Demande(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    organisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='demandes')
    participants = models.ManyToManyField(User, related_name='invitations', blank=True)
    date = models.DateTimeField(null=True, blank=True)
    lieu = models.ForeignKey(Lieu, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titre
