from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
     path('days-off/', views.getDaysOff),
     path('day-off/<str:pk>', views.getDayOff),
     path('users/', views.getUsers),
     path('delete-day-off/<str:pk>', views.deleteDayOff),
     path('update-day-off/<str:pk>', views.updateDayOff),
     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]