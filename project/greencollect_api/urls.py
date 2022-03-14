from django.urls import path, include
from .views import (
    ParticipationDetailsView,
    ParticipationView,
    PointAreaView,
    WasteView,
    CommunityCollectDetailsView,
    CommunityCollectView,
    PreventiveView,
    PreventiveDetailsView,
    PointView,
    PointDetailsView,
    RatingView,
    RatingDetailsView
)
from rest_framework import routers
from .account import AccountView

router = routers.DefaultRouter()
router.register(r'account', AccountView, basename='account')

urlpatterns = [
    path('waste/', WasteView.as_view()),
    path('communityCollect/', CommunityCollectView.as_view()),
    path('communityCollectDetails/<int:id>/',
         CommunityCollectDetailsView.as_view()),
    path('preventive/', PreventiveView.as_view()),
    path('preventiveDetails/<int:id>/', PreventiveDetailsView.as_view()),
    path('points/', PointView.as_view()),
    path('pointDetails/<int:id>/', PointDetailsView.as_view()),
    path('pointArea/', PointAreaView.as_view()),
    path('rating/', RatingView.as_view()),
    path('rating/<int:id>/', RatingDetailsView.as_view()),
    path('participation/', ParticipationView.as_view()),
    path('participation/<int:id>/', ParticipationDetailsView.as_view()),
    path('', include(router.urls)),
]
