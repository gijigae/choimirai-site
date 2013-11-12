from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def verdantuserbar(context, css_file=""):
	#TODO: CSS file should by default be served from Verdant's core file system, not from implementation-specific folders
    try:
        items = ''.join(["<li>%s</li>" % item for item in context['request'].userbar])
        context.hasuserbar = True
        return """<link rel="stylesheet" href="%s" /><ul id="verdant-userbar">%s</ul>""" % (css_file, items)
    except AttributeError:
        return ''
