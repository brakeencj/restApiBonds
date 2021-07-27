from django.contrib import admin
from bonds.models import Bond, User


@admin.register(Bond, User)
class BondAdmin(admin.ModelAdmin):
    pass
