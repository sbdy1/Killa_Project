from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import mmaViewSet, mmaListView
from mma import views

router = routers.DefaultRouter()
router.register(r'mma', mmaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mma/', mmaListView.as_view(), name='mma_list'),
    path('admin/', admin.site.urls),
    path('csv/', views.get_csv_data, name='csv_data'),
]
