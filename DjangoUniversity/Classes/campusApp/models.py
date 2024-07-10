from django.db import models

# Create your models here.

class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False) #Creating a Character Field
    campus_id = models.IntegerField(default="", blank=True, null=False) #Creating an Integer Field
    state = models.CharField(max_length=2, default="", blank="True", null="False") #Creating a Character Field

object = models.Manager()

def __str__(self):
    display_course = '{0.title}: {0.instructor_name}'
    return display_course.format(self)

class Meta:
    verbose_name_plural = "University Campus" #Prevents Plural Names