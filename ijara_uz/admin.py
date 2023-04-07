from django.contrib import admin
from .models import CustomUser, User, Apartment

admin.site.register([CustomUser, User, Apartment])
