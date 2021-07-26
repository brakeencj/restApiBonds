from django.contrib import admin
from bonds.models import Bond, User, Purchase


@admin.register(Bond, User, Purchase)
class BondAdmin(admin.ModelAdmin):
    pass
