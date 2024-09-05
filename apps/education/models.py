from django.db import models
from ckeditor.fields import RichTextField

class EducationDegreeChoices(models.TextChoices):
    MASTER = "master","Magistratura"
    BACHELORS = "bachelors", "Bakalavr"

class LanguageChoices(models.TextChoices):
    UZ ="uz", "o'zbek tili"
    RU ="ru", "rus tili"
    EN ="en", "inglis tili"

class EducationTypesChoices(models.TextChoices):
    DAYTIME = "daytime","kundizgi"
    PART_TIME ="part_time", "sirtqi"
    EVNING ="evning", "Kechgi"

class Director(models.Model):
    full_name = models.CharField(max_length=255)
    bio = RichTextField()
    phone_number = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="images")

class Faculty(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    degree = models.CharField(max_length=255,choices=EducationTypesChoices.choices)
    dirictor = models.ForeignKey(Director,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return self.title

class Diriction(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(choices=LanguageChoices.choices,max_length=255)
    body = RichTextField()
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    education_type = models.CharField(choices=EducationTypesChoices.choices,max_length=16)

