from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Business
from .models import FeatureProduct

admin.site.register(Business)
admin.site.register(FeatureProduct)