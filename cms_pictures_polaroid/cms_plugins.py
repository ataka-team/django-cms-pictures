from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from cms_pictures_polaroid.models import Polaroid
from django.conf import settings

class PolaroidPlugin(CMSPluginBase):
    model = Polaroid
    name = _("Polaroid")
    render_template = "cms_pictures_polaroid/polaroid.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'polaroid': instance,
            'link': link,
            'placeholder': placeholder
        })
        return context

    def icon_src(self, instance):
        # TODO - possibly use 'instance' and provide a thumbnail image
        return settings.STATIC_URL + u"cms_pictures_polaroid/images/polaroid.png"

plugin_pool.register_plugin(PolaroidPlugin)
