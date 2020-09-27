from django.contrib import admin

# Register your models here.
#admin.site.register(people)
from .models import Crop

admin.site.register(Crop)
