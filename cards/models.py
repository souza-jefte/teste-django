from django.db import models

# Create your models here.
from django.db import models

class Card(models.Model):
    nome = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='cards/', null=True, blank=True)

    def __str__(self):
        return self.nome




