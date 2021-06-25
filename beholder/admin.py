from django.contrib import admin

from .models import Issue, Person, Bio, Content

# Register your models here.
admin.site.register(Issue)
admin.site.register(Person)
admin.site.register(Bio)
admin.site.register(Content)