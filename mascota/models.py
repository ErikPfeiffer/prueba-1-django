from django.db import models

class Mascota(models.Model):
	
	nombre = models.CharField(max_length=25)
	raza = models.CharField(max_length=25)
	color = models.CharField(max_length=15)
	sexo = models.BooleanField()
	sector = models.CharField(max_length=50)
	foto = models.CharField(max_length=70)
	estado = models.BooleanField()
	recompensa = models.IntegerField()
	usuario = models.ForeingKey("Usuario")
	
	def __unicode__(self):
		return ("%s %s"%(self.nombre, self.usuario))
		

class Usuario(models.Model):
	nombre = models.CharField(max_length=25)
	correo = models.CharField(max_length=30)
	telefono = models.IntegerField()

	def __unicode__(self):
		return("%s %s"%(self.nombre, self.correo))
		



# Create your models here.
