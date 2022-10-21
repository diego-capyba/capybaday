from django.views.generic.base import TemplateView

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Dragon
from .serializers import DragonSerializer


class DragonIndexView(TemplateView):

    template_name = "dragons.html"

    def get_context_data(self, **kwargs):
        queryset = Dragon.objects.all()
        context = super().get_context_data(**kwargs)
        context['dragons'] = queryset
        context['query'] = queryset.query
        context['size'] = len(queryset)
        return context
