from dataclasses import field
from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    field =['titre']

admin.site.register(Question)
