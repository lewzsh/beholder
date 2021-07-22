from django.contrib import admin

from .models import Issue, Person, Bio, Content

# Admin customization
class IssueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'release_date')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'role')

class BioAdmin(admin.ModelAdmin):
    list_display = ('person', 'pronouns')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue', 'page')
    list_filter = ('issue',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('page',)


# Register your models here.
admin.site.register(Issue, IssueAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Bio, BioAdmin)
admin.site.register(Content, ContentAdmin)