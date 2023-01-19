from rest_framework import viewsets
from .models import mma
from .serializers import mmaSerializer
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

class mmaViewSet(viewsets.ModelViewSet):
    queryset = mma.objects.all()
    serializer_class = mmaSerializer

class mmaListView(ListView):
    model = mma
    template_name = 'mma.html'
    context_object_name = 'mma_list'
