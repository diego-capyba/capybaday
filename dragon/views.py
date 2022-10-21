from django.views.generic.base import TemplateView

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Dragon
from .serializers import DragonSerializer, DragonBattleSerializer


class DragonIndexView(TemplateView):

    template_name = "dragons.html"

    def get_context_data(self, **kwargs):
        queryset = Dragon.objects.all().select_related('location').prefetch_related('riders')
        context = super().get_context_data(**kwargs)
        context['dragons'] = queryset
        context['query'] = queryset.query
        context['size'] = queryset.count()
        return context


class DragonViewSet(ModelViewSet):
    queryset = Dragon.objects.all().select_related('location').prefetch_related('riders')

    def get_serializer_class(self):
        if self.action == 'battle':
            return DragonBattleSerializer
        return DragonSerializer

    @action(detail=False, methods=['post'])
    def battle(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        winner = serializer.battle()
        return Response(data=winner)
