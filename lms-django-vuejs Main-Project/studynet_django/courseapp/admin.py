from django.contrib import admin

# Register your models here.
from .models import MyCourse,Category,Lesson,Comment,Quiz

admin.site.register(Category)
admin.site.register(MyCourse)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Quiz)