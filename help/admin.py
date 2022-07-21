from django.contrib import admin
from .models import Document, HelpRequest
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)


class DocumentInline(admin.StackedInline):
    model = Document


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
