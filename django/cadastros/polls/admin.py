from django.contrib import admin
from .models import Morador, Usuario, Evento, Convidado, Veiculo

# Register your models here.
admin.site.register(Morador)
admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(Convidado)
admin.site.register(Veiculo)
