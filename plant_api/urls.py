from django.urls import path
from plant_app import urls
from django.urls import path, include
from .views import Predict

urlpatterns = [
    path('', include("plant_app.urls"),name="plant_app"),
    path('predict/', Predict.as_view(), name='predict'),
]