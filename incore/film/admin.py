from django.contrib import admin
from .models import Film
from import_export.admin import ImportExportModelAdmin



class FilmAdmin(ImportExportModelAdmin, admin.ModelAdmin, ):
    list_display_links= ('title', 'createDate',)
    list_display=( 'title','createDate',)
    list_filter = ('createDate', 'genre', 'place')
    search_fields = ('title', 'createDate',  )
    filter_horizontal = ('genre','timetable','place',)
    


admin.site.register(Film, FilmAdmin)


