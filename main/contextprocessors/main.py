import config
def index(request):
    context = {}
    context['websiteTitle'] = config.websiteTitle
    context['websiteFullName'] = config.websiteFullName
    context['extensions'] = config.extensions
    return context