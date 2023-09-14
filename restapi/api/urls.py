from django.urls import path
from .views import PersonCreateView, PersonRetrieveUpdateDestroyView,PersonListView

urlpatterns = [
    path('people/', PersonCreateView.as_view(), name='person-create'),
    path('api/people/', PersonListView.as_view(), name='person-list'),
    path('people/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='person-retrieve-update-destroy'),
]
