from django.contrib import admin

from .models import Student,Qna,Answers

class AnswersAdmin(admin.ModelAdmin):
    readonly_fields=('shown_at',)

# Register your models here.
admin.site.register(Student)
admin.site.register(Qna)
admin.site.register(Answers,AnswersAdmin)
