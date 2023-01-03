from django.contrib import admin
from .models import Skill

# Register your models here.
class SkillAdmin(admin.ModelAdmin):
	list_display = ['title', 'description']
	list_filter= ('description',)
	search_fields = ('title', 'description')
	ordering = ('description',)
admin.site.register(Skill, SkillAdmin)