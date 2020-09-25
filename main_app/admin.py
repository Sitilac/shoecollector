from django.contrib import admin
# import your models here
from .models import *

# Register your models here
admin.site.register(Shoe)
admin.site.register(Cleaning)
admin.site.register(Outfit)
