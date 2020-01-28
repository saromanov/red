from django.contrib import admin
from team.models import Profile, Team

# Register your models here.
admin.site.register(Profile, Team)
