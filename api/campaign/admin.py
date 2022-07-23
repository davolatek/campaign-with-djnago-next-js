from django.contrib import admin
from .models import Campaigns, Subcription

# Register your models here.

class CampaignsModelAdmin(admin.ModelAdmin):
    list_display = ('id','created_at', 'updated_at')
    search_fields = ('id', 'created_at', 'description', 'updated_at')
    list_per_page = 10



class SubcriptionModelAdmin(admin.ModelAdmin):
    list_display = ('id','email','created_at', 'updated_at')
    search_fields = ('id','email', 'created_at', 'updated_at')
    list_per_page = 10


admin.site.register(Campaigns, CampaignsModelAdmin)
admin.site.register(Subcription, SubcriptionModelAdmin)