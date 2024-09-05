from django.contrib import admin
from apps.education import models

@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display =("full_name", "bio", "phone_number")


@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display =("title", "body", "degree", "dirictor")

@admin.register(models.Diriction)
class DirictionAdmin(admin.ModelAdmin):
   list_display =("title", "language", "body","faculty", "education_type")