from django.urls import path, include

from .views import (
    ParticipationDetailsView,
    ParticipationView,
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

from .account import AccountView

urlpatterns = [
    path('account/', AccountView.as_view()),
    path('waste/', WasteView.as_view()),
    path('communityCollect/', CommunityCollectView.as_view()),
    path('communityCollectDetails/<int:id>/',
         CommunityCollectDetailsView.as_view()),
    path('preventive/', PreventiveView.as_view()),
    path('preventiveDetails/<int:id>/', PreventiveDetailsView.as_view()),
    path('points/', PointView.as_view()),
    path('pointDetails/<int:id>/', PointDetailsView.as_view()),
    path('rating/', RatingView.as_view()),
    path('rating/<int:id>/', RatingDetailsView.as_view()),
    path('participation/', ParticipationView.as_view()),
    path('participation/<int:id>/', ParticipationDetailsView.as_view())
]
