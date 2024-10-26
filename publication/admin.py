from django.contrib import admin

# Register your models here.

from .models import Etudiant, Note, UE, EC, Niveau

admin.site.register(Etudiant)
admin.site.register(Note)
admin.site.register(UE)
admin.site.register(Niveau)
admin.site.register(EC)

