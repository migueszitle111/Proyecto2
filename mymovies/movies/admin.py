from django.contrib import admin

from movies.models import Movie, Genre, Job, Person, MovieCredit, MovieReview 


class MovieCreditInLine(admin.TabularInline):
    model = MovieCredit


class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('credits', )
    inlines = (MovieCreditInLine, )


class MovieCreditAdmin(admin.ModelAdmin):
    search_fields = ["person_name", "movie_title"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Job)
admin.site.register(Person)
admin.site.register(MovieCredit, MovieCreditAdmin)
admin.site.register(MovieReview)
