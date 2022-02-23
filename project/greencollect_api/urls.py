from django.urls import path, include

from .views import (
    WasteView,
    CommunityCollectDetailsView,
    CommunityCollectView,
    PreventiveView,
    PreventiveDetailsView,
)

urlpatterns = [
    path('waste', WasteView.as_view()),
    path('communityCollect/', CommunityCollectView.as_view()),
    path('communityCollectDetails/<int:id>/', CommunityCollectDetailsView.as_view()),
    path('preventive/', PreventiveView.as_view()),
    path('preventiveDetails/<int:id>/', PreventiveDetailsView.as_view()),
]