import timeit
from django.views.generic.base import TemplateView

from .models import Dragon


class DragonIndexView(TemplateView):

    template_name = "dragons.html"

    def get_context_data(self, **kwargs):
        queryset = Dragon.objects.all().select_related('location').prefetch_related('riders')
        context = super().get_context_data(**kwargs)
        context['dragons'] = queryset
        context['query'] = queryset.query
        context['size'] = queryset.count()
        return context
