from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import SliderPlugin, SliderPicture
from django.utils.translation import ugettext as _

class CMSSliderPlugin(CMSPluginBase):
    model = SliderPlugin
    name = _("Gallery Slider")
    render_template = "cms_pictures_slider/slider.html"

    def render(self, context, instance, placeholder):
        context.update({
            'slider':instance.slider,
            'pictures':SliderPicture.objects.all(),
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSSliderPlugin)

