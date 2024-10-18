from django.db import models

class Mestros(models.Model):
        name = models.CharField(null = False, editable = True, max_length = 30)
        last_name = models.CharField(null = False, editable = True, max_length = 30)
        n_reticulate = models.IntegerField(null = False)
        RFID = models.CharField(null = False, editable = True, unique = True)
        def __str__(self):
            return self.name
# Create your models here.
