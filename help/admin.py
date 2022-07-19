from django.contrib import admin
from .models import Document, HelpRequest


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    ...


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    ...
