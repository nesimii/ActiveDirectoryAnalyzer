from django.urls import path, include

from analyzer.views import GroupsListView, GroupDetailView, UsersListView, UserDetailView, ComputersListView, \
    ComputerDetailView

urlpatterns = [
    path('groups/', GroupsListView.as_view(), name='group-list'),
    path('groups/<str:distinguishedName>/', GroupDetailView.as_view(), name='group-detail'),
    path('users/', UsersListView.as_view(), name='user-list'),
    path('users/<str:distinguishedName>/', UserDetailView.as_view(), name='user-detail'),
    path('computers/', ComputersListView.as_view(), name='computer-list'),
    path('computers/<str:distinguishedName>/', ComputerDetailView.as_view(), name='computer-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
