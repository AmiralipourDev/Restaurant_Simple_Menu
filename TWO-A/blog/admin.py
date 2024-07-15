from django.contrib import admin

from .models import Category, Food, Chef, ContactForm

# Register your models here.

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Chef)
admin.site.register(ContactForm)
