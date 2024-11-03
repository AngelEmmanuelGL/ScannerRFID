from django.db import models

class ALumnos(models.Model):
        name = models.CharField(null = False, editable = True, max_length = 30)
        last_name = models.CharField(null = False, editable = True, max_length = 30)
        n_reticulate = models.IntegerField(null = False)
        semester = models.IntegerField(null = False)
        career = models.CharField(null=False, editable = True)
        RFID = models.CharField(null = False, editable = True, unique = True)
        
        def __str__(self):
            return self.name

#data base models entity<->relation
#--(entity)Maaestros
#--(entity)Alumnos
#--(entity)Clases
#--(relation)Impart
#--(relation)Course

#__scheme__
#[Maestros] _ManyToMany_ --> <Impart> <-- _ManyToMany_ [Clases] _ManyToMany_ --> <Course> <-- [Alumnos]
