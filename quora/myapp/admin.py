from django.contrib import admin
from .import models
# Register your models here.

myModels = [models.questions_model,models.answers_model,models.profile]  # iterable list
admin.site.register(myModels)
