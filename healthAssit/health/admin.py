from django.contrib import admin
from .models import UserProfile, HealthRecord, SkinDisease

admin.site.register(UserProfile)
admin.site.register(HealthRecord)
admin.site.register(SkinDisease)