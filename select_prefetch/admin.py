from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)