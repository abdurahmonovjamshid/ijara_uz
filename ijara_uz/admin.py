from django.contrib import admin
from .models import CustomUser, User

admin.site.register([CustomUser, User])
