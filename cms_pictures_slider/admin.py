from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import Slider,SliderPicture

class SliderPictureInline(admin.StackedInline):
    model = SliderPicture

class SliderAdmin(admin.ModelAdmin):
    inlines = [SliderPictureInline]

admin.site.register(Slider, SliderAdmin)

