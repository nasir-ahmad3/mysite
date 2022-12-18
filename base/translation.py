from modeltranslation.translator import translator, TranslationOptions
from .models import contact

# for Person model
class ContactTranslationOptions(TranslationOptions):
    fields = ('address',)

translator.register(contact, ContactTranslationOptions)