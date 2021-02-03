from django.contrib import admin
from .models import Question


# Register your models here.
class SearchQuestion(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, SearchQuestion)
