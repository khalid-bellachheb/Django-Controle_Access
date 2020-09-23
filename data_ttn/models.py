from django.db import models

# Create your models here.

AUTORISATION_TYPE=(
    ('Accés autorisé','Accés autorisé'),
    ('Accés non autorisé','Accés non autorisé'),
)

Porte_TYPE=(
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('E','E'),
)

Zone_TYPE=(
    ('Zone 1','Zone 1'),
    ('Zone 2','Zone 2'),
    ('Zone 3','Zone 3'),
)
class data_ttn(models.Model):
    badge=models.CharField(max_length=15)
    Autorisation=models.CharField(max_length=50,choices=AUTORISATION_TYPE)
    Porte=models.CharField(max_length=2,choices=Porte_TYPE)
    Zone=models.CharField(max_length=10,choices=Zone_TYPE)
    


    def __str__(self):
        return  ("badge N : "+ str(self.id))