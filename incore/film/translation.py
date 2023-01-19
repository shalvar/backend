from modeltranslation.translator import translator, TranslationOptions
from film.models import Film


class FilmOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Film, FilmOptions)