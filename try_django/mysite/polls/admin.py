from django.contrib import admin
# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice #data table
    extra = 3 #3개의 칸 만들어놓음
#하나의 문항에 대해서 여러개의 choice가 나올수있도록 만들기

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)