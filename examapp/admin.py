from django.contrib import admin
from .models import abexam

class AbexamAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'exam_date', 'is_public', 'created_at')
    search_fields = ('exam_name', 'users__email')
    list_filter = ('is_public', 'created_at', 'exam_date')
    filter_horizontal = ('users',)
    date_hierarchy = 'exam_date'

admin.site.register(abexam, AbexamAdmin)
