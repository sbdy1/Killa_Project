from rest_framework import viewsets
from .models import mma
from .serializers import mmaSerializer
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
import csv
import json

class mmaViewSet(viewsets.ModelViewSet):
    queryset = mma.objects.all()
    serializer_class = mmaSerializer

class mmaListView(ListView):
    model = mma
    template_name = 'mma.html'
    context_object_name = 'mma_list'

def get_csv_data():
       with open("/Users/david/killa_project/mma.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        data_list = []
        # Iterate over the rows in the CSV file
        for row in csv_reader:
            # Convert each row to a string and append it to the data_list
            data_list.append(str(row))
       return data_list