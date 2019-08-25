from django.contrib import admin

# Register your models here.

# Register your models here.

from .models import (
    Comments,
    Compra
)

admin.site.register(Compra)
admin.site.register(Comments)