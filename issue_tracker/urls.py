from django.urls import path
from issue_tracker import api_views

urlpatterns = [
    path(
        'status/<int:pk>/',
        api_views.StatusPartialUpdateView.as_view(),
        name='bug_status_update'
    ),
]
