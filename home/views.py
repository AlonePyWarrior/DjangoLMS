from django.conf import settings
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_control


@method_decorator(cache_control(max_age=settings.CACHE_MAX_AGE, public=True), name='dispatch')
class HomeTemplateView(generic.TemplateView):
    template_name = 'home/home.html'
