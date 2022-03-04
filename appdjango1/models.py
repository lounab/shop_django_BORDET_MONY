from django.db import models

class Question(models.Model):
    titre = models.CharField(max_length = 200)
    lienimage = models.CharField(max_length=500)
    description = models.TextField()
    prix = models.DecimalField(max_digits=20, decimal_places=2)
    quantite = models.IntegerField()
    
    def __str__(self):
        return self.titre
