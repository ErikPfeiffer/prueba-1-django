from django.contrib import admin
from . import models

@admin.register(models.Mascota)
class MascotaAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	pass



# Register your models here.
