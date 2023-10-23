from django.contrib import admin
from movies.models import Movie, Genre, Job, Person, MovieCredit, MovieReview,Person


class MovieCreditInLine(admin.TabularInline):
    model = MovieCredit


class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('credits', )
    inlines = (MovieCreditInLine, )

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_path')  

class MovieCreditAdmin(admin.ModelAdmin):
    search_fields = ["person_name", "movie_title",'profile_path']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Job)
admin.site.register(Person,PersonAdmin)
admin.site.register(MovieCredit, MovieCreditAdmin)
admin.site.register(MovieReview)
