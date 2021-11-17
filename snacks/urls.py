from django.urls import path
from .views import (SnackCreateView,
                    SnackListView,
                    SnackDeleteView,
                    SnackDetailView,
                    SnackUpdateView)


urlpatterns = [
    path('',SnackListView.as_view(), name='snack_view'),
    path('<int:pk>/',SnackDetailView.as_view(), name='snack_detail'),
    path('create/',SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/update/',SnackUpdateView.as_view(), name='snack_update'),
    path('<int:pk>/delete/',SnackDeleteView.as_view(), name='snack_delete'),

]