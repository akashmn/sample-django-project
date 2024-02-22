from django.contrib import admin

from .models import Movie_info, Director

#To see the tables in the admin panel, we need to register the models here.

admin.site.register(Movie_info)
admin.site.register(Director)

# Register your models here.
