from django.contrib import admin
from .models import Student, Reja

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('ism', 'kurs', 'yosh')
    list_filter = ('kurs',)
    search_fields = ('ism',)
    list_display_links = ('ism',)

@admin.register(Reja)
class RejaAdmin(admin.ModelAdmin):
    list_display = ('sarlavha', 'student', 'sana', 'bajarildi')
    list_filter = ('bajarildi',)
    search_fields = ('sarlavha', 'student__ism')
    list_display_links = ('sarlavha',)

admin.site.register(Student)
admin.site.register(Reja)
