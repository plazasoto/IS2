from django.db import models
from apps.usuario.models import Usuario 
from apps.viaje.models import Viaje
# Create your models here.


class Vehiculo(models.Model):
	patente = models.CharField(max_length=30,null=True)
	marca = models.CharField(max_length=30,null=True)
	modelo = models.CharField(max_length=30,null=True)
	maleta = models.BooleanField(default=True)
	color = models.CharField(max_length=30,null=True)
	Numeroasientos = models.IntegerField(default = 0)
	consumo = models.IntegerField(default = 10)
	foto = models.ImageField(upload_to='autos', null =True)

class Conductor(models.Model):
	clasedelicencia = models.CharField(max_length=1)
	fecha_obtencion = models.CharField(max_length=30,null=False)
	user = models.OneToOneField(Usuario, null= True, blank=True, on_delete=models.CASCADE)
	viaje = models.ForeignKey(Viaje, null= True, blank=True, on_delete=models.CASCADE)
	car = models.OneToOneField(Vehiculo, null = True, blank = True, on_delete=models.CASCADE)
	
	class Meta:
		verbose_name = "Conductor"
		verbose_name_plural = "Conductores"

	def __unicode__(self):
		return str(self.id)

