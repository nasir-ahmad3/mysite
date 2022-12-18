from modeltranslation.translator import translator, TranslationOptions
from .models import About

# for Person model
class AboutTranslationOptions(TranslationOptions):
    fields = ('name', 'job', 'about_my_self')

translator.register(About, AboutTranslationOptions)