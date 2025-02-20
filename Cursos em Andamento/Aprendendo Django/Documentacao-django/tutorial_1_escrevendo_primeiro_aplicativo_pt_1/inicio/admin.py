from django.contrib import admin  # type: ignore

# Register your models here.
from inicio.models import Pergunta

admin.site.register(Pergunta)
