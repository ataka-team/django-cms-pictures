
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page
from os.path import basename
#from inline_ordering.models import Orderable



class Slider(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name 

class SliderPicture(models.Model):
    gallery = models.ForeignKey(Slider)
    image = models.ImageField(_("image"), upload_to='uploads/images')
    url = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("if present image will be clickable"))
    page_link = models.ForeignKey(Page, verbose_name=_("page"), null=True, blank=True, help_text=_("if present image will be clickable"))
    alt = models.CharField(_("alternate text"), max_length=255, blank=True, null=True, help_text=_("textual description of the image"))
    longdesc = models.CharField(_("long description"), max_length=255, blank=True, null=True, help_text=_("additional description of the image"))
    
    def __unicode__(self):
        if self.alt:
            return self.alt[:40]
        elif self.image:
            # added if, because it raised attribute error when file wasn't defined
            try:
                return u"%s" % basename(self.image.path)
            except:
                pass
        return "<empty>"



class SliderPlugin(CMSPlugin):
    slider = models.ForeignKey(Slider)
