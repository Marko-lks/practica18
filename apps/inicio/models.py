from django.db import models

class alumno(models.Model):
    nombres=models.CharField(max_length=300)
    apellp=models.CharField(max_length=50)
    apellm=models.CharField(max_length=50)
    edad=models.IntegerField(default=0)
    carrera=models.CharField(max_length=100)

    def __unicode__(self):
        return self.apellp+" "+self.apellm+" "+self.nombres

