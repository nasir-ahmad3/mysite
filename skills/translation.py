from modeltranslation.translator import translator, TranslationOptions
from .models import Skill

# for Person model
class SkillTranslationOptions(TranslationOptions):
    fields = ("title",)

translator.register(Skill, SkillTranslationOptions)