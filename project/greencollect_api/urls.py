from django.urls import path, include

from .views import (
    WasteView,
)

urlpatterns = [
    path('waste', WasteView.as_view()),
]