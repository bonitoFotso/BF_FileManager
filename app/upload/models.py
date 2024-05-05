from django.db import models

class Fichier(models.Model):
    nom = models.CharField(max_length=100)
    fichier = models.FileField(upload_to='fichiers/')

    def __str__(self):
        return self.nom
