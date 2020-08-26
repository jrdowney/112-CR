from django.contrib import admin
from .models import Genre, Movie, Contact

# Register your models here.
class GenreTemplate(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

# tuple
class MovieTemplate(admin.ModelAdmin):
    list_display = ("id", "title", "release_year", "price")
    list_display_links = ("id", "title")
    fields = ("date_created", "release_year", "genre",  "title", "price", "director", "image_url", "description")
    # exclude = ("price",)

admin.site.register(Genre, GenreTemplate)
admin.site.register(Movie, MovieTemplate)
admin.site.register(Contact)