from django.contrib import admin
from .models import *
from .models import Category
from modeltranslation.admin import TranslationAdmin



@admin.register(Lesson,Exam, Course,Teacher,Student)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )

        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
               }


@admin.register(Category)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Option)
admin.site.register(Question)
admin.site.register(Assignment)
admin.site.register(Certificate)
admin.site.register(CourseReview)
admin.site.register(TeacherReview)
admin.site.register(TeacherRating)
