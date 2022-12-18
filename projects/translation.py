from modeltranslation.translator import translator, TranslationOptions
from .models import Project

# for Person model
class ProjectTranslationOptions(TranslationOptions):
    fields = ("title", "description")

translator.register(Project, ProjectTranslationOptions)