from django.db import models
from django.http import Http404
from django.shortcuts import render

from django.contrib.contenttypes.models import ContentType


class SiteManager(models.Manager):
    def get_by_natural_key(self, hostname):
        return self.get(hostname=hostname)


class Site(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    root_page = models.ForeignKey('Page')

    def natural_key(self):
        return (self.hostname,)

    def __unicode__(self):
        if self.hostname == '*':
            return "[Default site]"
        else:
            return self.hostname


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='subpages')
    content_type = models.ForeignKey('contenttypes.ContentType', related_name='pages')

    def __init__(self, *args, **kwargs):
        super(Page, self).__init__(*args, **kwargs)
        if not self.content_type_id:
            # set content type to correctly represent the model class that this was
            # created as
            self.content_type = ContentType.objects.get_for_model(self)

    def __unicode__(self):
        return self.title

    def route(self, request, path_components):
        if path_components:
            # request is for a child of this page
            child_slug = path_components[0]
            remaining_components = path_components[1:]

            try:
                subpage = self.subpages.get(slug=child_slug)
            except Page.DoesNotExist:
                raise Http404

            return subpage.route(request, remaining_components)

        else:
            # request is for this very page
            return self.serve(request)

    # TODO: metaclass voodoo so that a sensible default template path
    # (consisting of "LOWERCASED_APP_NAME/LOWERCASED_MODEL_NAME.html")
    # is defined at the point of subclassing
    template = "core/page.html"

    def serve(self, request):
        return render(request, self.template, {
            'self': self
        })
