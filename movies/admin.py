from django.contrib import admin

from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
