from django.contrib import admin
from . import forms as contact_forms
from . import models as contact_models

# Register your models here.
admin.site.register(contact_models.Contact_Post)