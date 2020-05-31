from django.contrib import admin

from .models import reporter, article

admin.site.register(reporter)

class articleAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['article']
    list_display = ('article', 'pub_date')
    fieldsets = [
        (None,               {'fields': ['article']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
admin.site.register(article)